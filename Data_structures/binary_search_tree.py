# author:
"""A Sai Shree Anjan """
# task  : Data structures programs

""" A binary tree is a tree which is characterized by any of the following properties:

    It can be empty (null).
    It can contain a root node which contain some value and two subtree, left subtree and right subtree,
    which are also binary tree.
    A binary tree is a binary search tree (BST) if all the non-empty nodes follows both two properties:

    If node has a left subtree, then all the values in its left subtree are smaller than the value of the current node.
    If node has a right subtree, then all the value in its right subtree are greater than the value of the current node.
    You are given N nodes, each having unique value ranging from [1, N], how many different binary search tree can be
    created using all of them.

    Input
    First line will contain an integer, T, number of test cases. Then T lines follow, where each line represent a test
    case.Each test case consists a single integer, N, where N is the number of nodes in the binary search tree.

    Output
    For each test case, find the number of different binary search trees that can be created using these nodes.
    Print the answer modulo (108+7).

    Constraints
    1 <= T <= 1000
    1 <= N <= 1000
"""


from UtilityMethods.ds_utility import BinarySearchTree


def binary_search_tree():
    """
        This method is used to count the number of binary trees formed
    """

    binary_tree = BinarySearchTree()                # creating an object binary tree

    try:

        number_of_nodes = int(input("Enter the Number of Nodes:\n"))

    except ValueError:

        print("Enter integer value")

    except TypeError:

        print("enter valid data")

    print("number of binary trees formed ")         # number of possible of tree formation

    binary_tree.count(number_of_nodes)              # calling count method


if __name__ == "__main__":

    try:

        binary_search_tree()                            # calling binary search tree method

    except UnboundLocalError:

        print("enter valid data")
