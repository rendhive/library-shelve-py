import shelve

with shelve.open('person_shelve.db') as db:
    person = db['person1']

print(f"Nama: {person.name}, Usia: {person.age}")
# Fungsi: Membaca objek kustom dari shelve.
# Kondisi: Ketika Anda ingin memulihkan objek kustom yang tersimpan sebelumnya.
