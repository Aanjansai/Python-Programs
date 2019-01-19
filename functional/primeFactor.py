""" Desc -> Computes the prime factorization of N using brute force.
    I/P -> Number to find the prime factors
    Logic -> Traverse till i*i <= N instead of i <= N for efficiency.
    O/P -> Print the prime factors of number N."""


from UtilityMethods import Utility
try:
    number = int(input("enter the number \n"))
    Utility.prime_number(number)
except NameError as e:
    print(e)

