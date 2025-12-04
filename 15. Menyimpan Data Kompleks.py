import shelve

complex_data = {
    'employees': [
        {'name': 'Tom', 'age': 28},
        {'name': 'Sara', 'age': 32}
    ],
    'department': 'Sales'
}

with shelve.open('complex_data.db') as db:
    db['dept'] = complex_data

print("Data kompleks berhasil disimpan ke dalam shelve.")
# Fungsi: Menyimpan struktur data yang kompleks ke dalam shelve.
# Kondisi: Ketika Anda ingin menyimpan data yang memiliki banyak detail.
