""" work sheet"""

number = int(input("enter the number\n"))
r = int(input("enter the r value\n"))


def calc_factorial(x):

    if x == 1:
        return 1
    else:
        return x * calc_factorial(x-1)


nume = calc_factorial(number)
deno = calc_factorial(number - r)

result = nume/deno

print(result)
