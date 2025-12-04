import shelve

cache_data = {'config': {'theme': 'dark', 'language': 'en'}}

with shelve.open('settings_cache.db') as db:
    db['settings'] = cache_data['config']

print("Pengaturan berhasil disimpan dalam cache.")
# Fungsi: Menggunakan shelve untuk menyimpan pengaturan aplikasi dengan cepat.
# Kondisi: Ketika Anda memiliki pengaturan aplikasi yang perlu dimuat ketika aplikasi dimulai.
