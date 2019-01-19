""" Desc -> Create Utility Class having following static methods
    binarySearch method for integer
    binarySearch method for String
    insertionSort method for integer
    insertionSort method for String
    bubbleSort method for integer
    bubbleSort method for String
    I/P -> Write main function to call the utility function
    Logic -> Check using Stopwatch the Elapsed Time for every method call
    O/P -> Output the Search and Sorted List. More importantly print elapsed time performance in descending order """


from UtilityMethods import Utility

number = int(input("enter the number to perform operations\n"))
if number == 1:
    Utility.string_insertion_sort()
elif number == 2:
    Utility.integer_insertion_sort()
elif number == 3:
    Utility.string_binary()
elif number == 4:
    Utility.integer_binary()
elif number == 5:
    Utility.integer_bubble_sort()
elif number == 6:
    Utility.string_bubble_sort()
else:
    print("invalid data ")


