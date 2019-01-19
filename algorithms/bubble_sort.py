""" Desc -> Reads in integers prints them in sorted order using Bubble Sort
    I/P -> read in the list ints
    O/P -> Print the Sorted List """

from UtilityMethods import Utility
try:
    # calling bubble sort method
    Utility.integer_bubble_sort()
except Exception as e:
    print(e)


