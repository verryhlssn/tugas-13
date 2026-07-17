import heapq  # Mengimpor modul heapq untuk membuat Priority Queue (Min Heap)


class Edge:  # Mendefinisikan class Edge untuk menyimpan hubungan antar vertex
    def __init__(self, weight, start_vertex, target_vertex):  # Constructor Edge
        self.weight = weight  # Menyimpan bobot edge
        self.start_vertex = start_vertex  # Menyimpan vertex asal
        self.target_vertex = target_vertex  # Menyimpan vertex tujuan


class Node:  # Mendefinisikan class Node sebagai vertex pada graph
    def __init__(self, name):  # Constructor Node
        self.name = name  # Menyimpan nama vertex
        self.visited = False  # Menandai apakah vertex sudah dikunjungi
        self.predecessor = None  # Menyimpan vertex sebelumnya pada jalur terpendek
        self.neighbors = []  # Menyimpan daftar edge yang terhubung
        self.min_distance = float("inf")  # Mengatur jarak awal menjadi tak hingga

    def __lt__(self, other_node):  # Digunakan agar Node dapat dibandingkan di dalam heap
        return self.min_distance < other_node.min_distance  # Membandingkan berdasarkan jarak minimum

    def add_edge(self, weight, destination_vertex):  # Menambahkan edge dari node ini ke node tujuan
        edge = Edge(weight, self, destination_vertex)  # Membuat objek Edge baru
        self.neighbors.append(edge)  # Menambahkan edge ke daftar tetangga


class Dijkstra:  # Mendefinisikan class untuk algoritma Dijkstra
    def __init__(self):  # Constructor Dijkstra
        self.heap = []  # Membuat Priority Queue kosong

    def calculate(self, start_vertex):  # Fungsi untuk menghitung jarak terpendek
        start_vertex.min_distance = 0  # Mengatur jarak vertex awal menjadi 0
        heapq.heappush(self.heap, start_vertex)  # Memasukkan vertex awal ke Priority Queue

        while self.heap:  # Melakukan perulangan selama heap masih berisi data

            actual_vertex = heapq.heappop(self.heap)  # Mengambil vertex dengan jarak terkecil

            if actual_vertex.visited:  # Jika vertex sudah diproses sebelumnya
                continue  # Lewati dan lanjut ke iterasi berikutnya

            for edge in actual_vertex.neighbors:  # Menelusuri seluruh edge dari vertex aktif

                start = edge.start_vertex  # Menyimpan vertex asal edge
                target = edge.target_vertex  # Menyimpan vertex tujuan edge

                new_distance = start.min_distance + edge.weight  # Menghitung jarak baru

                if new_distance < target.min_distance:  # Jika ditemukan jarak yang lebih pendek

                    target.min_distance = new_distance  # Memperbarui jarak minimum

                    target.predecessor = start  # Menyimpan vertex sebelumnya

                    heapq.heappush(self.heap, target)  # Memasukkan kembali vertex ke Priority Queue

            actual_vertex.visited = True  # Menandai vertex sudah selesai diproses

    def get_shortest_path(self, vertex):  # Menampilkan hasil jalur terpendek
        print(f"The shortest path to the vertex is: {vertex.min_distance}")  # Menampilkan total jarak

        actual_vertex = vertex  # Memulai dari vertex tujuan

        while actual_vertex is not None:  # Menelusuri predecessor hingga vertex awal
            print(actual_vertex.name, end=" ")  # Menampilkan nama vertex
            actual_vertex = actual_vertex.predecessor  # Berpindah ke predecessor


# Step 1 - Membuat seluruh vertex
nodeA = Node("A")  # Membuat vertex A
nodeB = Node("B")  # Membuat vertex B
nodeC = Node("C")  # Membuat vertex C
nodeD = Node("D")  # Membuat vertex D
nodeE = Node("E")  # Membuat vertex E
nodeF = Node("F")  # Membuat vertex F
nodeG = Node("G")  # Membuat vertex G
nodeH = Node("H")  # Membuat vertex H


# Step 2 - Membuat seluruh edge beserta bobotnya
nodeA.add_edge(6, nodeB)  # Menambahkan edge A → B dengan bobot 6
nodeA.add_edge(10, nodeC)  # Menambahkan edge A → C dengan bobot 10
nodeA.add_edge(9, nodeD)  # Menambahkan edge A → D dengan bobot 9

nodeB.add_edge(5, nodeD)  # Menambahkan edge B → D dengan bobot 5
nodeB.add_edge(16, nodeE)  # Menambahkan edge B → E dengan bobot 16
nodeB.add_edge(13, nodeF)  # Menambahkan edge B → F dengan bobot 13

nodeC.add_edge(6, nodeD)  # Menambahkan edge C → D dengan bobot 6
nodeC.add_edge(5, nodeH)  # Menambahkan edge C → H dengan bobot 5
nodeC.add_edge(21, nodeG)  # Menambahkan edge C → G dengan bobot 21

nodeD.add_edge(8, nodeF)  # Menambahkan edge D → F dengan bobot 8
nodeD.add_edge(7, nodeH)  # Menambahkan edge D → H dengan bobot 7

nodeE.add_edge(10, nodeG)  # Menambahkan edge E → G dengan bobot 10

nodeF.add_edge(4, nodeE)  # Menambahkan edge F → E dengan bobot 4
nodeF.add_edge(12, nodeG)  # Menambahkan edge F → G dengan bobot 12

nodeH.add_edge(2, nodeF)  # Menambahkan edge H → F dengan bobot 2
nodeH.add_edge(14, nodeG)  # Menambahkan edge H → G dengan bobot 14


algorithm = Dijkstra()  # Membuat objek algoritma Dijkstra
algorithm.calculate(nodeA)  # Menghitung jarak terpendek mulai dari vertex A
algorithm.get_shortest_path(nodeG)  # Menampilkan hasil jalur terpendek menuju vertex G

# Output:
# The shortest path to the vertex is: 29
# G H C A