import shelve

with shelve.open('settings_cache.db') as db:
    settings = db['settings']
    print("Pengaturan yang dimuat:", settings)
# Fungsi: Memulihkan pengaturan dari cache.
# Kondisi: Ketika Anda ingin mengakses pengaturan aplikasi yang telah disimpan sebelumnya.
