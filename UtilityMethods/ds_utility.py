# author:
"""A Sai Shree Anjan """
# task  : Data structures programs
# since : 14/01/2019
# to    : 21/01/2019

# importing packages


from UtilityMethods import Utility
import math


# -------------------------------------------------cash counter--------------------------------------------


class Queue:                                            # used to create Queue

    def __init__(self):  # constructor of Queue class

        self.list1 = []

    def is_empty(self):
        """ This method returns the list
        """
        return self.list1 == []

    def enqueue(self, list1):
        """ This method is used to insert elements
        """
        self.list1.insert(0, list1)

    def de_queue(self):
        """ This method removes the items
        """
        return self.list1.pop()

    def size(self):
        """ This method returns size of the list
        """
        return len(self.list1)


queue = Queue()

# -------------------------------------------------unordered list------------------------------------------


class Node:                                             # This class is used to create Node

    def __init__(self, data, next_node=None):

        """
            This is the constructor of Node class .
            data       :  user given value will be stored in this variable
            next_node  :  this variable keeps the address of next node
        """
        self.data = data

        self.next = next_node


class LinkedList:                                       # This class is used to create LinkedList

    head = None

    def __init__(self):

        # This is constructor of LinkedList class

        pass

    def is_empty(self):

        """
            This is used to know whether LinkedList is empty or not
            return  :  this will return True if LinkedList is empty else return False
        """
        if self.head is None:

            return True

        else:

            return False

    def append(self, data):

        """
            This method is used to append data given by user at the end of the LinkedList
            data   :  this value will be provided by user to append at the end of list
            return :  this method returns nothing.
        """

        node = Node(data)                               # creation of  object node

        if self.head is None:

            self.head = node                            # if head is null then assign new node to head

        else:

            traverse = self.head                        # Initialize the head to a traverse variable

            while traverse.next is not None:            # then traverse pointer till last node and

                traverse = traverse.next                # append new node at end

            traverse.next = node

    def display(self):

        """
            This method is used to display content of each node in the LinkedList
            return  :  nothing
        """

        traverse = self.head

        # condition to check list is empty or not
        if self.head is None:

            print("Linked List  is empty")              # if empty then print list is empty

            return

        while traverse.next is not None:

            print(traverse.data)                        # if not empty then traverse pointer till end

            traverse = traverse.next                    # and print node value one by one

        # print(traverse.data)

    def search_item(self, data):

        """
            This method is used to search data given by user.
            data        :  this is the data that user want to search in the list
            return      :  this will return true if data is found else return False
        """

        traverse = self.head

        if self.head is None:                           # execute if list empty

            return False

        while traverse.next is not None:                # execute till node is null

            if traverse.data == data:                   # checks for matching data

                return True

            traverse = traverse.next

        if traverse.data == data:

            return True                                 # for single node

        else:

            return False

    def remove(self, data):

        traverse = self.head

        if self.head is None:

            return None

        if traverse.data == data:

            self.head = traverse.next                   # for first node of linked list

            return

        while traverse.next is not None:

            temp = traverse.next

            if temp.data == data:                       # matching the temp data

                traverse.next = temp.next               # if data match with node then delete

                return

            traverse = traverse.next

    def size(self):

        """
            This method is used to calculate size of LinkedList.
            return  :  this will return the size of LinkedList
        """
        traverse = self.head

        count = 0

        while traverse.next is not None:
            traverse = traverse.next           # incrementing the pointer position from start to end for calculate size

            count += 1

        return count + 1

    def display_content(self):

        """
            This method is used to display content of Linked list.
            this method return each data in each node in LinkedList
            and this method is created so that it can be used in HashTable to display
            each data stored in HashTable data structure
            return  :  this will return each data in LinkedList
        """
        list1 = []

        traverse = self.head

        if self.head is None:

            return None                                    # if empty then return None

        while traverse.next is not None:

            list1.append(traverse.data)                    # append element in list till linked list not end

            traverse = traverse.next

        list1.append(traverse.data)

        return list1                                       # return Linked List

    def file_update(self, data):

        with open("jack.txt", "r+") as file:

            file.truncate(0)

        if self.search_item(data) is True:

            self.remove(data)

            file = open("jack.txt", "a+")

            linked_list_content = []

            linked_list_content = self.display_content()  # assign linked list to a list

            for i in linked_list_content:

                file.write(i + " ", )               # write data into file

            file.close()

            file = open("jack.txt", "r")

            for i in file:

                print(i)                            # print file

            file.close()
            
        else:

            self.append(data)                       # if data not found then append data into file

            file = open("jack.txt", "a+")

            linked_list_content = []

            linked_list_content = self.display_content()

            for i in linked_list_content:

                file.write(i + " ")                 # write file data into list

            file.close()

            file = open("jack.txt", "r")

            for i in file:

                print(i)                            # print list contents

            file.close()

# ----------------------------------------------stack--------------------------------------------------


class Stack:  # This class is used to create Stack

    def __init__(self):

        self.items = []                             # assigning list to the items

    def is_empty(self):
        """
            This method is used to check whether stack is empty or not
            returns  :  items list
        """

        return self.items == []

    def push(self, item):
        """
            This method add elements to the list
        """
        self.items.append(item)                     # append function is used to add items

    def pop(self):
        """
            This method is used remove the elements
            returns  :  Popped items list
        """
        return self.items.pop()                     # pop function is used to remove the elements

    def peek(self):
        """ This method is used to look the top of the stack
            returns  :  Top element of the stack
        """
        return self.items[len(self.items) - 1]

    def size(self):
        """
            This method is used for the size of items list
            returns  :  length of the items list
        """
        return len(self.items)                      # len method is used to find the length of the items list


# ----------------------------------------------Deque------------------------------------------

class Deque:
    """
        This is used to create deque
    """

    def __init__(self):

        self.list1 = []                                     # assigning list

    def is_empty(self):
        return self.list1 == []

    def add_rear(self, item):                               # add items to back of the list
        self.list1.append(item)

    def add_front(self, item):                              # add items in front of the list
        self.list1.insert(0, item)

    def remove_rear(self):                                  # remove items at the end of the list
        return self.list1.pop()

    def remove_front(self):                                 # remove items at the front of the list
        return self.list1.pop(0)

    def list1_size(self):                                   # returns the size of list
        return len(self.list1)

# -----------------------------------------------------Ordered list---------------------------------------


class OrderedList:
    """
        This is used to create OrderedList.
    """
    head = None                                           # Initialize head as none

    def __init__(self):
        """
            This is the constructor of OrderedList class
        """
        pass

    def append(self, data):
        """
            This method is used to put data in OrderedList in increasing order.
            data    :  dat will be provided by user
        """
        node = Node(data)                               # creation of node

        if self.head is None:

            self.head = node                            # if head is null then assign new node to head

        else:

            traverse = self.head                        # Initialize the head to a traverse variable

            while traverse.next is not None:            # else traverse pointer till last node and

                traverse = traverse.next                # append new node at end

            traverse.next = node

    def search_item(self, data):
        """
            This method is used to search data given by user.
            data    :  this is the data that user want to search in the list
            return  :  this will return true if data is found else return False
        """

        traverse = self.head

        # if self.head is None:  # execute, if list is empty

        # return False

        while traverse.next is not None:                # execute till node is null

            if traverse.data == data:                   # checks for matching data

                return True

            traverse = traverse.next

        if traverse.data == data:                       # checks for matching data

            return True

        else:

            return False

    def remove(self, data):

        traverse = self.head

        if self.head is None:

            return None

        if traverse.data == data:

            self.head = traverse.next                   # for first node of linked list

            return

        while traverse.next is not None:

            temp = traverse.next

            if temp.data == data:                       # matching the temp data

                traverse.next = temp.next               # if data match with node then delete

                return

            traverse = traverse.next

    def is_empty(self):
        """
            This is used to know whether OrderedList is empty or not
            return  :  this will return True if OrderedList is empty else return False
        """

        if self.head is None:

            return True

        else:

            return False

    def size(self):
        """
            This method is used to calculate size of OrderedList.
            return  :  this will return the size of L;inkedList
        """
        traverse = self.head

        count = 1

        while traverse.next is not None:

            traverse = traverse.next

            count += 1

        return count

    def display_content(self):
        """
            This method is used to display content of OrderedList.
            this method return each data in each node in LinkedList
            and this method i created so that i can use in HashTable to display
            each data stored in HashTable data structure
            return  :  this will return each data in OrderedList
        """
        list1 = []

        traverse = self.head

        if self.head is None:

            return

        while traverse.next is not None:

            list1.append(traverse.data)

            traverse = traverse.next

        list1.append(traverse.data)

        return list1

    def file_update(self, data):

        file = open("/home/admin1/Documents/ordered_list.txt", "r+")

        file.truncate(0)

        file.close()

        if self.search_item(data) is True:

            self.remove(data)

            file = open("/home/admin1/Documents/ordered_list.txt", "a")

            ordered_list_content = []

            ordered_list_content = self.display_content()   # assign data to list return by

            for i in ordered_list_content:                  # display()  method

                file.write(i + " ")                         # write data into file

            file.close()

            search_number = [int(i) for i in ordered_list_content]

            search_number.sort()                        # sort linked list

            print(search_number)                        # print linked list

        else:

            self.append(data)                           # if data not found in list then add it

            file = open("/home/admin1/Documents/ordered_list.txt", "a")

            ordered_list_content = []

            ordered_list_content = self.display_content()

            for i in ordered_list_content:

                file.write(i + " ")                     # write data into file

            file.close()

            search_number = [int(i) for i in ordered_list_content]

            search_number.sort()                        # sorting of element in ascending order

            print(search_number)                        # print data of linked list


# -------------------------------------------------hash table----------------------------------------------


class HashTable:
    """
        This HashTable class is used to create hashtable data structure.
    """

    def __init__(self):

        pass

    objects_list = []

    for i in range(11):

        objects_list.append(LinkedList())

    def hash_function(self, key):
        """
            This method is used to convert users key or data into index.
            this index is used to store user data in hashtable on index which is obtained  by that particular
            data from hash_function
            key     :  data given by user as a key
            return  :  this will return index for that data to store in hashtable
        """
        index = key % len(self.objects_list)

        return index

    def insert(self):
        """
            This method is used to read data from file and convert each data into
            integer format from string format.
        """

        file = open("/home/admin1/Documents/hashing.txt", "r")

        file_elements = file.readlines()

        string = file_elements[0]

        string_list = string.split()

        file_elements = []

        for i in range(0, len(string_list)):

            to_integer = int(string_list[i])

            file_elements.append(to_integer)

        for i in range(len(file_elements)):

            index = self.hash_function(file_elements[i])

            self.objects_list[index].append(file_elements[i])

    def search(self, data):
        """
            This method is used to search data which is given by user in hashtable data structure.
            data        :  data will be given bu user
            return      :  this will return true if data is found else return false
        """
        index = self.hash_function(data)

        return self.objects_list[index].search_item(data)

    def file_update(self, data):
        """
            This method is used to update file after any operation happened in hashtable
            data structure.
            data  :  this is the data that is to be removed or added to the file according to search result
        """
        result = self.search(data)

        if result is True:

            index = self.hash_function(data)

            self.objects_list[index].remove(data)

            self.display_content_hashtable()

        if result is False:

            index = self.hash_function(data)

            self.objects_list[index].append(data)

            self.display_content_hashtable()

    def display_content_hashtable(self):
        """
            This method is used to display content of HashTable data structure.
        """
        global lines

        file = open("/home/admin1/Documents/hashing.txt", "r+")

        file.truncate(0)

        file.close()

        for i in range(0, len(self.objects_list)):

            if self.objects_list[i].display_content() is not None:

                lines = []

                lines = self.objects_list[i].display_content()

                file = open("/home/admin1/Documents/hashing.txt", "a+")

                for j in lines:

                    file.write(str(j) + ' ')

        file.close()

        file = open("/home/admin1/Documents/hashing.txt", "r")

        for i in file:

            print(i)


hash_obj = HashTable()

# ----------------------------------------------Stack with linked list-----------------------------------------------


class StackLinked:
    """
        This is the Stack class to create Stack.
    """
    top = 0

    head = None

    def __init__(self):
        """
            This is the constructor of Stack class.
        """
        pass

    def push(self, data):
        """
            This method is used to insert data in stack.
            data  : data will given by user
        """

        node = Node(data)

        if self.head is None:

            self.head = node
        else:

            traverse = self.head

            while traverse.next is not None:
                traverse = traverse.next

            traverse.next = node

    def size(self):
        """
            This method is used to find the size of Stack.
            return  :  this will return the size of stack
        """
        traverse = self.head                                    # assign head to the traverse

        if self.head is None:

            return 0

        size = 1

        while traverse.next is not None:

            traverse = traverse.next

            size += 1

        return size

    def show(self):
        """
            This method is used to display content of stack.
        """
        traverse = self.head

        if self.top <= -1:

            print(" Stack Underflow")

            return

        if traverse is None:

            print("Stack is empty")

            return

        while traverse.next is not None:

            print(traverse.data)

            traverse = traverse.next

        print(traverse.data)

    def pop(self):
        """
            This method is used to delete last data which is inserted into the stack.
            actually stack follow the Last in First Out order Principle to pop the data from the stack
            return  :  this will return the data that will be removed
        """

        traverse = self.head

        if self.head is None:                         # if head is Null then return -1

            return -1

        if self.head.next is None:                    # if traverse is Null then return None

            self.head = None

            return traverse.data

        while traverse.next is not None:         # traverse till the end

            t1 = traverse.next                   # In t1, the data that  is placed in a traverse variable will be store

            if t1.next is None:

                traverse.next = None

                return t1.data

            traverse = traverse.next

    def peek(self):
        """
            This method is used to return the last inserted item in the stack.
            return  : return the last item inserted in the stack
        """
        traverse = self.head

        if self.head is None:

            return "empty stack"

        self.top = self.size() - 1

        for i in range(0, self.top):

            traverse = traverse.next

        return traverse.data

    def is_empty(self):
        """
            This method is used to know wheter stack is empty or not.
            return  :  this will return true if stack is empty else return False
        """

        if self.size() == 0:

            return True

        else:

            return False

    def balanced_parentheses(self, string):
        """
            This method is used to check whether expression is balanced or not.
            string  :  this is the expression which will be given by user
        """
        for i in string:

            if i == '(' or i == '[' or i == '{':
                stack.push(i)

            if ((stack.peek() == '(' and i == ')') or (stack.peek() == '[' and i == ']') or (
                    stack.peek() == '{' and i == '}')) and stack.size() > 0:
                stack.pop()
                continue

            if i == ')' or i == ']' or i == '}':
                stack.push(i)

        if stack.size() == 0:
            print("Balanced Parenthesis ")
        else:
            print("Parenthesis is not Balanced ")


stack = StackLinked()
stack1 = StackLinked()

# -------------------------------------------------Queue with linked list--------------------------------


class QueueLinked:
    """
        This Queue class is used to create Queue.
    """
    front = None

    rear = None

    def __init__(self):
        """
            This is the constructor of Queue class .
        """
        pass

    def enqueue(self, data):
        """
            This method is used to insert data in the Queue .
            data will be given by user which data to be inserted ,
            queue follows First in First Out Principle.
            data  :  data will be given by user
        """

        node = Node(data)

        if self.front is None and self.rear is None:  # If Null

            self.front = node                                   # Assign Nodes in front and a rear

            self.rear = node

        else:

            self.rear.next = node                               # assign node to rear of next

            self.rear = self.rear.next

    def show(self):
        """
            This method is used to display content of queue .
        """

        if self.front is None:

            print("Linked List  is empty")

            return

        while self.front.next is not None:

            print(self.front.data)

            self.front = self.front.next

        print(self.front.data)

    def dequeue(self):
        """
            This method is used to delete data from the Queue.
            data will deleted according to FIFO principle
            return  :  this will return the data that will be removed from the Queue
        """

        temp = self.front                           # keep data in a temporary variable for deletion

        self.front = self.front.next

        return temp.data

    def is_empty(self):
        """
            This method is used to know whether Queue is empty or not.
            return  :  this will return true if Queue is empty else return False
        """
        if self.front is None:

            return True

        else:

            return False

    def size(self):
        """
            This method is used to display content of queue.
        """

        size = 1

        traverse = self.front

        if self.front is None:

            return 0

        while traverse.next is not None:

            traverse = traverse.next

            size += 1

        return size


queue1 = QueueLinked()

# ---------------------------------------------------Deque with linked list--------------------------------


class DequeLinked:

    def __init__(self, front=None, rear=None):
        """
            This is the constructor of Deque class.
            front  :  this will always point to first node in the deque
            rear  :  this will always point to last node in the Deque
        """
        self.front = front

        self.rear = rear

    def add_front(self, data):
        """
            This method is used to insert data at front in Deque.
            data  :  data will be given by user that which data to be inserted in Deque
        """
        node = Node(data)

        if self.front is None and self.rear is None:

            self.front = node

            self.rear = node

        else:

            node.next = self.front

            self.front = node

    def add_rear(self, data):
        """
            This method is used to insert data at last in Deque.
            data  :  data will be given by user
        """

        node = Node(data)

        if self.front is None and self.rear is None:

            self.front = node

            self.rear = node

        else:

            self.rear.next = node
            self.rear = node

    def show(self):
        """
            This method is used to display content of deque.
        """

        if self.front is None:

            print("Queue  is empty")

            return

        while self.front.next is not None:

            print(self.front.data)

            self.front = self.front.next

        print(self.front.data)

    def remove_front(self):
        """
            This is used to remove data which is at front in deque.
            return  :  this will return the data which will be removed from the deque
        """

        if self.front.next is None:

            temp = self.front

            self.front = None

            return temp.data

        temp = self.front

        self.front = self.front.next

        return temp.data

    def remove_rear(self):
        """
            This is used to remove data which is at rear position in deque.
            return  :  this will return the data which will be removed from the deque
       """

        traverse = self.front

        if self.rear == self.front:

            self.rear = None

            self.front = None

            return traverse.data

        while traverse.next != self.rear:

            traverse = traverse.next

        rear_value = self.rear

        self.rear = traverse

        traverse.next = None

        return rear_value.data

    def is_empty(self):
        """
            This method is used to know whether Deque is empty or not.
            return  :  this will return True if Deque is empty or else  return False.
        """

        if self.front is None:

            return True

        else:

            return False

    def size(self):
        """
            This method is used to calculate size of Deque
            return  : this will return size of Deque
        """
        size = 1

        traverse = self.front

        if self.front is None:

            return 0

        while traverse.next is not None:

            traverse = traverse.next

            size += 1

        return size


deque1 = DequeLinked()

# ----------------------------------------------------Binary search tree---------------------------------


class BinarySearchTree:
    """
        This class is used to count the binary trees
    """

    def count(self, number_of_items_chosen):  # Method to count the number of binary trees

        n = number_of_items_chosen

        number = int((math.factorial(2 * n)) / (math.factorial(n + 1) * math.factorial(n)))

        print(number)

# ----------------------------------------------------logic for calender-----------------------------


class FunctionsOfOperations:
    """
        This class Methods is used to write logic of various programs.
    """

    def __init__(self):

        pass

    def anagram_stack(self):
        """
            This method is used to print prime anagram in reverse order.
        """
        for i in Utility.get_anagram_prime():   # get anagram numbers which are prime

            stack.push(i)                       # push numbers into stack

        for i in range(0, stack.size()):

            print(stack.pop())                  # print in reverse order

    def anagram_queue(self):
        """
            This method is used to print prime anagram using queue.
        """

        for i in Utility.get_anagram_prime():    # get anagram numbers which are prime

            queue1.enqueue(i)                    # add numbers into queue

        for i in range(0, queue1.size()):

            print(queue1.dequeue())              # print in reverse order

    def prime_number_2d_array(self):
        """
            This method is used to store prime number in matrix or 2d array
            and print in proper order.
        """

        prime_list = Utility.get_prime()         # get prime number

        row = 10

        column = 25

        limit = 100

        # create empty 2d array
        two_d_array = [[0 for loop in range(column)] for loop in range(row)]

        loop3 = 0
        for loop1 in range(row):

            for loop2 in range(column):

                if loop3 < len(prime_list):

                    if prime_list[loop3] <= limit:                      # prime number check with the limit

                        two_d_array[loop1][loop2] = prime_list[loop3]   # add number into array

                        loop3 += 1

            limit += 100                                        # increment limit by 100 for each iteration

        for loop4 in range(row):

            for loop5 in range(column):

                if two_d_array[loop4][loop5] != 0:

                    print(two_d_array[loop4][loop5], end=" ")   # display elements in 2d array format

            print()

    def anagram_2d_array(self):
        """
            This method is used to store prime anagram and prime number which are not anagram in matrix or 2d array.
            and print them accordingly
        """
        prime_list = Utility.get_prime()                        # get prime numbers

        anagram_list = Utility.get_anagram_prime()              # get anagram numbers which is prime also

        not_anagram = []
        row = 10
        column = 25

        two_d_array = [[0 for j in range(column)] for i in range(row)]

        k = 0

        index = 0

        for i in prime_list:

            if anagram_list.__contains__(i) is not True:        # if file not contains same element

                not_anagram.append(i)                           # append into not_anagram list

        for i in range(row):

            for j in range(column):

                if k < len(anagram_list):

                    two_d_array[i][j] = anagram_list[k]         # add element of anagram list into array

                    k += 1

                if k >= len(anagram_list) and index < len(not_anagram):

                    two_d_array[i][j] = not_anagram[index]      # add element of not_anagram list

                    k += 1                                      # into same array after anagram_list

                    index += 1

        for i in range(row):

            for j in range(column):

                if two_d_array[i][j] != 0:

                    print(two_d_array[i][j], end=" ")           # print 2d array

            print()

    def calender(self, month, year):
        """
            This method is used to print Calender of given month and year.
            month  :  month given by user
            year   :  year given by user
        """

        day = ['S', ' M', ' T', ' W', ' Th', 'F', ' S']

        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        values = 1

        d = 1

        m = month

        y = year

        y0 = y - (14 - m) // 12

        x = y0 + y0 // 4 - y0 // 100 + y0 // 400

        m0 = m + 12 * ((14 - m) // 12) - 2

        d0 = (d + x + 31 * m0 // 12) % 7

        print(d0)

        if Utility.leap_year(year):                   # check leap year

            days[1] = 29

        row = 6

        column = 7

        two_d_array = [[0 for j in range(column)] for i in range(row)]  # create empty 2d array

        print('Your Calender is\n')

        for i in range(0, 6 + 1):

            print(day[i], end=' ')                    # print day's for calender

        print()

        for i in range(row):

            for j in range(column):

                if values <= days[m - 1]:

                    if i == 0 and j < d0:             # while d0 is less than j

                        two_d_array[i][j] = ' '       # it will print blank space

                        continue

                    two_d_array[i][j] = values        # add days into calender

                    values += 1                       # increment counter

        for i in range(row):

            for j in range(column):

                if two_d_array[i][j] != 0:

                    x = two_d_array[i][j]            # l just() method returns the string

                    x1 = str(x).ljust(2)             # left justified in a string of length width.

                    print(x1, end=" ")

            print()

    def calender_queue(self, month, year):

        """
            This method is used to print calender of given month and year.
            In this method calender is created using queue
            month   : month given ser
            year    : year given by year

        """
        day = ['S', ' M', ' T', ' W', ' Th', 'F', ' S']

        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        values = 1

        d = 1

        m = month

        y = year

        y0 = y - (14 - m) // 12

        x = y0 + y0 // 4 - y0 // 100 + y0 // 400

        m0 = m + 12 * ((14 - m) // 12) - 2

        d0 = (d + x + 31 * m0 // 12) % 7

        if Utility.leap_year(year):              # check leap year

            days[1] = 29

        row = 6

        column = 7

        print('Your Calender is\n')

        for i in range(0, 6 + 1):

            print(day[i], end=' ')               # print day's for calender

        print()

        for i in range(row):

            for j in range(column):

                if values <= days[m - 1]:        # while d0 is less than j

                    if i == 0 and j < d0:        # it will print blank space

                        queue1.enqueue(' ')      # used enqueue() method of queue class

                        continue                 # to add space

                    queue1.enqueue(values)       # add element in queue

                    values += 1

        for i in range(row):

            for j in range(column):

                if queue1.size() > 0:

                    x = queue1.dequeue()         # remove element from queue and store it in x variable

                    x1 = str(x).ljust(2)         # using l just() method print formatted calender

                    print(x1, end=" ")

            print()

    def calender_stack(self, month, year):
        """
            This method is used to print calender of given month and year.
            In this method calender is created using stack
            month :  month given by user
            year  :  year given by user
        """
        day = ['S', ' M', ' T', ' W', ' Th', 'F', ' S']

        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        values = 1

        d = 1

        m = month

        y = year

        y0 = y - (14 - m) // 12

        x = y0 + y0 // 4 - y0 // 100 + y0 // 400

        m0 = m + 12 * ((14 - m) // 12) - 2

        d0 = (d + x + 31 * m0 // 12) % 7

        if Utility.leap_year(year):              # check leap year

            days[1] = 29

        row = 6

        column = 7

        print('Your Calender is Ready\n')

        for i in range(0, 6 + 1):

            print(day[i], end=' ')               # print day's for calender

        print()

        for i in range(row):

            for j in range(column):

                if values <= days[m - 1]:        # while d0 is less than j

                    if i == 0 and j < d0:        # it will print blank space

                        stack.push(' ')          # use push() to add blanks

                        continue

                    stack.push(values)           # add days using push() method

                    values += 1

        for i in range(stack.size()):

            stack_element = stack.pop()         # pop element from stack and store in local variable

            stack1.push(stack_element)          # again push element into stack for reverse

        for i in range(row):

            for j in range(column):

                if stack1.size() > 0:

                    x = stack1.pop()            # access element one by one using pop() method

                    x1 = str(x).ljust(2)        # l just() method to print in calender structure

                    print(x1, end=" ")

            print()
