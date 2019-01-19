""" Add the Prime Numbers that are Anagram in the Range of 0 - 1000 in a Queue using the Linked List
    and Print the Anagrams from the Queue. Note no Collection Library can be used.
"""

from UtilityMethods.ds_utility import FunctionsOfOperations


def anagram_in_stack():
    """
        This method act as runner for anagram_stack()  method.
        return: nothing
    """
    logic_object = FunctionsOfOperations()

    print("All prime numbers from 0 - 1000 in ANAGRAM\n")

    logic_object.anagram_stack()


if __name__ == "__main__":

    anagram_in_stack()
