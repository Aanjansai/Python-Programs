"""  I/P -> Year, ensure it is a 4 digit number.
     Logic -> Determine if it is a Leap Year.
     O/P -> Print the year is a Leap Year or not."""

from UtilityMethods import Utility
try:
    year = int(input("enter the year \n"))
    Utility.leap_year(year)
except Exception as e:
    print(e)
    print("enter the integer")
