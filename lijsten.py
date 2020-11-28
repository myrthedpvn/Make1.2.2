#!/usr/bin/env python

"""
 Info about our project comes here.
 """

# import


__author__ = "Myrthe Diepeveen"
__email__ = "myrthe.diepeveen@student.kdg.be"
__status__ = "Development"


def main():
 list = [['.', '.', '.', '.', '.', '.'],
             ['.', '2', '2', '.', '.', '.'],
             ['2', '2', '2', '2', '.', '.'],
             ['2', '2', '2', '2', '2', '.'],
             ['.', '2', '2', '2', '2', '2'],
             ['2', '2', '2', '2', '2', '.'],
             ['2', '2', '2', '2', '.', '.'],
             ['.', '2', '2', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.']]

 print("What do you want to print?")
 print("1. A heart")
 print("2. A Christmas three ")

 choice = input()

# Reverse to the right
 if choice == "1":
     for x in range(6):
         for y in range(9):
             if y < 8:
                print(list[y][+(x)], end="")                                 # Print out the matrix turned to the right
             else:
                print(list[y][x])

# Reverse to the left
 if choice == "2":
    for x in range(6):
         for y in range(9):
             if y < 8:
                 print(list[y][-(x + 1)], end="")                            # Print out the matrix turned to the left
             else:
                   print(list[y][x])

if __name__ == '__main__':                                                 # code to execute if called from command-line
    main()
