""" Desc -> Create a Slot of 10 to store Chain of Numbers that belong to each Slot to efficiently
    search a number from a given set of number
    I/P -> read a set of numbers from a file and take user input to search a number
    Logic -> Firstly store the numbers in the Slot. Since there are 10 Numbers divide each number by 11 and
    the reminder put in the appropriate slot. Create a Chain for each Slot to avoid Collision.
    If a number searched is found then pop it or else push it.
    Use Map of Slot Numbers and Ordered LinkedList to solve the problem. In the Figure Below,
    you can see number 77/11 reminder is 0 hence sits in the 0 slot while 26/11 remainder is 4 hence sits in slot 4
    O/P -> Save the numbers in a file
"""

from UtilityMethods.ds_utility import HashTable


def hashing_number_run():
    """
        This method acts as runner
    """

    hash_object = HashTable()

    print('These are the Numbers in File')

    file = open("/home/admin1/Documents/hashing.txt", "r")

    print(file.readline())

    try:

        number = int(input('Now enter the Number you are looking for = '))

    except ValueError:

        print("Enter Number only")

    hash_object.insert()

    print(hash_object.search(number))

    print('Now Updated File Content are as Follows')

    hash_object.file_update(number)


if __name__ == "__main__":

    try:

        hashing_number_run()

    except UnboundLocalError:

        print("enter valid data ")
