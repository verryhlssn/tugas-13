# Floyd Warshall Algorithm in python

INF = 9999  # Nilai untuk menyatakan jarak yang tidak terhubung

# Printing the solution
def printSolution(nV, distance):  # Fungsi untuk mencetak hasil matriks jarak
    for i in range(nV):  # Perulangan setiap baris matriks
        for j in range(nV):  # Perulangan setiap kolom matriks
            if(distance[i][j] == INF):  # Mengecek apakah jarak bernilai INF
                print("INF", end=" ")
            else:
                print(distance[i][j], end="  ")  # Mencetak nilai jarak
        print(" ")  # Pindah ke baris berikutnya


def floydWarshall(nV, G):  # Fungsi utama algoritma Floyd-Warshall
    distance = G  # Menyalin graf awal sebagai matriks jarak
    
    for k in range(nV):  # Memilih vertex perantara
        for i in range(nV):  # Memilih vertex awal
            for j in range(nV):  # Memilih vertex tujuan
                distance[i][j] = min(distance[i][j], distance[i][k]+distance[k][j])  # Mengambil jarak terkecil melalui vertex k
    
    printSolution(nV, distance)  # Menampilkan hasil akhir jarak terpendek


G = [[0, 8, INF,1],
    [INF, 0, 1,INF],
    [4, INF, 0,INF],
    [INF, 2, 9,1]
    ]  # Membuat matriks adjacency graf


floydWarshall(4, G)  # Menjalankan algoritma dengan jumlah vertex 4

# Output:
# 0  3  4  1   
# 5  0  1  6   
# 4  7  0  5   
# 7  2  3  1 