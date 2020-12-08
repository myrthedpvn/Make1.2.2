#!/usr/bin/env python

"""
 een script waarbij je om input vraagt achter een willekeurig woord
 en waarbij het script het woord achterstevoren weergeeft.

 """

# import


__author__ = "Myrthe Diepeveen"
__email__ = "myrthe.diepeveen@student.kdg.be"
__status__ = "Development"


def main():
    word = input("Give me a random word\n")
    print(word[::-1])                                                       #To print the word backwords

if __name__ == '__main__':  # code to execute if called from command-line
    main()
