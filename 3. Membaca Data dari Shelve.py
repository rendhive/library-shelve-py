import shelve

# Membuka shelve untuk membaca data
with shelve.open('my_shelve.db') as db:
    data1 = db['key1']
    print("Data untuk key1:", data1)
# Fungsi: Membaca data dari shelve menggunakan key.
# Kondisi: Ketika Anda ingin mengakses objek yang telah disimpan sebelumnya.
