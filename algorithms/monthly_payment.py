"""  Write a Util Static Function to calculate monthlyPayment that reads in three command-line
     arguments P, Y, and R and calculates the monthly payments you would have to make over Y years
     to pay off a P principal loan amount at R per cent interest compounded monthly."""


principal = float(input("enter the principal\n"))
year = int(input("enter the year\n"))
interest = float(input("enter the interest_rate\n"))
r = interest/(12*100)
n = 12*year
payment = (principal*r)/(1 - (1 + r)**(-n))
print(payment)
