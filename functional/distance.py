""" Write a program Distance.java that takes two integer command-line arguments x and y and
    prints the Euclidean distance
    from the point (x, y) to the origin (0, 0).
    The formulae to calculate distance = Sq(x*x + y*y). Use Math.power function"""

import cmath
try:
    x = float(input("enter the x value \n"))
    y = float(input("enter the y value \n"))
    # sum of products, where origin values are (0,0)
    sum_of_product = (x*x + y*y)
    distance = cmath.sqrt(sum_of_product)
    print("distance = ", distance)

except Exception as e:
    print(e)
    print("enter valid number")
