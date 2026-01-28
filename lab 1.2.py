BYTES_ONE_CHAR = 4  # размер одного символа в байтах

pages = 100
lines = 50
chars = 25

total_chars = pages * lines * chars
total_bytes = total_chars * BYTES_ONE_CHAR

disk_size = 1.44 * 1024 * 1024  # размер в байтах
num_books = int(disk_size // total_bytes)

print("Количество книг, помещающихся на дискету:", num_books)
