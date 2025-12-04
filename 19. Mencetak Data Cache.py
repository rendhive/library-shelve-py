import shelve

with shelve.open('user_cache.db') as db:
    for key in db:
        print(key, ":", db[key])
# Fungsi: Mencetak semua data dalam cache.
# Kondisi: Ketika Anda ingin melihat semua informasi yang telah disimpan.
