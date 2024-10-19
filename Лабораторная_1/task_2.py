# TODO Найдите количество книг, которое можно разместить на дискете

inf_volume=1.44
pages=100
lines=50
symbols=25
bytes=4

books_volume=pages*lines*symbols*bytes # объем книги
inf_volume_byt=inf_volume * 1024 ** 2
books=inf_volume_byt // books_volume

books = int(books)
print("Количество книг, помещающихся на дискету:", books)
