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
    queue = Queue()

    bank_cash = 1000

    no_of_people = int(input('Enter Number of People in the Queue:\n'))

    for i in range(0, no_of_people):

        queue.enqueue(i)

    for i in range(0, queue.size()):

        print("1. Deposit the amount\n2. Withdraw cash\n")

        choose = int(input("Enter the your choice\n"))

        if choose == 1:

            deposit_amount = float(input("Enter the amount to deposit \n"))

            bank_cash = bank_cash + deposit_amount

            queue.de_queue()

        if choose == 2:

            withdraw_cash = float(input("Enter the amount to withdraw\n"))

            if withdraw_cash <= bank_cash:

                bank_cash = bank_cash - withdraw_cash

                queue.de_queue()

            if withdraw_cash > bank_cash:

                print("Insufficient bank balance \n")

                print("1. Reenter the amount\n2. cancel the transaction\n")

                choice = int(input("Enter your choice\n"))

                if choice == 1:

                    if withdraw_cash <= bank_cash:

                        withdraw_cash = float(input("Enter the amount to withdraw\n"))

                        bank_cash = bank_cash - withdraw_cash

                        print("Withdraw cash = ", withdraw_cash, "\n")

                    queue.de_queue()

                if choice == 2:

                    print("Your transaction is cancelled\n")

                    print("Thank you\n")

                    queue.de_queue()

        if i < queue.size():

            print("Next person \n")

    print("Total cash in bank counter = ", bank_cash)


if __name__ == '__main__':
    """ main"""

    cash_counter()
