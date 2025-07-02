🚇 Metro Simulation (Route Optimization)
This project is a Python simulation that aims to find the following between two stations in a metro network:

The route requiring the least number of transfers (BFS Algorithm)

The fastest route (A* Algorithm)

Additionally, the project presents the metro line as a graph with visualization support. Users can find the most optimal route between stations and examine the structure of the metro network in detail.

📌 Technologies and Libraries Used
The following technologies and libraries were used in this project:

Python 3 (Main programming language)

collections.deque (Queue structure for BFS)

heapq (Priority queue for A* algorithm)

functools.total_ordering (For comparison operations)

networkx and matplotlib (For visualizing the metro network)

🔍 Logic Behind the Algorithms
🔵 BFS Algorithm (Least Transfer Route)
Uses Breadth-First Search (BFS) to find the route with the fewest transfers.

The queue structure is used to determine the path to the destination with the shortest number of steps.

🔴 A* Algorithm (Fastest Route)*
The A* algorithm determines the fastest possible route using the Dijkstra + Heuristic approach.

Priority queue (heapq) processes the lowest-cost stations first.

The heuristic (H) function assumes an estimated 3 minutes between each station.

🖼️ Visualizing the Metro Network
With NetworkX, stations are modeled as nodes, and line connections as edges.

The metro line is presented graphically using Matplotlib.

🛠️ How to Run?
Install the required libraries:

sh
Kopyala
Düzenle
pip install networkx matplotlib
To run the project:

sh
Kopyala
Düzenle
python MetehanOzay_metro_simulation.py
You will choose an action from the main menu:

1️⃣ Visualize the Metro Network → Displays the metro line as a graph.

2️⃣ Query Route → Calculates the fastest and least-transfer route between two user-selected stations.

3️⃣ Run Test Scenarios → Runs route calculations between pre-defined stations to test the accuracy of the algorithms.

4️⃣ Exit → Exits the program.

🚀 Example Usage & Outputs
🎯 Example 1: Finding a Route from AŞTİ to OSB
sh
Kopyala
Düzenle
📍 Least transfer route: AŞTİ -> Kızılay -> Ulus -> Demetevler -> OSB  
🚄 Fastest route (18 minutes): AŞTİ -> Kızılay -> Ulus -> Demetevler -> OSB
🔗 Resources
BFS Algorithm

A* Algorithm

Python Collections

Python Heapq

NetworkX Documentation

📌 This project was developed as part of the Global AI Hub "Introduction to Python and AI Bootcamp" in March 2025. 🚀
