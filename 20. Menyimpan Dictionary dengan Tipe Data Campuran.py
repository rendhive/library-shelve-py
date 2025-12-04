import shelve

mixed_data = {
    "integer": 10,
    "float": 3.14,
    "string": "Hello",
    "list": [1, 2, 3]
}

with shelve.open('mixed_type_data.db') as db:
    db['data'] = mixed_data

print("Data campuran berhasil disimpan.")
# Fungsi: Menyimpan berbagai tipe data ke dalam shelve dengan kunci.
# Kondisi: Ketika Anda perlu menyimpan koleksi tipe data yang berbeda dalam struktur sederhana.
