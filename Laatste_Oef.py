#!/usr/bin/env python

"""
 Kijken wat het grootste getal is.
 """

# import


__author__ = "Myrthe Diepeveen"
__email__ = "myrthe.diepeveen@student.kdg.be"
__status__ = "Development"


def main():
    a = int(input("Enter the first number:"))
    b = int(input("Enter the second number:"))
    c = int(input("Enter the third number:"))

    if a > b and a > c:
        print("Biggest number:", a)
    elif b > c:
        print("Biggest number:", b)
    else:
        print("Biggest number:", c)

if __name__ == '__main__':  # code to execute if called from command-line
    main()
