"""  User Input and Replace String Template “Hello <<UserName>>, How are you?”
     I/P -> Take User Name as Input. Ensure UserName has min 3 char
     Logic -> Replace <<UserName>> with the proper name
     O/P -> Print the String with User Name"""


from UtilityMethods import Utility

statement = "hello username, how are you?"
# username should have minimum 3 characters
replaced_name = input("enter the name to be replaced \n")
Utility.replace(statement, replaced_name)


