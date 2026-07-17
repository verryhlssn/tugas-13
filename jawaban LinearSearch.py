# Searching algorithms - Linear Search

def linearSearch(array, value):  # Fungsi untuk mencari nilai dalam array
    for i in range(len(array)):  # Melakukan perulangan pada setiap index array
        if array[i] == value:  # Mengecek apakah nilai pada index sama dengan nilai yang dicari
            return i  # Mengembalikan index jika nilai ditemukan
    return -1  # Mengembalikan -1 jika nilai tidak ditemukan


print(linearSearch([20,40,30,50,90], 90))  # Menampilkan hasil pencarian index nilai 90

# Output:
# 4