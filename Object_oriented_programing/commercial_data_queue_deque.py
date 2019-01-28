# author: Sai Anjan
# task  : Object Oriented programming
# date  : 27/01/19

""" Further maintain DateTime of the transaction in a Queue implemented using Linked List to indicate
    when the transactions were done.
"""

from UtilityMethods.ds_utility import QueueLinked

import datetime
import json

queue = QueueLinked()                                              # queue object is created to implement queue


class Person:
    """ this class is created to add the stock by admin and user can buy and sell
        their shares by implementing queue data structure
    """
    try:
        def __init__(self):
            with open("stock.json", "r") as stock_jf:
                stock_jf = json.load(stock_jf)                      # load() convert file into python from json

            self.stock_jf = stock_jf
            with open("customers.json", "r") as person_json_value:
                person_json_value = json.load(person_json_value)
            self.person_json_value = person_json_value

        def view_shares(self):                   # Iterating through Stock Report by means of checking the length
            for share in range(len(self.stock_jf['Stock Report'])):
                print(share, self.stock_jf['Stock Report'][share])

        def check_validity(self):
            number = 0
            name = input("Enter Username")
            while number < len(self.person_json_value["Person"]):  # Creating the user for buying or selling a shares
                if self.person_json_value["Person"][number]["Name"] == name.title():  # Verifying the user
                    index = number
                    print(self.person_json_value["Person"][number])
                    print("....Login successful....")
                    c = int(input("1:Buy shares\n2:Sell shares:"))
                    if c == 1:
                        person_object.buy_share(index, name)
                    elif c == 2:
                        person_object.sell_share(index, name)

                    else:
                        print("wrong Input")

                number += 1

        def add_new_company(self):                               # Add a new company by adding a new through dictionary
            name = input("Enter company name\n")
            number = int(input("Enter Your Number of share\n"))
            price = int(input('Enter Your Price per share\n'))
            new_stock_dict = {"Stock Name": name,                 # created the dictionary for a new values

                              "Number of Share": number,

                              "Share Price": price}
            try:
                with open("stock.json", 'w') as stock_jf:                # Add a new file in a json through a key
                    self.stock_jf['Stock Report'].append(new_stock_dict)
                    stock_jf.write(json.dumps(self.stock_jf, indent=2))  # Writing a file through python to json

            except FileNotFoundError:
                print("File Not Found")

        def buy_share(self, index, name):
            for bu_share in range(len(self.stock_jf['Stock Report'])):
                print(bu_share, self.stock_jf['Stock Report'][bu_share])

            print('Enter Which Company Share you want to buy\n')
            choice = int(input("Enter choice in Int\n"))
            buy_share = int(input("Enter Number of Share You want to buy\n"))
            each_share_price = self.stock_jf['Stock Report'][choice]['Share Price']
            # Asking for a user to sell shares among indexing
            amount_pay = buy_share * each_share_price     # Calculating the share that are purchasing

            if self.person_json_value['Person'][index]["Total Balance"] > amount_pay:
                # Balance should be there while purchasing
                print("Total amount you have to pay for ", buy_share, " stocks : ", amount_pay)
                updated_stock_share = self.stock_jf["Stock Report"][choice]["Number of Share"] - buy_share
                # Updating the stock

                with open("stock.json", "w") as jf:  # Changing the updated stock in a file
                    self.stock_jf["Stock Report"][choice]["Number of Share"] = updated_stock_share
                    jf.write(json.dumps(self.stock_jf, indent=2))

                person_updated_balance = self.person_json_value['Person'][index]["Total Balance"] - amount_pay
                # Subtracting the new share amount from a balance
                print('Now Your Updated Balance is ', person_updated_balance)
                person_updated_share = self.person_json_value['Person'][index]['Number of Share'] + buy_share
                # Adding the new shares in a stock
                print('Now Your Updated Number of share is ', person_updated_share, "\n")
                dt = datetime.datetime.now()                             # to show the date

                queue.enqueue(      # adding stock details
                    ("Buy", self.stock_jf["Stock Report"][choice]["Stock Name"], "Number of shares : ", buy_share))

                with open("stack_transaction.txt", "a")as txt:          # open file to append data
                    txt.write(name + str(queue.show()) + str(dt) + "\n")
                print("stack show")
                queue.show()
                queue.enqueue("B")
                queue.show()

                with open("customers.json", "w") as jf:                  # open a file to write data
                    self.person_json_value['Person'][index]['Total Balance'] = person_updated_balance
                    self.person_json_value['Person'][index]['Number of Share'] = person_updated_share
                    jf.write(json.dumps(self.person_json_value))
            else:
                print("You Don't have enough money ")

        def sell_share(self, index, name):
            print('Enter choice to sell your share to particular company\n')

            # this loop is used to show the share of shock report
            for share in range(len(self.stock_jf['Stock Report'])):
                print(share, self.stock_jf['Stock Report'][share])

            choice = int(input("Enter choice in Int"))

            print('Enter Number of share you want to sell to', self.stock_jf['Stock Report'][choice]['Stock Name'],
                  'company', "\n")
            sell_share = int(input("Number of shares to sell "))
            updated_stock_share = self.stock_jf["Stock Report"][choice]["Number of Share"] + sell_share

            with open("stock.json", "w") as jf:     # open a file to dump data (python to json)
                self.stock_jf["Stock Report"][choice]["Number of Share"] = updated_stock_share
                jf.write(json.dumps(self.stock_jf, indent=2))
            # updated share of a person
            updated_person_share = self.person_json_value['Person'][index]["Number of Share"] - sell_share

            person_share_price = int(input("price for per share you want from company\n"))
            # user updated balance
            person_updated_balance = self.person_json_value['Person'][index][
                                         "Total Balance"] + person_share_price * sell_share

            print(' --> ', person_share_price * sell_share, '<--will be Added to your total balance')
            print('Now Your Updated Balance is ', person_updated_balance, "\n")

            print('Now Your Updated Number of share is ', updated_person_share, "\n")
            # add the stock report in the inventory
            queue.enqueue(("Sold", self.stock_jf["Stock Report"][choice]["Stock Name"],
                           "Number of shares :", sell_share))
            print("stack show")
            queue.show()
            queue.enqueue("S")
            queue.show()

            with open("customers.json", "w") as jf:                  # open file to write the user details
                self.person_json_value['Person'][index]['Total Balance'] = person_updated_balance
                self.person_json_value['Person'][index]['Number of Share'] = updated_person_share
                jf.write(json.dumps(self.person_json_value, indent=2))

    except Exception as e:
        print(e)


if __name__ == "__main__":
    while True:
        person_object = Person()                        # object for person class
        person_object.view_shares()
        print("\n")
        try:
            i = int(input("1: Admin Login or 2: User \n"))
            if i == 1:                                  # To enter as admin
                print("welcome Admin")
                j = int(input("1 to add Company :\n"))
                if j == 1:
                    person_object.add_new_company()
            elif i == 2:                                # To enter as user
                print("Welcome User")
                person_object.check_validity()

            else:
                print("Invalid choice")

        except ValueError:
            print("Invalid Value")
