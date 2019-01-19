""" Desc -> Given N distinct Coupon Numbers, how many random numbers do you need to generate distinct coupon number?
    This program simulates this random process.
    I/P -> N Distinct Coupon Number
    Logic -> repeatedly choose a random number and check whether it's a new one.
    O/P -> total random number needed to have all distinct numbers.
    Functions => Write Class Static Functions to generate random number and to process distinct coupons. """


from UtilityMethods import Utility
try:
    coupon_number = int(input("Enter the Coupon number\n"))
    Utility.coupon(coupon_number)
except ValueError as v:
    print(v)
    print("enter integer data ")

