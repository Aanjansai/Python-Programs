""" Extend the Prime Number Program and store only the numbers in that range that are Anagrams.
    For e.g. 17 and 71 are both Prime and Anagrams in the 0 to 1000 range.
    Further store in a 2D Array the numbers that are Anagram and numbers that are not Anagram
"""

from UtilityMethods.ds_utility import FunctionsOfOperations


def two_d_anagram_runner():
    """
        This method is act as runner for anagram_2d_array() method .
        return: this will return nothing
    """

    logic_obj = FunctionsOfOperations()

    print("prime numbers that are ANAGRAM \n")

    logic_obj.anagram_2d_array()       # function calls


if __name__ == "__main__":

    two_d_anagram_runner()
