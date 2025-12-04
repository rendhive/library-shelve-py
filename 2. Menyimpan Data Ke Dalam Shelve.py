import shelve

# Membuka shelve untuk menulis data
with shelve.open('my_shelve.db') as db:
    db['key1'] = {'name': 'Alice', 'age': 30}
    db['key2'] = {'name': 'Bob', 'age': 25}

print("Data berhasil disimpan ke dalam shelve.")
# Fungsi: Menyimpan objek Python ke dalam shelve menggunakan key.
# Kondisi: Ketika Anda ingin menyimpan objek dengan akses yang cepat dan mudah.
