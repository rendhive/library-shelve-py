import shelve

# Menghapus data dari shelve
with shelve.open('my_shelve.db') as db:
    del db['key2']  # Menghapus data untuk key2

print("Data untuk key2 berhasil dihapus.")
# Fungsi: Menghapus objek dari shelve menggunakan key.
# Kondisi: Ketika Anda ingin menghapus data yang tidak lagi diperlukan.
