""" Desc -> Read .a List of Numbers from a file and arrange it ascending Order in a Linked List.
    Take user input for a number, if found then pop the number out of the list else
    insert the number in appropriate position
    I/P -> Read from file the list of Numbers and take user input for a new number
    Logic -> Create a Ordered Linked List having Numbers in ascending order.
    O/P -> The List of Numbers to a File.
"""

from UtilityMethods.ds_utility import OrderedList


def ordered_list():
    """
        This method is used to read content of file.
        This method displays the ordered list.
    """

    ordered_linked_list_obj = OrderedList()                  # creating an object to the ordered list

    file = open("/home/admin1/Documents/ordered_list.txt", "r+")

    list1 = file.readlines()                                 # returns a list containing the lines

    file_string = list1[0]                                   # list's 1st element to the string file

    list1 = file_string.split()                              # returns a list of strings after breaking the given string

    for i in range(0, len(list1)):

        ordered_linked_list_obj.append(list1[i].strip())     # appending the elements

    file.close()

    print(list1)

    try:

        data = input("Enter the data to search = ")

    except ValueError:

        print('Enter data in string only')

    print(ordered_linked_list_obj.search_item(data))

    print("The updated file content are as follows")

    ordered_linked_list_obj.file_update(data)               # display the updated file


if __name__ == '__main__':

    try:

        ordered_list()                                     # calling the ordered lists

    except UnboundLocalError:

        print("enter the valid data")
