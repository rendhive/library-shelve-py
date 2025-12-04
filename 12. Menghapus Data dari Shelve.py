import shelve

with shelve.open('user_cache.db') as db:
    del db['user2']  # Menghapus user2 dari cache

print("User2 berhasil dihapus dari cache.")
# Fungsi: Menghapus objek dari shelve berdasarkan key.
# Kondisi: Ketika Anda ingin membersihkan data yang tidak lagi diperlukan dalam cache.
