""" Desc -> A program with cubic running time. Read in N integers and counts the
    number of triples that sum to exactly 0.
    I/P -> N number of integer, and N integer input array
    Logic -> Find distinct triples (i, j, k) such that a[i] + a[j] + a[k] = 0
    O/P -> One Output is number of distinct triplets as well as the second output is to print the distinct triplets."""

from UtilityMethods import Utility
try:
    size = int(input("enter the size of list\n"))
    list1 = []
    print("enter the values ")
    for i in range(0, size):
        val = int(input())
        list1.append(val)

    Utility.triplets(size, list1)
except Exception as e:
    print(e)
