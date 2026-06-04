'''
Copyright 2026 - Program and Files by Lincoln C. Hanks
'''

import json
import random

def parse_data(filename):
    '''Turn a JSON file, formatted as a list, into a list.'''
    assert(type(filename) == type(""))
    assert(filename.endswith(".json"))

    with open(filename, "rt") as filehandle:
        book_data = json.loads(filehandle.read())
    
    chapters = book_data["chapters"]
    assert(type(chapters) == type([]))
    return chapters

def select_random_chapter(chapters):
    '''Pick a random chapter from the list, remove it from the list,
    and return it.
    '''
    assert(type(chapters) == type([]))
    assert(len(chapters) > 0)

    next_chapter = random.choice(chapters)
    chapters.remove(next_chapter)

    assert(type(next_chapter) == type(""))
    return next_chapter

def append_chapter_to_file(filename, chapter):
    '''Append the chapter name to the end of the file filename.txt.
    Return nothing.
    '''
    assert(type(filename) == type(""))
    assert(filename.endswith(".txt"))
    assert(type(chapter) == type(""))

    with open(filename, "at") as filehandle:
        filehandle.write(f"{chapter}\n")

def clear_file(filename):
    '''Clears a specified file.'''
    with open(filename, "wt") as filehandle:
        filehandle.write("")

def main():
    chapters = parse_data("cosmere_chapters.json")

    clear_file("output.txt")

    while len(chapters) > 0:
        append_chapter_to_file("output.txt", select_random_chapter(chapters))


main()