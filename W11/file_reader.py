with open("books.txt") as book:
    for line in book:
        book = line.strip()
        print(book)

