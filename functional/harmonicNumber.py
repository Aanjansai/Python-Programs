"""" Desc -> Prints the Nth harmonic number: 1/1 + 1/2 + ... + 1/N
     (http://users.encs.concordia.ca/~chvatal/notes/harmonic.html).
     I/P -> The Harmonic Value N. Ensure N != 0
     Logic -> compute 1/1 + 1/2 + 1/3 + ... + 1/N
     O/P -> Print the Nth Harmonic Value."""

from UtilityMethods import Utility

number = int(input("enter the number \n"))

Utility.harmonic(number)
