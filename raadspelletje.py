#!/usr/bin/env python

"""
Een raadspelletje waarbij je een woord moet raden dat in een lijst staat
 """

# import


__author__ = "Myrthe Diepeveen"
__email__ = "myrthe.diepeveen@student.kdg.be"
__status__ = "Development"


def main():
    list = ["flamingo", "hond", "stokstaartje", "beer", "leeuw"]
    a = 0
    while a < 3:
        guess = input(f"Guess the word.\n")
        for x in list:
            if guess == x:
                a+=3
                print("Jej, you won.")

        else:
            a+=1



if __name__ == '__main__':  # code to execute if called from command-line
    main()
