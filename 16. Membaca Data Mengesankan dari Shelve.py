import shelve

with shelve.open('complex_data.db') as db:
    data = db['dept']
    print("Detail Departemen:", data)
# Fungsi: Membaca data kompleks dari shelve.
# Kondisi: Ketika Anda ingin memulihkan informasi detail tentang struktur data.
