""" Write a program with Static Functions to do Merge Sort of list of Strings.
    Logic -> To Merge Sort an array, we divide it into two halves, sort the two halves independently,
    and then merge the results to sort the full array. To sort a[lo, hi), we use the following recursive strategy:
    Base case: If the subarray length is 0 or 1, it is already sorted.
    Reduction step: Otherwise, compute mid = lo + (hi - lo) / 2, recursively sort the two subarrays a[lo, mid)
    and a[mid, hi), and merge them to produce a sorted result."""

from UtilityMethods import Utility

m = int(input("Enter the number of Elements"))
print("Enter the elements")
arr = [(input()) for i in range(m)]
Utility.merge_sort(arr)

