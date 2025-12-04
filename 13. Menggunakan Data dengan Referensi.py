import shelve

with shelve.open('ref_data.db') as db:
    obj = {'key': 'value'}
    db['ref1'] = obj
    db['ref2'] = obj  # Referensi ke objek yang sama

print("Data dengan referensi berhasil disimpan.")
# Fungsi: Menyimpan objek dengan referensi dalam satu shelve.
# Kondisi: Ketika Anda perlu menyimpan objek yang sama di beberapa tempat.
