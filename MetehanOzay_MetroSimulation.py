from collections import defaultdict
import heapq
import networkx as nx
import matplotlib.pyplot as plt

from typing import Dict, List, Optional

from functools import total_ordering


@total_ordering
class Istasyon:
    def __init__(self, idx: str, ad: str, hat: str):
        self.idx = idx
        self.ad = ad
        self.hat = hat
        self.komsular = []  # (istasyon, süre) tuple'ları

    def komsu_ekle(self, komsu_istasyon: 'Istasyon', gecis_suresi: int):
        self.komsular.append((komsu_istasyon, gecis_suresi))

    def __eq__(self, other):
        return self.idx == other.idx

    def __lt__(self, other):
        return self.idx < other.idx  # ID’ye göre sıralama yapacak

    def __hash__(self):
        return hash(self.idx)  # İstasyonların ID’sine göre hash oluşturuyoruz


class MetroAgi:
    def __init__(self):
        self.istasyonlar: Dict[str, Istasyon] = {}
        self.hatlar: Dict[str, List[Istasyon]] = defaultdict(list)

    def istasyon_ekle(self, istasyon_id: str, ad: str, hat: str) -> None:
        if istasyon_id not in self.istasyonlar:
            yeni_istasyon = Istasyon(istasyon_id, ad, hat)
            self.istasyonlar[istasyon_id] = yeni_istasyon
            self.hatlar[hat].append(yeni_istasyon)

    def baglanti_ekle(self, istasyon1_id: str, istasyon2_id: str, gecis_suresi: int) -> None:
        istasyon1 = self.istasyonlar[istasyon1_id]
        istasyon2 = self.istasyonlar[istasyon2_id]
        istasyon1.komsu_ekle(istasyon2, gecis_suresi)
        istasyon2.komsu_ekle(istasyon1, gecis_suresi)

    def en_az_aktarma_bul(self, baslangic_id1: str, hedef_id1: str) -> Optional[List[Istasyon]]:
        """BFS algoritması kullanarak en az aktarmalı rotayı bulur"""
        from collections import deque  # Gerekli modülü kullanıyoruz

        if baslangic_id1 not in self.istasyonlar or hedef_id1 not in self.istasyonlar:
            return None

        baslangic = self.istasyonlar[baslangic_id1]
        hedef_istasyon = self.istasyonlar[hedef_id1]

        kuyruk = deque([(baslangic, [baslangic])])  # (Şu anki istasyon, şu ana kadar olan yol)
        ziyaret_edilenler = set()

        while kuyruk:
            mevcut_istasyon, yol = kuyruk.popleft()

            if mevcut_istasyon == hedef_istasyon:
                return yol  # En az aktarmalı rota bulundu

            ziyaret_edilenler.add(mevcut_istasyon)

            for komsu, _ in mevcut_istasyon.komsular:
                if komsu not in ziyaret_edilenler:
                    kuyruk.append((komsu, yol + [komsu]))
                    ziyaret_edilenler.add(komsu)  # Burada ekleyerek tekrar kuyruğa eklenmesini engelliyoruz

        return None  # Eğer rota bulunamazsa

    def en_hizli_rota_bul(self, baslangic_id: str, hedef_id: str):
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None

        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]

        def heuristic(istasyon: Istasyon) -> int:
            """Heuristik fonksiyon: Şu an basit bir tahmin olarak her istasyon arası 3 dakika alınmıştır."""
            return 3  # Daha gerçekçi bir model için coğrafi mesafe kullanılabilir.

        oncelik_kuyrugu = [(0 + heuristic(baslangic), 0, baslangic, [baslangic])]  # (F = G + H, G, istasyon, yol)
        ziyaret_edilenler = {}

        while oncelik_kuyrugu:
            _, toplam_sure, mevcut_istasyon, yol = heapq.heappop(oncelik_kuyrugu)

            if mevcut_istasyon == hedef:
                return yol, toplam_sure  # En hızlı rota bulundu

            if mevcut_istasyon in ziyaret_edilenler and ziyaret_edilenler[mevcut_istasyon] <= toplam_sure:
                continue  # Daha iyi bir rota zaten bulunduysa devam etme

            ziyaret_edilenler[mevcut_istasyon] = toplam_sure

            for komsu, sure in mevcut_istasyon.komsular:
                yeni_toplam_sure = toplam_sure + sure
                heapq.heappush(oncelik_kuyrugu,
                               (yeni_toplam_sure + heuristic(komsu), yeni_toplam_sure, komsu, yol + [komsu]))

        return None  # Eğer rota bulunamazsa

class MetroAgiVisualizer:
    def __init__(self, metro_agi):
        self.metro_agi = metro_agi
        self.graf = nx.Graph()

    def grafigi_olustur(self):
        """Metro ağını NetworkX ile bir graf olarak oluşturur"""
        for istasyon in self.metro_agi.istasyonlar.values():
            self.graf.add_node(istasyon.idx, label=istasyon.ad, color=self.get_hat_rengi(istasyon.hat))

        for istasyon in self.metro_agi.istasyonlar.values():
            for komsu, sure in istasyon.komsular:
                if not self.graf.has_edge(istasyon.idx, komsu.idx):  # Çift yönlü bağlantıyı önlemek için kontrol
                    self.graf.add_edge(istasyon.idx, komsu.idx, weight=sure, color=self.get_hat_rengi(istasyon.hat))

    def get_hat_rengi(self, hat):
        """Metro hatları için özel renkler belirler"""
        renkler = {
            "Kırmızı Hat": "#E63946",   # Kırmızı
            "Mavi Hat": "#1D3557",      # Koyu Mavi
            "Turuncu Hat": "#F4A261",   # Turuncu
            "Yeşil Hat": "#2A9D8F",     # Yeşil (Ekstra hat eklenirse)
            "Mor Hat": "#9B5DE5"        # Mor (Ekstra hat eklenirse)
        }
        return renkler.get(hat, "#6D6875")  # Varsayılan olarak gri-mor tonu

    def grafigi_ciz(self):
        pos = nx.spring_layout(self.graf, seed=42)  # Daha dengeli bir yerleşim

        # Aktarma istasyonlarını belirleme
        node_sizes = [3500 if len(self.metro_agi.istasyonlar[n].komsular) > 2 else 2000 for n in self.graf.nodes]

        # Kenar renklerini ve kalınlıklarını belirleme
        kenar_kalinliklari = [1 + (data["weight"] / 2) for _, _, data in self.graf.edges(data=True)]

        plt.figure(figsize=(12, 8))
        nx.draw(self.graf, pos, labels=nx.get_node_attributes(self.graf, "label"),
                with_labels=True, node_color=[data["color"] for _, data in self.graf.nodes(data=True)],
                edge_color=[data["color"] for _, _, data in self.graf.edges(data=True)],
                font_size=12, node_size=node_sizes, font_weight="bold", width=kenar_kalinliklari)

        # Süreleri ekle
        edge_labels = {(a, b): d["weight"] for a, b, d in self.graf.edges(data=True)}
        nx.draw_networkx_edge_labels(self.graf, pos, edge_labels=edge_labels, font_size=10)

        plt.title("Geliştirilmiş Metro Haritası", fontsize=14)
        plt.show()


# Örnek Kullanım
if __name__ == "__main__":
    metro = MetroAgi()

    # İstasyonlar ekleme
    # Kırmızı Hat
    metro.istasyon_ekle("K1", "Kızılay", "Kırmızı Hat")
    metro.istasyon_ekle("K2", "Ulus", "Kırmızı Hat")
    metro.istasyon_ekle("K3", "Demetevler", "Kırmızı Hat")
    metro.istasyon_ekle("K4", "OSB", "Kırmızı Hat")

    # Mavi Hat
    metro.istasyon_ekle("M1", "AŞTİ", "Mavi Hat")
    metro.istasyon_ekle("M2", "Kızılay", "Mavi Hat")  # Aktarma noktası
    metro.istasyon_ekle("M3", "Sıhhiye", "Mavi Hat")
    metro.istasyon_ekle("M4", "Gar", "Mavi Hat")

    # Turuncu Hat
    metro.istasyon_ekle("T1", "Batıkent", "Turuncu Hat")
    metro.istasyon_ekle("T2", "Demetevler", "Turuncu Hat")  # Aktarma noktası
    metro.istasyon_ekle("T3", "Gar", "Turuncu Hat")  # Aktarma noktası
    metro.istasyon_ekle("T4", "Keçiören", "Turuncu Hat")

    # Bağlantılar ekleme
    # Kırmızı Hat bağlantıları
    metro.baglanti_ekle("K1", "K2", 4)  # Kızılay -> Ulus
    metro.baglanti_ekle("K2", "K3", 6)  # Ulus -> Demetevler
    metro.baglanti_ekle("K3", "K4", 8)  # Demetevler -> OSB

    # Mavi Hat bağlantıları
    metro.baglanti_ekle("M1", "M2", 5)  # AŞTİ -> Kızılay
    metro.baglanti_ekle("M2", "M3", 3)  # Kızılay -> Sıhhiye
    metro.baglanti_ekle("M3", "M4", 4)  # Sıhhiye -> Gar

    # Turuncu Hat bağlantıları
    metro.baglanti_ekle("T1", "T2", 7)  # Batıkent -> Demetevler
    metro.baglanti_ekle("T2", "T3", 9)  # Demetevler -> Gar
    metro.baglanti_ekle("T3", "T4", 5)  # Gar -> Keçiören

    # Hat aktarma bağlantıları (aynı istasyon farklı hatlar)
    metro.baglanti_ekle("K1", "M2", 2)  # Kızılay aktarma
    metro.baglanti_ekle("K3", "T2", 3)  # Demetevler aktarma
    metro.baglanti_ekle("M4", "T3", 2)  # Gar aktarma

    while True:
        print("\n=== Metro Sistemi ===")
        print("1️⃣ Metro ağını görselleştir")
        print("2️⃣ Rota sorgula")
        print("3️⃣ Test senaryolarını çalıştır")
        print("4️⃣ Çık")


        try:
            secim = input("Lütfen bir seçenek girin: ").strip()
        except KeyboardInterrupt:
            print("\n🚨 Program kullanıcı tarafından kapatıldı. Çıkılıyor...")
            exit()

        if secim == "1":
            print("\n🖼 Metro ağı görselleştiriliyor...")
            visualizer = MetroAgiVisualizer(metro)
            visualizer.grafigi_olustur()
            visualizer.grafigi_ciz()

        elif secim == "2":
            while True:
                print("\nMevcut istasyonlar:")
                for istasyon in metro.istasyonlar.values():
                    print(f"- {istasyon.ad} ({istasyon.idx}) [{istasyon.hat}]")

                baslangic_adi = input("\nBaşlangıç istasyonunun adını girin: ").strip()
                hedef_adi = input("Hedef istasyonunun adını girin: ").strip()

                # Kullanıcının girdiği ismi al ve doğru ID'yi bul
                baslangic_id = None
                hedef_id = None

                for id, ist in metro.istasyonlar.items():
                    if ist.ad.lower() == baslangic_adi.lower():
                        baslangic_id = id
                    if ist.ad.lower() == hedef_adi.lower():
                        hedef_id = id

                if not baslangic_id or not hedef_id:
                    print("❌ Geçersiz istasyon adı girdiniz! Lütfen listeden bir ad seçin.")
                    exit()

                print("\n📍 En az aktarmalı rota:")
                rota = metro.en_az_aktarma_bul(baslangic_id, hedef_id)
                if rota:
                    print(" -> ".join(i.ad for i in rota))
                else:
                    print("⚠ Rota bulunamadı!")

                print("\n🚄 En hızlı rota:")
                sonuc = metro.en_hizli_rota_bul(baslangic_id, hedef_id)
                if sonuc:
                    rota, sure = sonuc
                    print(f"({sure} dakika) " + " -> ".join(i.ad for i in rota))
                else:
                    print("⚠ Rota bulunamadı!")

                devam = input("\nYeni bir sorgu yapmak ister misiniz? (E/H): ").strip().lower()
                if devam != 'e':
                    break

        elif secim == "3":

            # Test senaryoları
            print("\n=== Test Senaryoları ===")

            # Senaryo 1: AŞTİ'den OSB'ye
            print("\n1. AŞTİ'den OSB'ye:")
            rota = metro.en_az_aktarma_bul("M1", "K4")
            if rota:
                print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))

            sonuc = metro.en_hizli_rota_bul("M1", "K4")
            if sonuc:
                rota, sure = sonuc
                print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))

            # Senaryo 2: Batıkent'ten Keçiören'e
            print("\n2. Batıkent'ten Keçiören'e:")
            rota = metro.en_az_aktarma_bul("T1", "T4")
            if rota:
                print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))

            sonuc = metro.en_hizli_rota_bul("T1", "T4")
            if sonuc:
                rota, sure = sonuc
                print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))

            # Senaryo 3: Keçiören'den AŞTİ'ye
            print("\n3. Keçiören'den AŞTİ'ye:")
            rota = metro.en_az_aktarma_bul("T4", "M1")
            if rota:
                print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))

            sonuc = metro.en_hizli_rota_bul("T4", "M1")
            if sonuc:
                rota, sure = sonuc
                print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))

            print("\n🔍 Test senaryoları çalıştırılıyor...")

            testler = [
                ("M1", "K4"),  # AŞTİ -> OSB
                ("T1", "T4"),  # Batıkent -> Keçiören
                ("T4", "M1")  # Keçiören -> AŞTİ
            ]

            for baslangic, hedef in testler:
                print(f"\n{metro.istasyonlar[baslangic].ad} → {metro.istasyonlar[hedef].ad}:")

                rota = metro.en_az_aktarma_bul(baslangic, hedef)
                if rota:
                    print("📍 En az aktarmalı rota:", " -> ".join(i.ad for i in rota))

                sonuc = metro.en_hizli_rota_bul(baslangic, hedef)
                if sonuc:
                    rota, sure = sonuc
                    print(f"🚄 En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))

        elif secim == "4":
            print("🚪 Programdan çıkılıyor...")
            break

        else:
            print("⚠ Geçersiz seçim! Lütfen 1, 2, 3 veya 4 girin.")