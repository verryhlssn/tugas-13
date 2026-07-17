# Kruskal Algorithm  in Python
import jawaban_DisjointSet as dst  # Mengimpor class DisjointSet untuk Union-Find

class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Menyimpan jumlah vertex
        self.graph = []  # Menyimpan daftar edge
        self.nodes = []  # Menyimpan daftar node
        self.MST = []  # Menyimpan edge hasil MST

    def addEdge(self, s, d, w):
        self.graph.append([s, d, w])  # Menambahkan edge beserta bobotnya
    
    def addNode(self, value):
        self.nodes.append(value)  # Menambahkan node ke dalam daftar
    
    def printSolution(self,s,d,w):
        for s, d, w in self.MST:  # Menampilkan semua edge yang masuk MST
            print("%s - %s: %s" % (s, d, w))
    
    def kruskalAlgo(self):
        i, e = 0, 0  # Variabel indeks edge dan jumlah edge MST
        ds = dst.DisjointSet(self.nodes)  # Membuat struktur Disjoint Set
        self.graph = sorted(self.graph, key=lambda item: item[2])  # Mengurutkan edge berdasarkan bobot terkecil

        while e < self.V - 1:  # Mengulang sampai MST memiliki V-1 edge
            s, d, w = self.graph[i]  # Mengambil edge berikutnya
            i += 1  # Berpindah ke edge selanjutnya

            x = ds.find(s)  # Mencari parent dari node awal
            y = ds.find(d)  # Mencari parent dari node tujuan

            if x != y:  # Mengecek apakah edge tidak membentuk cycle
                e += 1  # Menambah jumlah edge MST
                self.MST.append([s,d,w])  # Menambahkan edge ke MST
                ds.union(x,y)  # Menggabungkan dua kelompok node

        self.printSolution(s,d,w)  # Menampilkan hasil MST

g = Graph(5)  # Membuat graf dengan 5 vertex

g.addNode("A")  # Menambahkan node A
g.addNode("B")  # Menambahkan node B
g.addNode("C")  # Menambahkan node C
g.addNode("D")  # Menambahkan node D
g.addNode("E")  # Menambahkan node E

g.addEdge("A", "B", 5)  # Menambahkan edge A-B dengan bobot 5
g.addEdge("A", "C", 13)  # Menambahkan edge A-C dengan bobot 13
g.addEdge("A", "E", 15)  # Menambahkan edge A-E dengan bobot 15
g.addEdge("B", "A", 5)  # Menambahkan edge B-A dengan bobot 5
g.addEdge("B", "C", 10)  # Menambahkan edge B-C dengan bobot 10
g.addEdge("B", "D", 8)  # Menambahkan edge B-D dengan bobot 8
g.addEdge("C", "A", 13)  # Menambahkan edge C-A dengan bobot 13
g.addEdge("C", "B", 10)  # Menambahkan edge C-B dengan bobot 10
g.addEdge("C", "E", 20)  # Menambahkan edge C-E dengan bobot 20
g.addEdge("C", "D", 6)  # Menambahkan edge C-D dengan bobot 6
g.addEdge("D", "B", 8)  # Menambahkan edge D-B dengan bobot 8
g.addEdge("D", "C", 6)  # Menambahkan edge D-C dengan bobot 6
g.addEdge("E", "A", 15)  # Menambahkan edge E-A dengan bobot 15
g.addEdge("E", "C", 20)  # Menambahkan edge E-C dengan bobot 20

g.kruskalAlgo()  # Menjalankan algoritma Kruskal

# Output:
# A
# A - B: 5
# C - D: 6
# B - D: 8
# A - E: 15