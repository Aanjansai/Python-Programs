# author:
"""A Sai Shree Anjan """
# task  : Data structures programs

""" Desc -> Take an Arithmetic Expression such as (5+6)∗(7+8)/(4+3)(5+6)∗(7+8)/(4+3)
    where parentheses are used to order the performance of operations.
    Ensure parentheses must appear in a balanced fashion.
    I/P -> read in Arithmetic Expression such as (5+6)∗(7+8)/(4+3)(5+6)∗(7+8)/(4+3)
    Logic -> Write a Stack Class to push open parenthesis “(“ and pop closed parenthesis “)”.
    At the End of the Expression if the Stack is Empty then the Arithmetic Expression is Balanced.
    Stack Class Methods are Stack(), push(), pop(), peak(), isEmpty(), size()
    O/P -> True or False to Show Arithmetic Expression is balanced or not.
"""


from UtilityMethods.ds_utility import Stack


def is_balanced_parentheses():
    """ This method checks whether given string is balanced or not.
        symbol_string  :  user given string.
        returns  :  returns 'true' if balanced or 'false' if not balanced.
    """

    symbol_string = [str(loop) for loop in str(input("enter the parentheses to check \n"))]
    reference_variable = Stack()                   # object is created and given a reference as reference_variable
    balanced = True                                # assign boolean value 'True' to the balance variable
    index = 0

    while index < len(symbol_string) and balanced:  # both conditions are true then assign value od string to symbol
        symbol = symbol_string[index]
        if symbol == "(" and "[" and "{":           # if symbol are parentheses then perform push operation(adding)
            reference_variable.push(symbol)
        else:
            if reference_variable.is_empty():
                balanced = False                    # if stack is empty then it is false
            else:
                reference_variable.pop()            # if stack is not empty then perform pop operation(deleting)

        index = index + 1                           # increment index

    if balanced and reference_variable.is_empty():  # if stack is balanced and empty then return 'True' else 'False'
        return True
    else:
        return False


if __name__ == '__main__':                          # main method
    print(is_balanced_parentheses())                # calling in main method

