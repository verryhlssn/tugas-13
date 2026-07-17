# Soal 1 – BFS dan Dijkstra (SSSP)

# Kasus

# Sebuah kota memiliki jaringan jalan seperti berikut.

# Dari	Ke	Jarak
# A	B	4
# A	C	2
# B	C	1
# B	D	5
# C	D	8
# C	E	10
# D	E	2
# D	F	6
# E	F	3

# Tugas

# Simpan graf menggunakan Adjacency List.
# Implementasikan algoritma Breadth First Search (BFS) mulai dari simpul A.
# Implementasikan algoritma Dijkstra dengan sumber A.
# Tampilkan:
# Urutan kunjungan BFS.
# Jarak minimum dari A ke seluruh simpul.
# Jalur terpendek dari A ke F.

# Contoh Output

# BFS Traversal
# A C B D E F

# Shortest Distance
# A : 0
# B : 3
# C : 2
# D : 8
# E : 10
# F : 13

# Shortest Path
# A -> C -> B -> D -> E -> F

# Penjelasan Program
# 1. Representasi Graf

# Graf disimpan menggunakan Adjacency List.

# graph = {
#     'A': [('B',4), ('C',2)],
#     ...
# }

# Artinya:

# A
# ├── B (4)
# └── C (2)

# Setiap simpul menyimpan pasangan:

# (Tetangga, Bobot)
# 2. Breadth First Search (BFS)

# Algoritma BFS menggunakan Queue (FIFO).

# Langkah-langkah:

# Masukkan simpul awal ke queue.
# Ambil simpul paling depan.
# Kunjungi semua tetangganya.
# Masukkan tetangga yang belum dikunjungi.
# Ulangi hingga queue kosong.

# Urutan kunjungan:

# Queue

# [A]

# ↓

# A

# Queue
# [B,C]

# ↓

# B

# Queue
# [C,D]

# ↓

# C

# Queue
# [D,E]

# ↓

# D

# Queue
# [E,F]

# ↓

# E

# ↓

# F

# Traversal:

# A → B → C → D → E → F

# 3. Algoritma Dijkstra

# Digunakan untuk mencari Shortest Path pada graf berbobot positif.

# Awalnya:

# Vertex	Distance
# A	0
# B	∞
# C	∞
# D	∞
# E	∞
# F	∞

# Setelah memproses A

# A→B = 4
# A→C = 2

# Vertex	Distance
# A	0
# B	4
# C	2
# D	∞
# E	∞
# F	∞

# Memproses C

# C→B = 2+1 = 3 (lebih kecil)
# C→D =10
# C→E =12

# Vertex	Distance
# A	0
# B	3
# C	2
# D	10
# E	12
# F	∞

# Memproses B

# B→D = 3+5 = 8

# Vertex	Distance
# A	0
# B	3
# C	2
# D	8
# E	12
# F	∞

# Memproses D

# D→E = 8+2 =10
# D→F =14

# Vertex	Distance
# A	0
# B	3
# C	2
# D	8
# E	10
# F	14

# Memproses E

# E→F =10+3 =13

# Hasil akhir

# Vertex	Distance
# A	0
# B	3
# C	2
# D	8
# E	10
# F	13

# 4. Jalur Terpendek

# Array previous menyimpan simpul sebelumnya.

# F ← E ← D ← B ← C ← A

# Dibalik menjadi

# A
# ↓
# C
# ↓
# B
# ↓
# D
# ↓
# E
# ↓
# F

# Total jarak

# 2 + 1 + 5 + 2 + 3 = 13

# Kompleksitas Algoritma

# Algoritma	Kompleksitas Waktu	Kompleksitas Ruang
# BFS	O(V + E)	O(V)
# Dijkstra (Priority Queue)	O((V + E) log V)	O(V)

# Keterangan:

# V = jumlah simpul (vertex).
# E = jumlah sisi (edge).

# Kesimpulan

# BFS digunakan untuk menelusuri graf berdasarkan tingkat (level) tanpa mempertimbangkan bobot sisi.
# Dijkstra digunakan untuk mencari jarak terpendek dari satu sumber ke semua simpul pada graf dengan bobot tidak negatif.
# Berdasarkan graf pada soal:
# Traversal BFS dari A adalah A → B → C → D → E → F.
# Jarak terpendek dari A ke F adalah 13.
# Jalur terpendek adalah A → C → B → D → E → F.

# kode :

from collections import deque
import heapq

# ============================
# Adjacency List
# ============================
graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('C', 1), ('D', 5)],
    'C': [('A', 2), ('B', 1), ('D', 8), ('E', 10)],
    'D': [('B', 5), ('C', 8), ('E', 2), ('F', 6)],
    'E': [('C', 10), ('D', 2), ('F', 3)],
    'F': [('D', 6), ('E', 3)]
}

# ============================
# Breadth First Search (BFS)
# ============================
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    order = []

    visited.add(start)

    while queue:
        current = queue.popleft()
        order.append(current)

        for neighbor, weight in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order


# ============================
# Dijkstra
# ============================
def dijkstra(graph, start):
    distance = {node: float('inf') for node in graph}
    previous = {node: None for node in graph}

    distance[start] = 0

    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distance[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            new_distance = current_distance + weight

            if new_distance < distance[neighbor]:
                distance[neighbor] = new_distance
                previous[neighbor] = current_node
                heapq.heappush(pq, (new_distance, neighbor))

    return distance, previous


# ============================
# Menampilkan Path
# ============================
def shortest_path(previous, start, target):
    path = []

    while target is not None:
        path.append(target)
        target = previous[target]

    path.reverse()

    return path


# ============================
# Program Utama
# ============================

print("===== BFS Traversal =====")
order = bfs(graph, 'A')
print(" -> ".join(order))

distance, previous = dijkstra(graph, 'A')

print("\n===== Shortest Distance =====")
for node in sorted(distance):
    print(f"A -> {node} = {distance[node]}")

print("\n===== Shortest Path A ke F =====")
path = shortest_path(previous, 'A', 'F')
print(" -> ".join(path))
print("Total Distance =", distance['F'])

# output:

# ===== Shortest Path A ke F =====
# A -> C -> B -> D -> E -> F
# Total Distance = 13