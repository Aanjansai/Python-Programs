""" To the Util Class add dayOfWeek static function that takes a date as input and prints the day of the week
    that date falls on. Your program should take three command-line arguments: m (month), d (day), and y (year).
    For m use 1 for January, 2 for February, and so forth. For output print 0 for Sunday, 1 for Monday, 2 for Tuesday,
    and so forth. Use the following formulas, for the Gregorian calendar (where / denotes integer division):
    y0 = y − (14 − m) / 12
    x = y0 + y0/4 − y0/100 + y0/400
    m0 = m + 12 × ((14 − m) / 12) − 2
    d0 = (d + x + 31m0 / 12) mod 7"""


month = int(input("enter the month \n"))
date = int(input("enter the date \n"))
year = int(input("enter the year \n"))
match = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
try:
    if (date <= 31) and (month <= 12):
        year1 = year - (14 - month)/12  # year value
        x = year1 + year1/4 - year1/100 + year1/400  #
        month1 = month + 12*((14 - month)/12) - 12
        day = int((date + x + 31*month1/12) % 7)
        print("day =", day)
        print(match[day])

except NameError as e:
    print(e)
