import shelve

with shelve.open('mixed_data.db') as db:
    db['integer'] = 42
    db['float'] = 3.14
    db['string'] = "Hello World"
    db['list'] = [1, 2, 3, 4, 5]

print("Data campuran berhasil disimpan.")
# Fungsi: Menyimpan berbagai tipe objek ke dalam shelve.
# Kondisi: Ketika Anda ingin menyimpan berbagai tipe data dalam satu tempat.
