from collections import defaultdict  # Mengimpor defaultdict untuk membuat dictionary dengan nilai default berupa list


class Graph:  # Mendefinisikan class Graph
    def __init__(self):  # Constructor untuk membuat graph
        self.nodes = set()  # Menyimpan kumpulan vertex
        self.edges = defaultdict(list)  # Menyimpan adjacency list
        self.distances = {}  # Menyimpan bobot setiap edge
    
    def addNode(self, value):  # Menambahkan vertex ke dalam graph
        self.nodes.add(value)  # Memasukkan vertex ke dalam set
    
    def addEdge(self, fromNode, toNode, distance):  # Menambahkan edge beserta bobotnya
        self.edges[fromNode].append(toNode)  # Menambahkan vertex tujuan ke adjacency list
        self.distances[(fromNode, toNode)] = distance  # Menyimpan bobot edge


def dijkstra(graph, initial):  # Fungsi algoritma Dijkstra
    visited = {initial: 0}  # Menyimpan jarak terpendek dari vertex awal
    path = defaultdict(list)  # Menyimpan predecessor setiap vertex

    nodes = set(graph.nodes)  # Menyalin seluruh vertex ke dalam set

    while nodes:  # Melakukan perulangan selama masih ada vertex yang belum diproses

        minNode = None  # Menyimpan vertex dengan jarak minimum

        for node in nodes:  # Menelusuri seluruh vertex yang belum diproses

            if node in visited:  # Jika vertex sudah memiliki jarak

                if minNode is None:  # Jika belum ada vertex minimum
                    minNode = node  # Menjadikan vertex saat ini sebagai minimum

                elif visited[node] < visited[minNode]:  # Jika ditemukan jarak yang lebih kecil
                    minNode = node  # Memperbarui vertex minimum

        if minNode is None:  # Jika tidak ada vertex yang dapat dijangkau
            break  # Menghentikan proses

        nodes.remove(minNode)  # Menghapus vertex minimum dari daftar yang belum diproses

        currentWeight = visited[minNode]  # Mengambil jarak vertex minimum

        for edge in graph.edges[minNode]:  # Menelusuri seluruh tetangga vertex

            weight = currentWeight + graph.distances[(minNode, edge)]  # Menghitung jarak baru

            if edge not in visited or weight < visited[edge]:  # Jika ditemukan jalur yang lebih pendek

                visited[edge] = weight  # Memperbarui jarak terpendek

                path[edge].append(minNode)  # Menyimpan predecessor terbaru dari jalur terpendek
    
    return visited, path  # Mengembalikan jarak dan jalur


customGraph = Graph()  # Membuat objek graph

customGraph.addNode("A")  # Menambahkan vertex A
customGraph.addNode("B")  # Menambahkan vertex B
customGraph.addNode("C")  # Menambahkan vertex C
customGraph.addNode("D")  # Menambahkan vertex D
customGraph.addNode("E")  # Menambahkan vertex E
customGraph.addNode("F")  # Menambahkan vertex F
customGraph.addNode("G")  # Menambahkan vertex G

customGraph.addEdge("A", "B", 2)  # Menambahkan edge A ke B dengan bobot 2
customGraph.addEdge("A", "C", 5)  # Menambahkan edge A ke C dengan bobot 5
customGraph.addEdge("B", "C", 6)  # Menambahkan edge B ke C dengan bobot 6
customGraph.addEdge("B", "D", 1)  # Menambahkan edge B ke D dengan bobot 1
customGraph.addEdge("B", "E", 3)  # Menambahkan edge B ke E dengan bobot 3
customGraph.addEdge("C", "F", 8)  # Menambahkan edge C ke F dengan bobot 8
customGraph.addEdge("D", "E", 4)  # Menambahkan edge D ke E dengan bobot 4
customGraph.addEdge("E", "G", 9)  # Menambahkan edge E ke G dengan bobot 9
customGraph.addEdge("F", "G", 7)  # Menambahkan edge F ke G dengan bobot 7

print(dijkstra(customGraph, "A"))  # Menjalankan algoritma Dijkstra dari vertex A dan menampilkan hasil


# See change the distance from d to e to 1 and from b to e to 6.
# then to get to e from a ,
# shortest path should be a b d e
# but your code is giving a b e

# Output:
# ({'A': 0, 'B': 2, 'C': 5, 'D': 3, 'E': 6, 'F': 13, 'G': 15}, defaultdict(<class 'list'>, {'B': ['A'], 'C': ['A'], 'D': ['B'], 'E': ['B'], 'F': ['C'], 'G': ['E']}))