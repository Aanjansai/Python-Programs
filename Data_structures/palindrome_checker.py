# author:
"""A Sai Shree Anjan """
# task  : Data structures programs

""" Desc -> A palindrome is a string that reads the same forward and backward, for example, radar, toot, and madam.
    We would like to construct an algorithm to input a string of characters and check whether it is a palindrome.
    I/P -> Take a String as an Input
    Logic -> The solution to this problem will use a deque to store the characters of the string.
    We will process the string from left to right and add each character to the rear of the deque.
    O/P -> True or False to Show if the String is Palindrome or not.
"""
from UtilityMethods.ds_utility import Deque


def check_palindrome():
    """
        This method checks whether the string is palindrome or not
    """

    input_string = [str(loop) for loop in input("enter the word to check whether it is palindrome or not \n")]

    deque = Deque()                                 # creating an object for deque

    equality = True                                 # assigning True to the equality

    for char_loop in input_string:

        deque.add_front(char_loop)                  # adding item at front of the list

    while deque.list1_size() > 1 and equality:

        first_char = deque.remove_rear()            # item removed at the end is assigned to the first character

        last_char = deque.remove_front()            # item removed at the front is assigned to the last character

        if first_char != last_char:                 # if both doesn't match then equality is false

            equality = False

    return equality


if __name__ == '__main__':

    print(check_palindrome())












