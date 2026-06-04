# random-cosmere-reading-order
This program has three modes: First Chapter Random, Random Equal Weight, and True Random (still working on the names).
## First Chapter Random
Every version of the program operates on the same loop: pick a random chapter from the Cosmere, write it to the end of the output file, and repeat. The difference lies in how each version picks the random chapter.
First Chapter Random will pick a random book from the Cosmere, then it will spit out the first available chapter of that book. For instance, if it rolls Oathbringer, it will output the Oathbringer Prologue. The second time it rolls Oathbringer, it will output Oathbringer Chapter 1, and so on. This is best if you want a (somewhat) linear reading order to your Cosmere reread. Each time a book is rolled, you'll pick up exactly where you left off.
The only "flaw" with reading this version is that while the beginning of the reading order is varied, the ending highly favors the longer books in the Cosmere (cough, cough, Stormlight). You'll get novellas and short books finished early on in the reading order, but near the end you'll mostly be focusing on Stormlight Archive. That's not a bad thing per se, but if you want more randomness, try the other two versions of this program.
### How to Use
To use this version, open random_cosmere.py and change the TRUE_RANDOM variable to False. Then run the program and check output.txt for the reading order.
## Random Equal Weight
This version is similar to First Chapter Random with one key difference. Whenever a book is rolled, instead of outputting the next chapter in that book, this program will output a random chapter from that book. This means that the order will be much more random, as you will end up reading chapter 58 of a book long before chapter 23.
This version has more randomness and therefore variety than First Chapter Random, although that does mean it loses the linear nature that FCR had. This version is still not perfectly random, though, because every book gets an equal weight, meaning that, once again, novellas will show up early in the order and nowhere else, while the end will still be generally dominated by Wind and Truth (although much less than FCR). If you want *true* randomness, where any chapter can appear at any place, try True Random.
### How to Use
To use Random Equal Weight, open random_cosmere.py (the same one from FCR) and change the TRUE_RANDOM variable to True. Then run the program and check output.txt.
## True Random
As the name suggests, this version is truly random. Any chapter can appear at any point in the reading order. This is because, rather than randomly selecting from a list of books, this program randomly selects from every chapter in the Cosmere. You can find that full list in cosmere_chapters.json. Don't ask me how long it took to write that file. Just know that I did it completely without AI.
### How to Use
All you need to do is run true_random_cosmere.py. No configuration. Then check output.txt.
## Copyright and Info
Copyright 2026, Program and Files by Lincoln C. Hanks.
No Generative AI was used in designing, developing, or testing this program, or in creating any files used by it.