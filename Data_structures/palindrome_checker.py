
from UtilityMethods.ds_utility import Deque


def check_palindrome():

    input_string = [str(loop) for loop in input("enter the word to check whether it is palindrome or not \n")]

    deque = Deque()

    equality = True

    for char_loop in input_string:

        deque.add_front(char_loop)

    while deque.list1_size() > 1 and equality:

        first_char = deque.remove_rear()

        last_char = deque.remove_front()

        if first_char != last_char:

            equality = False

    return equality


if __name__ == '__main__':

    print(check_palindrome())












