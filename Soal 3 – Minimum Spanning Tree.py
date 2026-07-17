# Soal 3 – Minimum Spanning Tree (Prim/Kruskal)

# Kasus

# Sebuah perusahaan ingin memasang kabel jaringan antar gedung.

# Gedung	Gedung	Biaya
# A	B	4
# A	H	8
# B	H	11
# B	C	8
# C	D	7
# C	I	2
# C	F	4
# D	E	9
# D	F	14
# E	F	10
# F	G	2
# G	H	1
# G	I	6
# H	I	7

# Tugas

# Simpan graf menggunakan adjacency list atau edge list.
# Implementasikan algoritma Prim.
# Implementasikan algoritma Kruskal.
# Tampilkan:
# Seluruh edge yang dipilih.
# Total biaya Minimum Spanning Tree.
# Bandingkan hasil kedua algoritma.

# Contoh Output

# Prim MST

# G-H (1)
# C-I (2)
# F-G (2)
# A-B (4)
# C-F (4)
# C-D (7)
# A-H (8)
# D-E (9)

# Total Cost = 37

# Kruskal MST

# G-H (1)
# C-I (2)
# F-G (2)
# A-B (4)
# C-F (4)
# C-D (7)
# A-H (8)
# D-E (9)

# Total Cost = 37

# Kompetensi yang Diukur

# Soal	Kompetensi
# 1	Implementasi Adjacency List, Queue, BFS, dan Dijkstra untuk Single Source Shortest Path
# 2	Implementasi Bellman-Ford, deteksi relaksasi, dan Floyd-Warshall untuk All Pairs Shortest Path
# 3	Implementasi algoritma Greedy pada Minimum Spanning Tree menggunakan Prim dan Kruskal, serta perbandingan hasil

# Ketiga soal tersebut sesuai untuk UAS Praktikum Struktur Data/Algoritma karena menguji kemampuan mahasiswa dalam merepresentasikan graf, mengimplementasikan algoritma inti tanpa library khusus, dan menganalisis hasil yang diperoleh.

# Catatan: Urutan edge pada hasil Prim dapat berbeda bergantung pada simpul awal dan urutan edge dalam priority queue, tetapi total biaya MST tetap sama (37).

# Penjelasan Program
# 1. Representasi Graf

# Graf berbobot tak berarah direpresentasikan sebagai Adjacency List.

# A
# ├── B (4)
# └── H (8)

# B
# ├── A (4)
# ├── C (8)
# └── H (11)

# ...

# 2. Algoritma Prim

# Prim membangun MST mulai dari satu simpul awal.

# Langkah-langkah:

# Pilih satu simpul awal (A).
# Masukkan semua edge yang terhubung ke priority queue.
# Pilih edge dengan bobot terkecil.
# Jika simpul tujuan belum dikunjungi, tambahkan edge ke MST.
# Ulangi hingga semua simpul telah terhubung.

# Ilustrasi

# Mulai dari A.

# Langkah 1

# Visited
# A

# Edge tersedia

# A-B = 4
# A-H = 8

# Pilih

# A-B

# Langkah 2

# Sekarang

# Visited

# A
# B

# Edge yang tersedia

# A-H = 8
# B-H = 11
# B-C = 8

# Pilih salah satu edge berbobot minimum (8), misalnya:

# A-H

# Langkah 3
# Visited

# A
# B
# H

# Edge minimum berikutnya

# H-G = 1

# Langkah Selanjutnya

# G-F = 2

# F-C = 4

# C-I = 2

# C-D = 7

# D-E = 9

# Semua simpul telah terhubung.

# Hasil Prim

# Edge	Bobot
# A-B	4
# A-H	8
# H-G	1
# G-F	2
# F-C	4
# C-I	2
# C-D	7
# D-E	9

# Total

# 4+8+1+2+4+2+7+9
# =
# 37

# 3. Algoritma Kruskal

# Berbeda dengan Prim, Kruskal tidak memilih simpul awal.

# Langkah pertama adalah mengurutkan semua edge berdasarkan bobot.

# Edge setelah diurutkan

# Edge	Bobot
# G-H	1
# C-I	2
# F-G	2
# A-B	4
# C-F	4
# C-D	7
# H-I	7
# A-H	8
# B-C	8
# D-E	9
# E-F	10
# B-H	11
# D-F	14

# Kemudian dipilih satu per satu.

# Jika edge membentuk siklus, maka edge tersebut dilewati.

# Contoh

# Dipilih

# G-H

# Tidak membentuk siklus.

# Dipilih

# C-I

# Tidak membentuk siklus.

# Dipilih

# F-G

# Tidak membentuk siklus.

# Dipilih

# A-B

# Tidak membentuk siklus.

# Dipilih

# C-F

# Tidak membentuk siklus.

# Dipilih

# C-D

# Tidak membentuk siklus.

# Kemudian

# H-I

# Membentuk siklus sehingga tidak dipilih.

# Selanjutnya

# A-H

# Menghubungkan dua komponen berbeda, sehingga dipilih.

# Terakhir

# D-E

# Semua simpul telah terhubung.

# Hasil Kruskal

# Edge	Bobot
# G-H	1
# C-I	2
# F-G	2
# A-B	4
# C-F	4
# C-D	7
# A-H	8
# D-E	9

# Total

# 37

# Perbandingan Prim dan Kruskal

# Aspek	Prim	Kruskal
# Mulai dari simpul	Ya	Tidak
# Strategi	Mengembangkan satu pohon dari simpul awal	Memilih edge berbobot terkecil secara global
# Struktur data utama	Priority Queue (Min Heap)	Union-Find (Disjoint Set)
# Deteksi siklus	Melalui simpul yang telah dikunjungi	Menggunakan Union-Find

# Kompleksitas waktu	O(E log V)	O(E log E) (≈ O(E log V))

# Kesimpulan

# Prim membangun MST dengan memperluas pohon dari sebuah simpul awal menggunakan priority queue.
# Kruskal membangun MST dengan memilih edge berbobot minimum secara global dan menghindari siklus menggunakan Union-Find (Disjoint Set).
# Untuk graf pada soal, kedua algoritma menghasilkan Minimum Spanning Tree dengan total biaya 37, meskipun urutan edge yang dipilih dapat berbeda. Hal ini menunjukkan bahwa beberapa MST yang berbeda dapat memiliki total bobot minimum yang sama.

# kode :

import heapq

# ==========================================
# Data Graf
# ==========================================

vertices = ['A','B','C','D','E','F','G','H','I']

edges = [
    ('A','B',4),
    ('A','H',8),
    ('B','H',11),
    ('B','C',8),
    ('C','D',7),
    ('C','I',2),
    ('C','F',4),
    ('D','E',9),
    ('D','F',14),
    ('E','F',10),
    ('F','G',2),
    ('G','H',1),
    ('G','I',6),
    ('H','I',7)
]

# ==========================================
# Membuat Adjacency List
# ==========================================

graph = {}

for v in vertices:
    graph[v] = []

for u, v, w in edges:
    graph[u].append((v, w))
    graph[v].append((u, w))


# ==========================================
# Algoritma Prim
# ==========================================

def prim(graph, start):

    visited = set()

    pq = []

    mst = []

    total_cost = 0

    visited.add(start)

    for neighbor, weight in graph[start]:
        heapq.heappush(pq, (weight, start, neighbor))

    while pq:

        weight, u, v = heapq.heappop(pq)

        if v in visited:
            continue

        visited.add(v)

        mst.append((u, v, weight))

        total_cost += weight

        for next_vertex, next_weight in graph[v]:

            if next_vertex not in visited:
                heapq.heappush(
                    pq,
                    (next_weight, v, next_vertex)
                )

    return mst, total_cost


# ==========================================
# Disjoint Set (Union Find)
# ==========================================

parent = {}

rank = {}

def make_set(vertices):

    for v in vertices:
        parent[v] = v
        rank[v] = 0

def find(v):

    if parent[v] != v:
        parent[v] = find(parent[v])

    return parent[v]

def union(v1, v2):

    root1 = find(v1)
    root2 = find(v2)

    if root1 == root2:
        return

    if rank[root1] < rank[root2]:
        parent[root1] = root2

    elif rank[root1] > rank[root2]:
        parent[root2] = root1

    else:
        parent[root2] = root1
        rank[root1] += 1


# ==========================================
# Algoritma Kruskal
# ==========================================

def kruskal(vertices, edges):

    make_set(vertices)

    mst = []

    total_cost = 0

    edges = sorted(edges, key=lambda x: x[2])

    for u, v, weight in edges:

        if find(u) != find(v):

            union(u, v)

            mst.append((u, v, weight))

            total_cost += weight

    return mst, total_cost


# ==========================================
# Program Utama
# ==========================================

print("===== PRIM =====")

mst, cost = prim(graph, 'A')

for u, v, w in mst:
    print(f"{u} - {v} = {w}")

print("Total Cost =", cost)


print("\n===== KRUSKAL =====")

mst, cost = kruskal(vertices, edges)

for u, v, w in mst:
    print(f"{u} - {v} = {w}")

print("Total Cost =", cost)

# output:
# ===== PRIM =====
# A - B = 4
# A - H = 8
# H - G = 1
# G - F = 2
# F - C = 4
# C - I = 2
# C - D = 7
# D - E = 9
# Total Cost = 37

# ===== KRUSKAL =====
# G - H = 1
# C - I = 2
# F - G = 2
# A - B = 4
# C - F = 4
# C - D = 7
# A - H = 8
# D - E = 9
# Total Cost = 37