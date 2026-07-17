import math  # Mengimpor modul math untuk menggunakan fungsi floor()

def binarySearch(array, value):  # Fungsi Binary Search untuk mencari nilai pada array yang sudah terurut
    start = 0  # Menentukan indeks awal pencarian
    end = len(array) - 1  # Menentukan indeks akhir pencarian
    middle = math.floor((start + end) / 2)  # Menghitung indeks tengah

    while not (array[middle] == value) and start <= end:  # Perulangan selama nilai belum ditemukan dan area pencarian masih ada
        if value < array[middle]:  # Jika nilai yang dicari lebih kecil dari nilai tengah
            end = middle - 1  # Menggeser batas akhir ke kiri
        else:  # Jika nilai yang dicari lebih besar dari nilai tengah
            start = middle + 1  # Menggeser batas awal ke kanan

        middle = math.floor((start + end) / 2)  # Menghitung kembali indeks tengah
        # print(start, middle, end)  # Digunakan untuk melihat proses perpindahan indeks

    if array[middle] == value:  # Jika nilai berhasil ditemukan
        return middle  # Mengembalikan indeks nilai yang ditemukan
    else:  # Jika nilai tidak ditemukan
        return -1  # Mengembalikan -1 sebagai tanda nilai tidak ada


custArray = [8, 9, 12, 15, 17, 19, 20, 21, 28]  # Membuat array yang sudah terurut

print(binarySearch(custArray, 15))  # Mencari nilai 15 dan menampilkan indeksnya

# [8, 9, 12, 15, 17, 19, 20, 21, 28]
#   S              M               E
#   S  M      E
#         SM  E
#             SME

# Output:
# 3