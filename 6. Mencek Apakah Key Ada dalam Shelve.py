import shelve

with shelve.open('my_shelve.db') as db:
    exists = 'key1' in db
    print("Apakah key1 ada dalam shelve?", exists)
# Fungsi: Mencek apakah key tertentu ada dalam shelve.
# Kondisi: Ketika Anda ingin memverifikasi eksistensi data sebelum mengambilnya.
