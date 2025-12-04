import shelve

with shelve.open('mixed_data.db') as db:
    for key in db:
        print(key, ":", db[key])
# Fungsi: Membaca semua data dari shelve.
# Kondisi: Ketika Anda ingin melihat semua data yang disimpan di dalam shelve.
