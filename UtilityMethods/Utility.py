# author :
"""A Sai Shree Anjan """
# task : Functional and Algorithm programs
# since : 08/01/2019

# importing packages
import math
import cmath
import random
import time


# ----------------------------------replace prg-----------------------------------------------
# date : 08/01/2019
# method to replace the name


def replace(statement, replaced_name):
    # name should have minimum 3 characters
    if len(replaced_name) >= 3:

        # replace function is used to replace the strings

        print(statement.replace("username", replaced_name))

    else:

        print("enter the valid name to be replaced")

# -----------------------------------wind chill prg---------------------------------------------
# date : 08/01/2019
# method for wind chill


def windchill(temperature, wind_speed):

    if temperature > 50 and 120 > wind_speed > 3:

        print("it is not possible ")

    else:

        # formula for wind chill

        wind_chill = 35.74 + 0.0215*temperature + (0.4275*temperature - 35.75)*math.pow(wind_speed, 0.16)

        print("wind_chill = ", wind_chill)

# ----------------------------------------power of two-------------------------------------
# date : 08/01/2019
# method for power of two


def power_of_two(number):
    # number should be greater than or equal to zero and lesser than 31
    if (number >= 0) and (number < 31):
        result = 0
        # loop runs until the condition satisfies
        for i in range(1, number+1):

            result = 2 ** i  # 2 power i

        print("power of two ", result)
    else:
        print("invalid ")
# -----------------------------------------quadratic eq--------------------------------------
# method for quadratic with a, b and c arguments


def quadratic(a, b, c):
    # formula for delta
    delta = (b*b - 4*a*c)
    # root1 formula
    x1 = (-b + cmath.sqrt(delta)) / (2*a)
    # root2 formula
    x2 = (-b - cmath.sqrt(delta)) / (2*a)

    print("Root1 of x = ", x1)
    print("Root2 of x = ", x2)

# -------------------------------------------flip coin---------------------------------------
# method for flip coin


def flip_coin(number):
    tail = 0  # initialize tail to zero
    head = 0  # initialize head to zero
    # loop in range of number given
    for i in range(number):
        # random function is used to generate random numbers
        ran_num = random.randint(0, 1)
        # random number should be less than 0.5
        if ran_num < 0.5:
            # if condition is true then tail is incremented
            tail = tail + 1

        else:
            # if condition is false then head is incremented
            head = head + 1

    print("percentage of head ", (head / number) * 100, "%")
    print("percentage of tail ", (tail / number) * 100, "%")

# -------------------------------------------gambler---------------------------------------------
# method for gambler


def gambler_method(stake, goals, trails):
    # random function to generate random number
    ran_num = random.randint(0, 1)
    # initialize bet, win and loss to zero
    bet, win, loss = 0, 0, 0

    for i in range(trails):
        # assigning stake value to the cash
        cash = stake

        while (cash > 0) and (cash < goals):
            # while cash grater than zero and cash is less than goals increment bet
            bet = bet + 1
            if ran_num < 0.5:
                # if random number is less than 0.5 then increment the cash
                cash = cash + 1
            else:
                # if condition fails then decrement cash
                cash = cash - 1

        if cash == goals:
            # if cash equals goals then increment the wins
            win = win + 1
        else:
            # if cash is not equals to goals then increment loss
            loss = loss + 1

    print("win ", win)
    print("loss ", loss)
    print("win %", (win / trails) * 100)
    print("loss %", (loss / trails) * 100)

# -----------------------------------------------leap year--------------------------------------


def leap_year(year):

    if year > 999:

        if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
            print(year, "is a leap year ")
        else:
            print(year, "is not a leap year ")
    else:
        print("enter the valid year ")

# -----------------------------------------------harmonic----------------------------------------
# harmonic number method


def harmonic(number):
    # assign zero value to the result
    result = 0
    if number != 0:
        # if number is not equal to zero then perform the operations
        for i in range(1, number + 1):

            result = result + 1 / i   # 1/1 + 1/2 + 1/3 ---- 1/number

        print("Nth harmonic value = ", result)
    else:
        print("enter valid number ")
# -----------------------------------------------prime factor-----------------------------------
# method for prime factor


def prime_number(number):
    # i is in range of 2 to the number
    for i in range(2, number):
        # while reminder is equals to zero
        while number % i == 0:

            number = number/i  # perform division operation

            print(i)
    if number >= i:
        # if number is greater than zero print number
        print("number = ", number)

# ----------------------------------------------2D array-----------------------------------------
# method for 2D array


def tow_d_array(row, col, list1):
    # to insert values into the list
    for i in range(row):  # outer loop
        for j in range(col):  # inner loop

            val = input("enter the elements")
            # assigning values to the list
            list1[i][j] = val

    # to display the list in the form of 2D_array
    for i in range(row):  # outer loop
        for j in range(col):  # inner loop

            print(list1[i][j], end="   ")  # used for horizontal space

        print()  # for vertical space
        print()  # for vertical space

# ----------------------------------------------temperature-------------------------------------
# method for temperature(feh, cel)


def temp(cel):
    # formula for fahrenheit
    fahrenheit = 32 + ((9/5)*cel)
    # formula for celsius
    celsius = 5/9*(fahrenheit - 32)

    print("fahrenheit = ", fahrenheit, "\n")
    print("celsius = ", celsius)

# ---------------------------------------------prime numbers-----------------------------------
# method for prime numbers


def prime():
    # loop for the range of 0 to 1001
    for i in range(0, 1001):
        status = 0
        # loop for the range of 2 to i - 1
        for j in range(2, i - 1):
            # if reminder is equal to zero
            if i % j == 0:
                # assign status as 1
                status = 1
                break
        # if status is equal to zero
        if status == 0:
            # print i value
            print(i, end=" ")

# ----------------------------------------------bubble sort for integer-----------------------------------
# method for bubble sort for integer


def integer_bubble_sort():
    size = int(input("enter the size of list \n"))
    list1 = []
    for i in range(size):
        # adding values to the list
        val = int(input("enter the elements \n"))
        # append() is used to add values
        list1.append(val)

    for i in range(len(list1)):
        for j in range(len(list1) - 1):
            # if condition is true, swapping happens
            if list1[j] > list1[j + 1]:
                # swapping the elements in the list1
                list1[j], list1[j + 1] = list1[j + 1], list1[j]

    print(list1)

# ---------------------------------------------------string bubble sort------------------------
# method for string bubble sort


def string_bubble_sort():
    size = int(input("enter the size of list \n"))
    list1 = []
    for i in range(size):
        # adding values to the list
        val = input("enter the elements \n")
        # append() is used to add values
        list1.append(val)

    for i in range(len(list1)):
        for j in range(len(list1) - 1):
            # if condition is true, swapping happens
            if list1[j] > list1[j + 1]:
                # swapping the elements in the list1
                list1[j], list1[j + 1] = list1[j + 1], list1[j]


# -----------------------------------------------insertion sort for string----------------------------------------
# method for insertion sort for string


def string_insertion_sort():
    size = int(input("enter the size \n"))
    list1 = []
    # from range i to size
    for i in range(size):
        val = input("enter the word\n")
        # to insert the words in to the list
        list1.append(val)
    # from range 1 to the length of the list1
    for i in range(1, len(list1)):
        temp = list1[i]
        # j value is one less than i value
        j = i - 1
        while (j >= 0) and (temp <= list1[j]):
            # swapping vales of the list
            list1[j + 1] = list1[j]
            j = j - 1  # j value is 1 less than j
        list1[j + 1] = temp
    print(list1)

# ------------------------------------------------insertion sort for integer-------------------------
# method for integer insertion sort


def integer_insertion_sort():
    size = int(input("enter the size \n"))
    list1 = []
    # from range i to size
    for i in range(size):
        val = input("enter the NUMBER\n")
        # to insert the words in to the list
        list1.append(val)
    # from range 1 to the length of the list1
    for i in range(1, len(list1)):
        temp = list1[i]
        # j value is one less than i value
        j = i - 1
        while (j >= 0) and (temp <= list1[j]):
            # swapping vales of the list
            list1[j + 1] = list1[j]
            j = j - 1  # j value is 1 less than j
        list1[j + 1] = temp
    print(list1)

# --------------------------------------------------binary search for string-------------------------------------
# method for binary search for string


def string_binary():
    size = int(input("enter the size \n"))
    lis = []
    # adding values to the list
    for i in range(size):
        val = input("enter the elements\n")
        lis.append(val)
    # assign start as zero
    start = 0
    # end as length of list minus 1
    end = len(lis) - 1
    # element to be searched
    target = str(input("enter the element to search\n"))
    while start <= end:
        # formula to find the mid value
        middle = (start + end) // 2
        # mid value of the list
        midpoint = lis[middle]
        if midpoint > target:
            # if the mid value is greater than target then end equals mid -1
            end = middle - 1
        elif midpoint < target:
            # if the mid value is lesser than target then start equals mid +1
            start = middle + 1
        else:
            # if condition is not satisfied then value equals to middle
            result = middle
            break
        print("element is not present \n")

    print("target = ", lis[result])
    print("element is present ")

# ----------------------------------------------binary search for int-----------------------------
# method for binary search for integer


def integer_binary():
    size = int(input("enter the size \n"))
    lis = []
    # adding values to the list
    for i in range(size):
        val = int(input("enter the elements\n"))
        lis.append(val)
    # assign start as zero
    start = 0
    # end as length of list minus 1
    end = len(lis) - 1
    # element to be searched
    target = str(input("enter the element to search\n"))
    while start <= end:
        # formula to find the mid value
        middle = (start + end) // 2
        # mid value of the list
        midpoint = lis[middle]
        if midpoint > target:
            # if the mid value is greater than target then end equals mid -1
            end = middle - 1
        elif midpoint < target:
            # if the mid value is lesser than target then start equals mid +1
            start = middle + 1
        else:
            # if condition is not satisfied then value equals to middle
            result = middle
            break
        print("element is not present \n")

    print("target = ", lis[result])
    print("element is present ")

# ------------------------------------------------anagram--------------------------------------------
# anagram method


def anagram(string1, string2):
    # assign zero value to count
    count = 0
    # the value of string3 is the upper case of string1
    string3 = string1.upper()
    # the value of string4 is the upper case of string2
    string4 = string2.upper()
    if len(string1) == len(string2):
        # loop is of 0 to length of string3
        for loop1 in range(0, len(string3)):
            # loop is of 0 to length of string4
            for loop2 in range(0, len(string4)):

                if string3[loop1] == string4[loop2]:
                    # count increment
                    count = count + 1
                    break
        if len(string1) == count:  # value of string1 length is equals to count
            print(string1, "is a matching ", string2, "\n")
            print("its  an anagram \n")
        else:
            print("it's not an anagram \n")
    else:
        print("enter valid data ")

# --------------------------------------------------vending machine-----------------------------------
# method for vending machine


def vending_machine(rupee):
    # enter the rupee notes
    money = [1000, 500, 50, 10, 5, 2, 1]
    # initialize note as zero
    note = 0
    for i in range(0, len(money)):
        # // is used to generate integer value
        if rupee // money[i] > 0:
            print("number of notes in ", money[i], "is ", rupee // money[i])
            note = note + (rupee // money[i])
            rupee = rupee % money[i]  # reminder is generated and assigned to rupee
    print("number of notes are ", note)

# -------------------------------------------------to binary---------------------------------------------
# method for hexadecimal to binary


def to_binary(number):
    # assigned string value to the binary_num
    binary_num = ""
    for i in range(1, number):  # i in range of 1 to the number
        while number != 0:
            reminder = number % 2  # holds the reminder value
            binary_num = str(reminder) + binary_num  # adding string values
            number = number // 2  # holds quotient value
    print("hexadecimal to binary ", binary_num)

# -----------------------------------------------triplets----------------------------------------
# method for triplets


def triplets(size, list1):
    count = 0
    for loop1 in range(0, size):
        # it iterates from 0 to the size
        for loop2 in range(loop1 + 1, size):
            # iterates from one addition of loop1 to the size
            for loop3 in range(loop2 + 1, size):
                # from 1 addition of loop2 to the size
                if list1[loop1] + list1[loop2] + list1[loop3] == 0:  # addition of all the lists equals to zero
                    print(list1[loop1], list1[loop2], list1[loop3])
                    count = count + 1  # increment the count
    print("total number of triplets = ", count)

# -------------------------------------------------coupon number-----------------------------------
# method coupon number


def coupon(coupon_no):
    count = 0
    list1 = [int(i) for i in str(coupon_no)]
    print(list1)
    while len(list1) > 0:
        number = random.randint(0, 9)  # assigned random function to the number
        count += 1  # increment the count
        if number in list1:
            list1.remove(number)  # if number is present in the list then remove it
        print(list1)

    print("Total random numbers to generate coupon", count)

# -----------------------------------------------stop watch------------------------------------------
# methods for stop watch


start_timer = 0
stop_timer = 0
elapsed = 0


def start1():
    start1.start_timer = time.time()  # function to get system time
    print("Start Time is ", start1.start_timer)


def stop1():
    stop1.stop_timer = time.time()  # function to get system time
    print("Stop Time is", stop1.stop_timer)


def elapsed_time():
    elapsed1 = stop1.stop_timer - start1.start_timer  # elapsed time
    print("Elapsed Timer is", elapsed1)
    print("Converting Milliseconds to Seconds", (elapsed1 / 1000), "sec")

# -------------------------------------------------palindrome-------------------------------------
# method palindrome


def palindrome(number):
    list1 = []
    new_number = str(number)  # make number as a string
    a = new_number[::-1]  # slicing the list in reverse order [first, last, step]
    if a == new_number:
        list1.append(a)  # assigning values to the list
        print("Given Number is Palindrome", list1)
    else:
        print("Not the Palindrome Nos")

# --------------------------------------------------merge sort-------------------------------------
# method for merge sort


def merge_sort1(left_half, right_half, list1):
    i = 0
    j = 0
    k = 0
    while (i < len(left_half)) and (j < len(right_half)):
        if left_half[i] < right_half[j]:
            list1[k] = left_half[i]  # assign left half value to the list
            i = i + 1  # increment i value
        else:
            list1[k] = right_half[j]  # assign right half value to the list
            j = j + 1  # increment j value
        k = k + 1  # increment k value
    while i < len(left_half):
        list1[k] = left_half[i]  # assign left half to list when i is lesser than length of left half
        i = i + 1  # increment i
        k = k + 1  # increment k
    while j < len(right_half):
        list1[k] = right_half[j]  # assign right half to list when j is lesser than length of right half
        j = j + 1  # increment j
        k = k + 1  # increment k

    print(list1)


def merge_sort(list1):
    n = len(list1)
    left_half = []  # left half list
    right_half = []  # right half list
    if len(list1) < 2:
        return list1  # returns list1
    mid = len(list1) // 2  # mid value
    for i in range(mid):
        left_half.append(list1[i])  # adding values to the left half
    for i in range(mid, n):
        right_half.append(list1[i])  # adding values to the right half
    merge_sort(left_half)
    merge_sort(right_half)
    merge_sort1(left_half, right_half, list1)

# ------------------------------------------------- number generation-------------------------------
# method for number generation


def search_number(low, high):
    if high - low == 1:
        return low  # if the difference between high and low is 1 then return low value
    mid = low + (high - low) / 2  # mid value
    print("Is Your Number Less then", mid, "Press 1 for Yes and 0 for No")
    val = int(input())
    if val == 1:
        return search_number(low, mid)  # if val equals to 1 then return low and mid
    elif val == 0:
        return search_number(mid, high)  # if val equals to 0 then return mid and high
    else:
        print("Valid Input")

# ------------------------------------------------anagram and prime -------------------------------


def get_prime():
    list = []
    is_prime = True
    for i in range(1001):
        if i == 0 or i == 1:
            continue
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
        if is_prime:
            list.append(i)
    return list


def PrimeCheck(no1, no2):  # Pass the No. from start till end
    flag = 0
    l = []
    print("Prime No.s in a Range", no1, "And ", no2)
    for i in range(no1, no2 + 1):  # Iterate no1 to no2(i=no1;i<no2+1;i++)
        for j in range(2, i):  # Iterate (j=2;j<i;j++)
            if i % j == 0:  # No1 is divisible by 2, break
                flag = 0
                break
            else:
                flag = 1
        if flag == 1:  # If its not divisible then append in the list
            l.append(i)

    print(l)


def get_anagram_prime():
    x = get_prime()

    x = [str(i) for i in x]
    anagram1 = []
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            if sorted(x[i]) == sorted(x[j]):
                anagram1.append(x[i])
                anagram1.append(x[j])
    return anagram1





