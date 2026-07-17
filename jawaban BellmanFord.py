class Graph:  # Mendefinisikan class Graph

    def __init__(self, vertices):  # Constructor untuk membuat graph
        self.V = vertices  # Menyimpan jumlah vertex
        self.graph = []  # Menyimpan daftar edge beserta bobotnya
        self.nodes = []  # Menyimpan daftar vertex

    def add_edge(self, s, d, w):  # Menambahkan edge beserta bobotnya
        self.graph.append([s, d, w])  # Menyimpan source, destination, dan weight ke dalam graph
    
    def addNode(self, value):  # Menambahkan vertex ke graph
        self.nodes.append(value)  # Memasukkan vertex ke daftar nodes

    def print_solution(self, dist):  # Menampilkan hasil jarak terpendek
        print("Vertex Distance from Source")  # Menampilkan judul output
        for key, value in dist.items():  # Menelusuri seluruh vertex dan jaraknya
            print('  ' + key, ' :    ', value)  # Menampilkan nama vertex dan jaraknya
    
    def bellmanFord(self, src):  # Fungsi Bellman-Ford
        dist = {i: float("Inf") for i in self.nodes}  # Mengatur seluruh jarak awal menjadi tak hingga
        dist[src] = 0  # Jarak dari source ke dirinya sendiri adalah 0

        for _ in range(self.V - 1):  # Melakukan relaksasi sebanyak V-1 kali
            for s, d, w in self.graph:  # Menelusuri seluruh edge
                if dist[s] != float("Inf") and dist[s] + w < dist[d]:  # Jika ditemukan jarak yang lebih pendek
                    dist[d] = dist[s] + w  # Memperbarui jarak terpendek
        
        for s, d, w in self.graph:  # Mengecek apakah masih ada relaksasi
            if dist[s] != float("Inf") and dist[s] + w < dist[d]:  # Jika masih bisa diperkecil
                print("Graph contains negative cycle")  # Menampilkan bahwa graph memiliki negative cycle
                return  # Menghentikan program
        
        self.print_solution(dist)  # Menampilkan hasil akhir jarak terpendek


g = Graph(5)  # Membuat objek graph dengan 5 vertex

g.addNode("A")  # Menambahkan vertex A
g.addNode("B")  # Menambahkan vertex B
g.addNode("C")  # Menambahkan vertex C
g.addNode("D")  # Menambahkan vertex D
g.addNode("E")  # Menambahkan vertex E

g.add_edge("A", "C", 6)  # Menambahkan edge A ke C dengan bobot 6
g.add_edge("A", "D", 6)  # Menambahkan edge A ke D dengan bobot 6
g.add_edge("B", "A", 3)  # Menambahkan edge B ke A dengan bobot 3
g.add_edge("C", "D", 1)  # Menambahkan edge C ke D dengan bobot 1
g.add_edge("D", "C", 2)  # Menambahkan edge D ke C dengan bobot 2
g.add_edge("D", "B", 1)  # Menambahkan edge D ke B dengan bobot 1
g.add_edge("E", "B", 4)  # Menambahkan edge E ke B dengan bobot 4
g.add_edge("E", "D", 2)  # Menambahkan edge E ke D dengan bobot 2

g.bellmanFord("E")  # Menjalankan algoritma Bellman-Ford dari vertex E

# Output:
# Vertex Distance from Source
#  A  :     6
#  B  :     3
#  C  :     4
#  D  :     2
#  E  :     0