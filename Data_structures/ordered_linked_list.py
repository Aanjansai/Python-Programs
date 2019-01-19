""" Desc -> Read .a List of Numbers from a file and arrange it ascending Order in a Linked List.
    Take user input for a number, if found then pop the number out of the list else
    insert the number in appropriate position
    I/P -> Read from file the list of Numbers and take user input for a new number
    Logic -> Create a Ordered Linked List having Numbers in ascending order.
    O/P -> The List of Numbers to a File.
"""

from UtilityMethods.ds_utility import OrderedList


def ordered_list():

    ordered_linked_list_obj = OrderedList()

    file = open("/home/admin1/Documents/ordered_list.txt", "r+")

    list1 = file.readlines()

    file_string = list1[0]

    list1 = file_string.split()

    for i in range(0, len(list1)):

        ordered_linked_list_obj.append(list1[i].strip())

    file.close()

    print(list1)

    try:

        data = input("Enter the data to search = ")

    except Exception as ex:

        print(ex)
        print('Enter data in string only')

    print(ordered_linked_list_obj.search_item(data))

    print("The updated file content are as follows")

    ordered_linked_list_obj.file_update(data)


if __name__ == '__main__':
    try:

        ordered_list()

    except Exception as e:

        print(e)
