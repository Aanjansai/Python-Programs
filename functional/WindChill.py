""" Write a program WindChill.java that takes two double command-line arguments t and v and prints the wind chill.
    Use Math.pow(a, b) to compute ab.
    Given the temperature t (in Fahrenheit) and the wind speed v (in miles per hour),
    the National Weather Service defines the effective temperature (the wind chill) to be:
    w=35.74 + 0.0215t + (0.4275t - 35.75)* v^0.16
    Note: the formula is not valid if t is larger than 50 in absolute value or if v is larger than 120 or less than 3
   (you may assume that the values you get are in that range)."""


from UtilityMethods import Utility

try:
        temperature = float(input("enter the temperature \n"))
        wind_speed = float(input("enter the speed of the wind \n"))
        Utility.windchill(temperature, wind_speed)

except Exception as e:
        print(e)
        print("do not enter character value")

