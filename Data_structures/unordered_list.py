""" Desc -> Read the Text from a file, split it into words and arrange it as Linked List.
    Take a user input to search a Word in the List. If the Word is not found then add it to the list,
    and if it found then remove the word from the List. In the end save the list into a file
    I/P -> Read from file the list of Words and take user input to search a Text
    Logic -> Create a Unordered Linked List. The Basic Building Block is the Node Object.
    Each node object must hold at least two pieces of information. One ref to the data field and
    second the ref to the next node object.
    O/P -> The List of Words to a File.
"""


from UtilityMethods.ds_utility import *


def unordered_list():

    """ This method is used to read content of file.
        this method also append data into orderedList to perform operation on it
        this method also acts as runner for various method
        return:nothing
    """

    reference_variable = LinkedList()  # creating an object

    try:

        file = open("jack.txt", "r+")

        list1 = file.readlines()

        file_string = list1[0]

        list1 = file_string.split()

        for loop in range(0, len(list1)):

            reference_variable.append(list1[loop].strip())

        file.close()

        print("Data present in the file: \n")

        file = open("jack.txt", "r+")

        list1 = file.readlines()

        list1 = list1[0]

        print(list1)

        file.close()

    except FileNotFoundError:

        print("File Not Found")

    try:

        data = (input("Enter word you are looking for: \n"))

    except Exception as e:

        print(e)
        print("Enter string only")

    print(reference_variable.search_item(data))

    print("Updated file contains: \n")

    reference_variable.file_update(data)


if __name__ == '__main__':
    """ main """

print(unordered_list())
