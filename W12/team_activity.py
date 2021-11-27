with open("books_and_chapters.txt") as scriptures_file:
    next(scriptures_file)

    largest_number_of_chapters = 0
    largest_book = ''

    for line in scriptures_file:
        clean_line = line.strip()
        line_list = clean_line.split(':')

        chapter = int(line_list[1])
        book = line_list[0]

        if chapter > largest_number_of_chapters:
            largest_number_of_chapters = chapter
            largest_book = book

        print(f'Scripture: {line_list[2]}, Book: {line_list[0]}, Chapters: {chapter}')
    
    print('')
    print(f'The largest number of chapters in the scriptures is {largest_number_of_chapters} and is found in {largest_book}')