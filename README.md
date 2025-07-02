# 🚇 Metro Simülasyonu (Rota Optimizasyonu)

Bu proje, bir metro ağında iki istasyon arasındaki:

- **En az aktarma gerektiren rota** (BFS Algoritması)
- **En hızlı rota** (A\* Algoritması) bulmayı amaçlayan bir Python simülasyonudur.

Ayrıca proje, **görselleştirme desteği** ile metro hattını bir graf olarak sunmaktadır. Kullanıcılar, istasyonlar arasındaki en optimum rotayı bulabilir ve metro ağının yapısını detaylı bir şekilde inceleyebilirler.

---

## 📌 Kullanılan Teknolojiler ve Kütüphaneler

Bu projede aşağıdaki teknolojiler ve kütüphaneler kullanılmıştır:

- **Python 3** (Ana programlama dili)
- **collections.deque** (BFS için kuyruk yapısı)
- **heapq** (A\* algoritması için öncelik kuyruğu)
- **functools.total_ordering** (Karşılaştırma işlemleri için)
- **networkx ve matplotlib** (Metro ağının görselleştirilmesi için)

---

## 🔍 Algoritmaların Çalışma Mantığı

### 🔵 **BFS Algoritması (En Az Aktarmalı Rota)**

- **Genişlik Öncelikli Arama (Breadth-First Search - BFS)** kullanılarak **en az aktarma gerektiren** rota bulunur.
- **Kuyruk (Queue) yapısı** kullanılarak en kısa adım sayısı ile hedefe ulaşan yol belirlenir.

### 🔴 *A\** Algoritması (En Hızlı Rota)*

- *A\** Algoritması*, **Dijkstra + Heuristik** yaklaşımı ile en hızlı gidilebilecek rotayı belirler.
- **Öncelik kuyruğu (heapq)** ile en düşük maliyetli istasyonlar öncelikli işlenerek hesaplanır.
- **Heuristik (H) fonksiyonu** olarak her istasyon arası tahmini **3 dakika** olarak belirlenmiştir.

### 🖼️ **Metro Ağını Görselleştirme**

- **NetworkX** kullanarak istasyonlar **düğüm (node)**, hat bağlantıları **kenar (edge)** olarak modellenmiştir.
- **Matplotlib** kullanarak metro hattı grafik olarak sunulmuştur.

---

## 🛠️ Nasıl Çalıştırılır?

1. **Gerekli kütüphaneleri yükleyin:**
   
sh
   pip install networkx matplotlib

2. **Projeyi çalıştırmak için:**
   
sh
   python MetehanOzay_metro_simulation.py

3. **Ana menüden işlem seçeceksiniz:**
   - **1️⃣ Metro Ağını Görselleştir** → Metro hattının grafik olarak görüntülenmesini sağlar.
   - **2️⃣ Rota Sorgula** → Kullanıcının belirlediği iki istasyon arasındaki en hızlı ve en az aktarmalı rotayı hesaplar.
   - **3️⃣ Test Senaryolarını Çalıştır** → Önceden belirlenmiş bazı istasyonlar arasında rota hesaplamalarını çalıştırarak algoritmaların doğruluğunu test eder.
   - **4️⃣ Çıkış Yap** → Programdan çıkış yapar.

---

## 🚀 Örnek Kullanım & Çıktılar

### 🎯 **Örnek 1: AŞTİ'den OSB'ye Rota Bulma**

sh
📍 En az aktarmalı rota: AŞTİ -> Kızılay -> Ulus -> Demetevler -> OSB
🚄 En hızlı rota (18 dakika): AŞTİ -> Kızılay -> Ulus -> Demetevler -> OSB



---

## 🔗 Kaynaklar

- [BFS Algoritması](https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/)
- [A\* Algoritması](https://www.redblobgames.com/pathfinding/a-star/introduction.html)
- [Python Collections](https://docs.python.org/3/library/collections.html)
- [Python Heapq](https://docs.python.org/3/library/heapq.html)
- [NetworkX Belgeleri](https://networkx.org/documentation/stable/)

---

📌 **Bu proje Global AI Hub "Python ve Yapay Zekaya Giriş Bootcamp" Mart 2025 kapsamında geliştirilmiştir.** 🚀
