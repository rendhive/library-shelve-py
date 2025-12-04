import shelve

# Memperbarui data yang ada
with shelve.open('my_shelve.db') as db:
    db['key1']['age'] = 31  # Mengupdate usia Alice

print("Data berhasil diperbarui.")
# Fungsi: Memperbarui objek yang sudah ada dalam shelve.
# Kondisi: Ketika Anda ingin merubah nilai dari objek yang disimpan sebelumnya.
