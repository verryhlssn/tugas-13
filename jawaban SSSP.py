class Graph:  # Membuat class Graph
    def __init__(self, gdict=None):  # Constructor untuk membuat objek Graph
        if gdict is None:  # Mengecek apakah graph dictionary kosong
            gdict = {}  # Membuat dictionary kosong jika tidak ada data
        self.gdict = gdict  # Menyimpan graph dictionary
    
    def bfs(self, start, end):  # Fungsi BFS untuk mencari jalur dari start ke end
        queue = []  # Membuat queue kosong
        queue.append([start])  # Menambahkan node awal ke queue
        while queue:  # Melakukan perulangan selama queue tidak kosong
            path = queue.pop(0)  # Mengambil jalur pertama dari queue
            node = path[-1]  # Mengambil node terakhir dari jalur
            if node == end:  # Mengecek apakah node tujuan ditemukan
                return path  # Mengembalikan jalur yang ditemukan
            for adjacent in self.gdict.get(node, []):  # Mengecek semua node tetangga
                new_path = list(path)  # Membuat salinan jalur saat ini
                new_path.append(adjacent)  # Menambahkan node tetangga ke jalur baru
                queue.append(new_path)  # Menambahkan jalur baru ke queue


customDict = { "a" : ["b", "c"],  # Membuat adjacency list graph
               "b" : ["d", "g"],
               "c" : ["d", "e"],
               "d" : ["f"],
               "e" : ["f"],
               "g" : ["f"]
            }

g = Graph(customDict)  # Membuat objek Graph

print(g.bfs("a", "f"))  # Menampilkan jalur BFS dari a menuju f

# Output:
# ['a', 'b', 'd', 'f']