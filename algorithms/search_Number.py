""" Desc -> takes a command-line argument N, asks you to think of a number between 0 and N-1, where N = 2^n, and always guesses the answer with n questions.
    I/P -> the Number N and then recursively ask true/false if the number is between a high and low value
    Logic -> Use Binary Search to find the number
    O/P -> Print the intermediary number and the final answer """


from UtilityMethods import Utility
import math
try:
    number = int(input("How much time you want me to ask the question:"))
    low = 0
    high = int(math.pow(2, number))
    print("Think a number between(", low, ")to(", high,")in range")
    result = Utility.search_number(low, high)
    print("The number is = ", result)
except Exception as e:
    print(e)
