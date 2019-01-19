""" Write a program Quadratic.java to find the roots of the equation a*x*x + b*x + c.
    Since the equation is x*x, hence there are 2 roots. The 2 roots of the equation can be found using a formula
    delta = b*b - 4*a*c
    Root 1 of x = (-b + sqrt(delta))/(2*a)
    Root 2 of x = (-b - sqrt(delta))/(2*a)
    Take a, b and c as input values to find the roots of x."""

from UtilityMethods import Utility
try:
    a = float(input("enter a value \n"))
    b = float(input("enter b value \n"))
    c = float(input("enter c value \n"))
    Utility.quadratic(a, b, c)

except Exception as e:
    print(e)
    print("enter the valid number ")

