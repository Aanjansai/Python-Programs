# author:
"""A Sai Shree Anjan """
# task  : Data structures programs

""" Create the Week Object having a list of WeekDay objects each storing the day (i.e S,M,T,W,Th,..)
    and the Date (1,2,3..) . The WeekDay objects are stored in a Queue implemented using Linked List.
    Further maintain also a Week Object in a Queue to finally display the Calendar
    Note - If a particular day has no date then the date is set as empty string and add it to queue.
"""

from UtilityMethods.ds_utility import FunctionsOfOperations


def queue_calender():
    """
        This method act as runner for calender_queue(month, year) method
        return  :  This method won't return anything
    """

    calender_stack_object = FunctionsOfOperations()             # creating an object for queue calender

    try:

        month = int(input('Enter the Month = '))

    except ValueError:

        print("Enter integer only ")

    try:

        year = int(input('Enter the year = '))

    except ValueError:

        print("Enter integer only")

    calender_stack_object.calender_queue(month, year)           # calling calender queue method


if __name__ == "__main__":

    try:

        queue_calender()                                        # calling queue calender method

    except UnboundLocalError:

        print("enter valid data")

