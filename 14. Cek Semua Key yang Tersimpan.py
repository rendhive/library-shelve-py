import shelve

with shelve.open('user_cache.db') as db:
    keys = list(db.keys())
    print("Keys dalam cache:", keys)
# Fungsi: Menampilkan semua keys yang tersimpan di shelve.
# Kondisi: Ketika Anda ingin mengetahui semua data yang tersedia di dalam shelve.
