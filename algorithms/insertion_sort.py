""" Desc -> Reads in strings from standard input and prints them in sorted order.
    Uses insertion sort.
    I/P -> read in the list words
    Logic -> Use Insertion Sort to sort the words in the String array
    O/P -> Print the Sorted List """


from UtilityMethods import Utility
try:
    Utility.string_insertion_sort()
except Exception as e:
    print(e)




