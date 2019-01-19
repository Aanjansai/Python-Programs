""" Write a program Calendar.java that takes the month and year as command-line arguments and
    prints the Calendar of the month. Store the Calendar in an 2D Array, the first dimension the
    week of the month and the second dimension stores the day of the week. Print the result
"""


from UtilityMethods.ds_utility import FunctionsOfOperations


def calender():
    """
        This method act as runner for calender_queue(month, year)
        return  :  nothing
    """

    calender_object = FunctionsOfOperations()  # to create an object for calender

    try:

        month = int(input('Enter month: '))

    except ValueError:

        print("Enter integer only ")

    try:

        year = int(input("Enter Year: "))

    except ValueError:

        print("Enter integer only")

    calender_object.calender(month, year)


if __name__ == "__main__":

    try:

        calender()

    except UnboundLocalError:

        print("enter valid data")
