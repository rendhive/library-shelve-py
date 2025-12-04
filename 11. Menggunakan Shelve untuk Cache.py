import shelve

cache_data = {
    'user1': 'Tom',
    'user2': 'Sara'
}

with shelve.open('user_cache.db') as db:
    for key, value in cache_data.items():
        db[key] = value

print("Cache pengguna berhasil disimpan.")
# Fungsi: Menggunakan shelve sebagai cache untuk data yang diakses berulang kali.
# Kondisi: Ketika Anda ingin mempercepat akses data dengan menyimpan informasi yang sering digunakan.
