""" I/P -> The number of times to Flip Coin. Ensure it is positive integer.
    Logic -> Use Random Function to get value between 0 and 1. If < 0.5 then tails or heads
    O/P -> Percentage of Head vs Tails"""

from UtilityMethods import Utility

try:
    number = int(input("enter the number of time the coin to be flipped \n"))
    Utility.flip_coin(number)  # calling the flip coin method
except ValueError:
    print("enter the integer value")


