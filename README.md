# 🚇 Metro Simulation (Route Optimization)

This project is a Python simulation that aims to find between two stations in a metro network:

- **The route requiring the least number of transfers** (BFS Algorithm)
- **The fastest route** (A* Algorithm)

Additionally, the project presents the metro line as a graph with **visualization support**. Users can find the most optimal route between stations and examine the structure of the metro network in detail.

---

## 📌 Technologies and Libraries Used

The following technologies and libraries were used in this project:

- **Python 3** (Main programming language)
- **collections.deque** (Queue structure for BFS)
- **heapq** (Priority queue for the A* algorithm)
- **functools.total_ordering** (For comparison operations)
- **networkx and matplotlib** (For visualizing the metro network)

---

## 🔍 Working Principle of the Algorithms

### 🔵 **BFS Algorithm (Least Transfer Route)**

- **Breadth-First Search (BFS)** is used to find the **route requiring the fewest transfers**.
- Using a **queue structure**, the path that reaches the destination with the fewest number of steps is determined.

### 🔴 *A\** Algorithm (Fastest Route)*

- The *A\** Algorithm determines the fastest possible route using the **Dijkstra + Heuristic** approach.
- The **priority queue (heapq)** is used to process the lowest-cost stations first.
- As the **Heuristic (H) function**, an estimated **3 minutes** is assigned between each station.

### 🖼️ **Visualizing the Metro Network**

- Using **NetworkX**, stations are modeled as **nodes**, and line connections as **edges**.
- The metro line is presented graphically using **Matplotlib**.

---

## 🛠️ How to Run?

1. **Install the required libraries:**

   ```sh
   pip install networkx matplotlib
   ```

2. **To run the project:**

   ```sh
   python MetehanOzay_metro_simulation.py
   ```

3. **You will select an option from the main menu:**
   - **1️⃣ Visualize the Metro Network** → Allows the metro line to be displayed graphically.
   - **2️⃣ Query Route** → Calculates the fastest and the least transfer route between two stations defined by the user.
   - **3️⃣ Run Test Scenarios** → Tests the accuracy of the algorithms by running route calculations between some predefined stations.
   - **4️⃣ Exit** → Exits the program.

---

## 🚀 Example Usage & Outputs

### 🎯 Example 1: Finding a Route from AŞTİ to OSB

```sh
📍 Least transfer route: AŞTİ -> Kızılay -> Ulus -> Demetevler -> OSB
🚄 Fastest route (18 minutes): AŞTİ -> Kızılay -> Ulus -> Demetevler -> OSB
```

---

## 🔗 Resources

- [BFS Algorithm](https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/)
- [A* Algorithm](https://www.redblobgames.com/pathfinding/a-star/introduction.html)
- [Python Collections](https://docs.python.org/3/library/collections.html)
- [Python Heapq](https://docs.python.org/3/library/heapq.html)
- [NetworkX Documentation](https://networkx.org/documentation/stable/)

---

📌 **This project was developed as part of the Global AI Hub "Introduction to Python and Artificial Intelligence Bootcamp" in March 2025.** 🚀
