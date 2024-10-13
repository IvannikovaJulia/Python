# TODO Найдите количество книг, которое можно разместить на дискете

count_symbols_in_line = 25 # Количество символов в строке
count_line_in_page = 50 # Количество строк в странице
count_page_in_book = 100 # Количество страниц в книге
size_one_symbol = 4 # Вес одного символа, в байтах
size_disk_Mb = 1.44 # Объём дискеты, в Мб

size_disk_b = size_disk_Mb * (2 ** 20) # Объём дискеты, в байтах
total_symbols_in_book = count_symbols_in_line * count_line_in_page * count_page_in_book # Количество символов в книге
size_one_book = total_symbols_in_book * size_one_symbol # Объём одной книги, в байтах

count_book = size_disk_b // size_one_book # Количество книг на одной дискете

print("Количество книг, помещающихся на дискету:", round(count_book))
