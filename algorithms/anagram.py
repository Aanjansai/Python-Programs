""" Desc -> One string is an anagram of another if the second is simply a rearrangement of the first.
    For example, 'heart' and 'earth' are anagrams...
    I/P -> Take 2 Strings as Input such abcd and dcba and Check for Anagrams
    O/P -> The Two Strings are Anagram or not...."""

from UtilityMethods import Utility
try:
    string1 = input("enter the string1 data \n")
    string2 = input("enter the string2 data \n")

    Utility.anagram(string1, string2)
except Exception as e:
    print(e)
