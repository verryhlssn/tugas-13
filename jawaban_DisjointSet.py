# Disjoint Set in Python

class DisjointSet:  # Mendefinisikan class Disjoint Set
    def __init__(self, vertices):  # Constructor untuk membuat Disjoint Set
        self.vertices = vertices  # Menyimpan daftar vertex
        self.parent = {}  # Dictionary untuk menyimpan parent setiap vertex
        for v in vertices:  # Menelusuri seluruh vertex
            self.parent[v] = v  # Mengatur setiap vertex sebagai parent dirinya sendiri
        self.rank = dict.fromkeys(vertices, 0)  # Menginisialisasi rank setiap vertex dengan nilai 0
    
    def find(self, item):  # Fungsi untuk mencari root (parent utama) dari suatu vertex
        if self.parent[item] == item:  # Jika vertex adalah root
            return item  # Mengembalikan vertex tersebut
        else:  # Jika vertex belum merupakan root
            return self.find(self.parent[item])  # Mencari root secara rekursif
    
    def union(self, x, y):  # Fungsi untuk menggabungkan dua himpunan
        xroot = self.find(x)  # Mencari root dari vertex x
        yroot = self.find(y)  # Mencari root dari vertex y

        if self.rank[xroot] < self.rank[yroot]:  # Jika rank root x lebih kecil
            self.parent[xroot] = yroot  # Root x menjadi anak dari root y

        elif self.rank[xroot] > self.rank[yroot]:  # Jika rank root x lebih besar
            self.parent[yroot] = xroot  # Root y menjadi anak dari root x

        else:  # Jika kedua rank sama
            self.parent[yroot] = xroot  # Root y menjadi anak dari root x
            self.rank[xroot] += 1  # Menambah rank root x


vertices = ["A", "B", "C", "D", "E"]  # Membuat daftar vertex

ds = DisjointSet(vertices)  # Membuat objek Disjoint Set

ds.union("A", "B")  # Menggabungkan himpunan A dan B
ds.union("A", "C")  # Menggabungkan himpunan A dan C

print(ds.find("A"))  # Menampilkan root dari vertex A

# Output:
# A