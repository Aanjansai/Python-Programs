""" Write a static function sqrt  to compute the square root of a nonnegative number c given in
    the input using Newton's method:
     - initialize t = c
     - replace t with the average of c/t and t
     - repeat until desired accuracy reached using condition Math.abs(t - c/t) > epsilon*t where epsilon = 1e-15;"""


try:
    c = int(input("enter the c value\n"))
    t = c
    epsilon1 = 1e-15
    while abs(t - c/t) > epsilon1*t:
        t = (c/t + t)/2
    print("avg =", t)
except ValueError as a:
    print(a)
    print("enter integer value ")
