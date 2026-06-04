'''
Copyright 2026 - Program and Files by Lincoln C. Hanks

Program Specs

On each loop of this program the program will pick a random Cosmere book, and write that book,
plus its current chapter number, onto the output text file (incrementing the current chapter).

If a book is selected when its chapter number is equal to its max chapter number, that book will
be removed from the list.

When all books have been removed from the list, the program will end.
'''

import json
import random

TRUE_RANDOM = True

def parse_data(filename):
    '''Turns a JSON file into a dictionary and returns it.'''
    assert(type(filename) == type(""))
    assert(filename.endswith(".json"))

    with open(filename, "rt") as filehandle:
        book_data = json.loads(filehandle.read())
    
    return book_data

def select_random_first_chapter(books, book_data):
    '''Pick a random book from the JSON, then pop the first item off
    of that book's list and return it with the book name.

    If the book's length afterward is 0, remove that book from the book list.
    '''
    assert(type(books) == type([]))

    book = random.choice(books)
    book_chapters = book_data[book]

    assert(type(book_chapters) == type([]))
    next_chapter = book_chapters.pop(0)

    if len(book_chapters) == 0:
        books.remove(book)

    return book, next_chapter

def select_true_random_chapter(books, book_data):
    '''Instead of picking the first chapter from a random book, pick a
    random chapter from the random book and return that instead.'''

    book = random.choice(books)
    book_chapters = book_data[book]

    assert(type(book_chapters) == type([]))
    next_chapter = random.choice(book_chapters)
    book_chapters.remove(next_chapter)

    if len(book_chapters) == 0:
        books.remove(book)
    
    return book, next_chapter

def build_next_chapter_string(books, book_data):
    '''
    Call select_random_first_chapter() or select_true_random_chapter(),
    then format and return a string with the book title and chapter.
    '''
    assert(type(books) == type([]))
    assert(type(book_data) == type({}))

    if TRUE_RANDOM:
        next_data = select_true_random_chapter(books, book_data)
    else:
        next_data = select_random_first_chapter(books, book_data)
    
    next_book = next_data[0]
    next_chapter = next_data[1]

    return f"{next_book}: {next_chapter}\n"

def clear_file(filename):
    '''Write blank space to a file to clear its contents.'''
    with open(filename, "wt") as filehandle:
        filehandle.write("")

def write_chapter_to_file(filename, chapter_string):
    '''
    Write the specified chapter string to a new line of the
    specified file.
    '''
    assert(type(filename) == type(""))
    assert(filename.endswith(".txt"))
    assert(type(chapter_string) == type(""))

    with open(filename, "at") as filehandle:
        filehandle.write(chapter_string)

def main():
    book_data = parse_data("cosmere_books.json")
    assert(type(book_data) == type({}))
    books = book_data["books"]

    clear_file("output.txt")

    while len(books) > 0:
        write_chapter_to_file("output.txt", build_next_chapter_string(books, book_data))

main()