# Prims Algorithm  in Python
import sys  # Mengimpor library sys untuk menggunakan nilai maksimum

class Graph:  # Membuat class Graph
    def __init__(self, vertexNum, edges, nodes):  # Constructor untuk membuat objek Graph
        self.edges = edges  # Menyimpan matriks edge graf
        self.nodes = nodes  # Menyimpan daftar node graf
        self.vertexNum = vertexNum  # Menyimpan jumlah vertex
        self.MST = []  # Menyimpan hasil Minimum Spanning Tree
    
    def printSolution(self):  # Fungsi untuk menampilkan hasil MST
        print("Edge : Weight")  # Menampilkan judul output
        for s, d, w in self.MST:  # Melakukan perulangan pada setiap edge MST
            print("%s -> %s: %s" % (s, d, w))  # Menampilkan edge dan bobotnya
    
    def primsAlgo(self):  # Fungsi untuk menjalankan algoritma Prim
        visited = [0]*self.vertexNum  # Membuat array untuk menyimpan vertex yang sudah dikunjungi
        edgeNum=0  # Menghitung jumlah edge pada MST
        visited[0]=True  # Menjadikan vertex pertama sebagai vertex awal
        
        while edgeNum<self.vertexNum-1:  # Mengulang sampai jumlah edge MST sesuai jumlah vertex
            min = sys.maxsize  # Menentukan nilai awal bobot minimum
            
            for i in range(self.vertexNum):  # Mengecek setiap vertex
                if visited[i]:  # Mengecek vertex yang sudah dikunjungi
                    for j in range(self.vertexNum):  # Mengecek semua vertex tujuan
                        if ((not visited[j]) and self.edges[i][j]):  # Mengecek edge yang belum dikunjungi dan memiliki bobot
                            if min > self.edges[i][j]:  # Membandingkan bobot untuk mencari yang terkecil
                                min = self.edges[i][j]  # Menyimpan bobot minimum
                                s = i  # Menyimpan vertex asal
                                d = j  # Menyimpan vertex tujuan
            self.MST.append([self.nodes[s], self.nodes[d], self.edges[s][d]])  # Menambahkan edge terpilih ke MST
            visited[d] = True  # Menandai vertex tujuan sudah dikunjungi
            edgeNum += 1  # Menambah jumlah edge MST
        self.printSolution()  # Menampilkan hasil MST



edges = [[0, 10, 20, 0, 0],  # Membuat matriks bobot graf
		[10, 0, 30, 5, 0],
		[20, 30, 0, 15, 6],
		[0, 5, 15, 0, 8],
		[0, 0, 6, 8, 0]]

nodes = ["A","B","C","D","E"]  # Membuat daftar nama vertex

g = Graph(5, edges, nodes)  # Membuat objek Graph dengan 5 vertex

g.primsAlgo()  # Menjalankan algoritma Prim

# Output:
# Edge : Weight
# A -> B: 10
# B -> D: 5
# D -> E: 8
# E -> C: 6