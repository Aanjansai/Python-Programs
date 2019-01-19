""" Modify the above program to store the Queue in two Stacks. Stack here is also implemented using
    Linked List and not from Collection Library
"""

from UtilityMethods.ds_utility import FunctionsOfOperations


def stack_calender():
    """
        This method is used as runner for calender_stack(month, year) method
        return  :  nothing
    """

    calender_stack_object = FunctionsOfOperations()  # creating an object for stack calender

    try:

        month = int(input('Enter Month = '))

    except ValueError:

        print("Enter integer only ")

    try:

        year = int(input('Enter Year = '))

    except ValueError:

        print("Enter integer only")

    calender_stack_object.calender_stack(month, year)


if __name__ == "__main__":

    try:

        stack_calender()

    except UnboundLocalError:

        print("enter valid data")
