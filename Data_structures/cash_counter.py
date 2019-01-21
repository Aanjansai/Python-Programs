# author:
"""A Sai Shree Anjan """
# task  : Data structures programs

""" Desc -> Create a Program which creates Banking Cash Counter where people come in to deposit Cash and withdraw Cash.
    Have an input panel to add people to Queue to either deposit or withdraw money and dequeue the people.
    Maintain the Cash Balance.
    I/P -> Panel to add People to Queue to Deposit or Withdraw Money and dequeue
    Logic -> Write a Queue Class to enqueue and dequeue people to either deposit or withdraw money and maintain
    the cash balance
    O/P -> True or False to Show Arithmetic Expression is balanced or not.
"""


from UtilityMethods.ds_utility import Queue


def cash_counter():
    """ This function is used to display the 'bank cash' by performing all the methods
        return  :  nothing
    """
    queue = Queue()                                                    # creating queue object

    bank_cash = 1000

    try:

        no_of_people = int(input('Enter Number of People in the Queue:\n'))

    except ValueError:

        print("enter data in number")

    for i in range(0, no_of_people):

        queue.enqueue(i)                                               # calling enqueue method to add candidate
    try:
        for i in range(0, queue.size()):

            print("1. Deposit the amount\n2. Withdraw cash\n")

            choose = int(input("Enter the your choice\n"))

            if choose == 1:

                deposit_amount = float(input("Enter the amount to deposit \n"))

                bank_cash = bank_cash + deposit_amount                 # increment bank cash for deposit

                queue.de_queue()                                       # calling de_queue method to remove the candidate

            if choose == 2:

                withdraw_cash = float(input("Enter the amount to withdraw\n"))

                if withdraw_cash <= bank_cash:

                    bank_cash = bank_cash - withdraw_cash                  # decrement bank cash for withdraw

                    queue.de_queue()                                       # calling de_queue to remove the candidate

                if withdraw_cash > bank_cash:

                    print("Insufficient bank balance \n")

                    print("1. Reenter the amount\n2. cancel the transaction\n")

                    choice = int(input("Enter your choice\n"))

                    if choice == 1:                                        # asking for reenter the amount

                        if withdraw_cash <= bank_cash:

                            withdraw_cash = float(input("Enter the amount to withdraw\n"))

                            bank_cash = bank_cash - withdraw_cash

                            print("Withdraw cash = ", withdraw_cash, "\n")

                        queue.de_queue()                                   # candidate will leave after the withdraw

                    if choice == 2:                                        # transaction is cancelled

                        print("Your transaction is cancelled\n")

                        print("Thank you\n")

                        queue.de_queue()                                   # candidate will leave after the cancellation

            if i < queue.size():                                           # calling next person

                print("Next person \n")

        print("Total cash in bank counter = ", bank_cash)

    except ValueError:
        print("enter valid data")


if __name__ == '__main__':
    """ main"""

    cash_counter()                                                     # calling cash counter method
