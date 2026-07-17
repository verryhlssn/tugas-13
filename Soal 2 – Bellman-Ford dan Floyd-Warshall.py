# Soal 2 – Bellman-Ford dan Floyd-Warshall

# Kasus

# Diberikan graf berbobot berikut.

# Dari	Ke	Bobot
# A	B	4
# A	C	2
# B	C	-2
# B	D	3
# C	D	2
# D	E	2
# E	B	-1

# Graf dapat memiliki bobot negatif tetapi tidak mengandung negative cycle.

# Tugas

# Simpan graf dalam bentuk Edge List.
# Implementasikan algoritma Bellman-Ford dengan sumber A.
# Tampilkan:
# Distance setiap vertex.
# Jalur terpendek menuju E.
# Implementasikan algoritma Floyd-Warshall.
# Cetak matriks jarak terpendek antar seluruh pasangan vertex.

# Contoh Output

# Bellman Ford

# A : 0
# B : 4
# C : 2
# D : 4
# E : 6

# Shortest Path A -> E
# A -> C -> D -> E

# Floyd Warshall Matrix

#       A  B  C  D  E
# A     0  4  2  4  6
# B    INF 0 -2  0  2
# C    INF INF 0  2  4
# D    INF 1 -1 0  2
# E    INF -1 -3 1  0

# Penjelasan Program
# 1. Representasi Graf

# Graf disimpan dalam bentuk Edge List.

# edges = [
#     ('A','B',4),
#     ('A','C',2),
#     ...
# ]

# Artinya

# A --4--> B
# A --2--> C
# B ---2--> C
# B --3--> D
# C --2--> D
# D --2--> E
# E ---1--> B

# 2. Bellman-Ford

# Bellman-Ford digunakan untuk mencari Single Source Shortest Path (SSSP) pada graf yang dapat memiliki bobot negatif.

# Algoritma melakukan relaksasi sebanyak |V|−1 kali.

# Karena terdapat 5 simpul,

# |V|-1 = 4 iterasi

# Iterasi 1

# Awal

# Vertex	Distance
# A	0
# B	∞
# C	∞
# D	∞
# E	∞

# Relaksasi seluruh edge

# A→B = 4
# A→C = 2
# B→C = 2
# B→D = 7
# C→D = 4
# D→E = 6
# E→B = belum

# Hasil

# Vertex	Distance
# A	0
# B	4
# C	2
# D	4
# E	6

# Iterasi 2

# Semua edge diperiksa kembali.

# Tidak ada lagi jarak yang menjadi lebih kecil.

# Begitu juga iterasi ke-3 dan ke-4.

# Maka hasil akhirnya

# Vertex	Distance
# A	0
# B	4
# C	2
# D	4
# E	6

# Jalur Terpendek

# Array predecessor

# B ← A
# C ← A
# D ← C
# E ← D

# Sehingga

# A
# ↓
# C
# ↓
# D
# ↓
# E

# Total

# 2 + 2 + 2 = 6

# 3. Deteksi Negative Cycle

# Bellman-Ford selalu melakukan pemeriksaan satu kali lagi.

# Jika masih ada edge yang dapat diperkecil,

# distance[u] + weight < distance[v]

# berarti terdapat Negative Cycle.

# Pada graf soal tidak ditemukan negative cycle, sehingga algoritma berhenti normal.

# 4. Floyd-Warshall

# Floyd-Warshall mencari jarak terpendek untuk seluruh pasangan simpul (All Pairs Shortest Path/APSP).

# Awalnya dibuat matriks

# 	A	B	C	D	E
# A	0	4	2	∞	∞
# B	∞	0	-2	3	∞
# C	∞	∞	0	2	∞
# D	∞	∞	∞	0	2
# E	∞	-1	∞	∞	0

# Kemudian setiap simpul dipakai sebagai simpul perantara:

# k = A
# k = B
# k = C
# k = D
# k = E

# Jika

# i → k → j

# lebih pendek daripada

# i → j

# maka nilai matriks diperbarui.

# Hasil akhirnya

# 	A	B	C	D	E
# A	0	4	2	4	6
# B	∞	0	-2	0	2
# C	∞	3	0	2	4
# D	∞	1	-1	0	2
# E	∞	-1	-3	1	0

# Matriks ini menunjukkan jarak terpendek dari setiap simpul ke semua simpul lainnya.

# Kompleksitas Algoritma

# Algoritma	Waktu	Ruang
# Bellman-Ford	O(V × E)	O(V)
# Floyd-Warshall	O(V³)	O(V²)

# Keterangan:

# V = jumlah simpul (vertex).
# E = jumlah sisi (edge).

# Kesimpulan

# Bellman-Ford digunakan untuk Single Source Shortest Path (SSSP) dan mampu menangani bobot negatif selama tidak terdapat negative cycle.
# Floyd-Warshall digunakan untuk All Pairs Shortest Path (APSP), yaitu menghitung jarak terpendek antara setiap pasangan simpul dalam graf.

# Pada graf soal:
# Jarak terpendek dari A ke E adalah 6 melalui jalur A → C → D → E.

# Matriks hasil Floyd-Warshall memberikan jarak minimum untuk seluruh pasangan simpul dan dapat digunakan untuk menjawab query jarak apa pun tanpa menjalankan algoritma ulang.

# kode :

# ==========================================
# Edge List
# ==========================================

vertices = ['A', 'B', 'C', 'D', 'E']

edges = [
    ('A', 'B', 4),
    ('A', 'C', 2),
    ('B', 'C', -2),
    ('B', 'D', 3),
    ('C', 'D', 2),
    ('D', 'E', 2),
    ('E', 'B', -1)
]

# ==========================================
# Bellman-Ford Algorithm
# ==========================================

def bellman_ford(vertices, edges, source):
    distance = {v: float('inf') for v in vertices}
    previous = {v: None for v in vertices}

    distance[source] = 0

    # Relaksasi sebanyak |V|-1 kali
    for i in range(len(vertices) - 1):
        for u, v, w in edges:
            if distance[u] != float('inf') and distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
                previous[v] = u

    # Deteksi Negative Cycle
    for u, v, w in edges:
        if distance[u] != float('inf') and distance[u] + w < distance[v]:
            print("Graf memiliki Negative Cycle")
            return None, None

    return distance, previous


# ==========================================
# Menampilkan Path
# ==========================================

def get_path(previous, target):
    path = []

    while target is not None:
        path.append(target)
        target = previous[target]

    path.reverse()
    return path


# ==========================================
# Floyd-Warshall Algorithm
# ==========================================

def floyd_warshall(vertices, edges):

    n = len(vertices)

    index = {vertices[i]: i for i in range(n)}

    INF = float('inf')

    dist = [[INF] * n for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0

    for u, v, w in edges:
        i = index[u]
        j = index[v]
        dist[i][j] = w

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist, index


# ==========================================
# Main Program
# ==========================================

distance, previous = bellman_ford(vertices, edges, 'A')

print("===== Bellman-Ford =====")

for v in vertices:
    print(f"A -> {v} = {distance[v]}")

print("\nShortest Path A ke E")

path = get_path(previous, 'E')

print(" -> ".join(path))

print("\n")

dist, index = floyd_warshall(vertices, edges)

print("===== Floyd Warshall =====")

print("     ", end="")

for v in vertices:
    print(f"{v:>5}", end="")

print()

for i in range(len(vertices)):
    print(f"{vertices[i]:>5}", end="")

    for j in range(len(vertices)):

        if dist[i][j] == float('inf'):
            print(f"{'INF':>5}", end="")
        else:
            print(f"{dist[i][j]:>5}", end="")

    print()

# Output:
# ===== Floyd Warshall =====
#         A    B    C    D    E
#    A    0    4    2    4    6
#    B  INF    0   -2    0    2
#    C  INF    3    0    2    4
#    D  INF    1   -1    0    2
#    E  INF   -1   -3   -1    0