# author:
"""A Sai Shree Anjan """
# task  : Data structures programs

""" Add the Prime Numbers that are Anagram in the Range of 0 - 1000 in a Stack using the Linked List and
    Print the Anagrams in the Reverse Order. Note no Collection Library can be used.
"""


from UtilityMethods.ds_utility import FunctionsOfOperations


def anagram_in_queue():
    """
        This method act as runner for anagram_queue() method.
    """
    anagram_object = FunctionsOfOperations()

    print("All prime numbers between 0 - 1000 that are ANAGRAM \n")

    anagram_object.anagram_queue()                  # calling the anagram queue function to display the numbers 0-1000


if __name__ == "__main__":

    anagram_in_queue()                              # calling in main method

