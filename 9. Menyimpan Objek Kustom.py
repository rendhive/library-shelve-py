import shelve

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 30)

with shelve.open('person_shelve.db') as db:
    db['person1'] = person

print("Objek 'Person' berhasil disimpan ke dalam shelve.")
# Fungsi: Menyimpan objek kustom ke dalam shelve.
# Kondisi: Ketika Anda memiliki objek kustom yang ingin Anda simpan untuk penggunaan di masa mendatang.
