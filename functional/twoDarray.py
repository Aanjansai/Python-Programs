"""  Desc -> A library for reading in 2D arrays of integers, doubles, or booleans from standard input and
     printing them out to standard output.
     I/P -> M rows, N Cols, and M * N inputs for 2D Array. Use Java Scanner Class
     Logic -> create 2 dimensional array in memory to read in M rows and N cols
     O/P -> Print function to print 2 Dimensional Array. In Java use PrintWriter with
     OutputStreamWriter to print the output to the screen."""


from UtilityMethods import Utility


row = int(input("enter the row size "))
col = int(input("enter the col size "))
list1 = [[0 for i in range(col)] for j in range(row)]
Utility.tow_d_array(row, col, list1)
