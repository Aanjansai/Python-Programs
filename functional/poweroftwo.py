""" Desc -> This program takes a command-line argument N and prints a table of the powers of 2
    that are less than or equal to 2^N.
    I/P -> The Power Value N. Only works if 0 <= N < 31 since 2^31 overflows an int
    Logic -> repeat until i equals N."""


from UtilityMethods import Utility

try:
    number = int(input("enter the number\n"))
    Utility.power_of_two(number)
except Exception as e:
    print(e)
    print("enter integer value")

