# author: Sai Anjan
# task  : Object Oriented programming
# date  : 26/01/19


""" Commercial data processing - StockAccount.java implements a data type that might be used by a
    financial institution to keep track of customer information. The StockAccount class implements following methods
    The StockAccount class also maintains a list of CompanyShares object which has Stock Symbol and
    Number of Shares as well as DateTime of the transaction. When buy or sell is initiated StockAccount
    checks if CompanyShares are available and accordingly update or create an Object.
"""

import json


class Person:
    """ this class is created to add the stock by the admin
        and user can buy sell their share in the market
    """
    try:
        def __init__(self):
            with open("stock.json", "r") as jf:
                stock_jf = json.load(jf)                    # load() convert file into python from json

            self.stock_jf = stock_jf
            with open("customers.json", "r") as person_json_value:
                person_json_value = json.load(person_json_value)
            self.person_json_value = person_json_value

        def show_shares(self):                        # this is to show the shares
            for number_of_shares in range(len(
                    self.stock_jf['Stock Report'])):  # Iterating through Stock Report by means of checking the length
                print(number_of_shares, self.stock_jf['Stock Report'][number_of_shares])

        def check_validity(self):                      # this method is to verify the user
            number = 0
            name = input("Enter Username\n")
            while number < len(self.person_json_value["Person"]):  # Creating the user for buying or selling a shares
                if self.person_json_value["Person"][number]["Name"] == name.title():  # Verifying the user
                    index = number
                    print(self.person_json_value["Person"][number])
                    print("....Login successful....")
                    c = int(input("1:Buy shares\n2:Sell shares:"))
                    if c == 1:
                        person_object.buy_share(index)
                    elif c == 2:
                        person_object.sell_share(index)

                    else:
                        print("wrong Input")
                number += 1

        def add_new_company(self):                              # Add a new company by adding a new through dictionary
            name = input("Enter company name\n")
            number = int(input("Enter Your Number of share\n"))
            price = int(input('Enter Your Price per share\n'))
            new_stock_dict = {"Stock Name": name,                           # created the dictionary for a new values

                              "Number of Share": number,

                              "Share Price": price}

            with open('stock.json', 'w') as stock_jf:                       # Add a new file in a json through a key
                self.stock_jf['Stock Report'].append(new_stock_dict)

                stock_jf.write(json.dumps(self.stock_jf, indent=2))         # Writing a file through python to json

        def buy_share(self, index):
            for stock_report in range(len(self.stock_jf['Stock Report'])):
                # Iterating through stock report for buying a shares
                print(stock_report, self.stock_jf['Stock Report'][stock_report])

            print('Enter Which Company Share you want to buy\n')
            choice = int(input("Enter choice in Int\n"))
            buy_share = int(input("Enter Number of Share You want to buy\n"))
            each_share_price = self.stock_jf['Stock Report'][choice]['Share Price']
            # Asking for a user to sell shares among indexing
            amount_pay = buy_share * each_share_price                       # Calculating the share that are purchasing

            if self.person_json_value['Person'][index]["Total Balance"] > amount_pay:
                # Balance should be there while purchasing

                print("Total amount you have to pay for ", buy_share, " stocks : ", amount_pay, "\n")
                updated_stock_share = self.stock_jf["Stock Report"][choice]["Number of Share"] - buy_share
                # Updating the stock

                with open("stock.json", "w") as jf:                    # Changing the updated stock in a file
                    self.stock_jf["Stock Report"][choice]["Number of Share"] = updated_stock_share
                    jf.write(json.dumps(self.stock_jf, indent=2))

                person_updated_balance = self.person_json_value['Person'][index]["Total Balance"] - amount_pay
                # Subtracting the new share amount from a balance
                print('Now Your Updated Balance is ', person_updated_balance)
                person_updated_share = self.person_json_value['Person'][index]['Number of Share'] + buy_share
                # Adding the new shares in a stock
                print('Now Your Updated Number of share is ', person_updated_share, "\n")

                with open("customers.json", "w") as jf:                         # Write to a file using a dump method
                    self.person_json_value['Person'][index]['Total Balance'] = person_updated_balance
                    self.person_json_value['Person'][index]['Number of Share'] = person_updated_share
                    jf.write(json.dumps(self.person_json_value))
            else:
                print("You Don't have enough money \n")

        def sell_share(self, index):                            # this method is to sell the shares
            print('Enter choice to sell your share to particular company\n')
            for i in range(len(self.stock_jf['Stock Report'])):
                print(i, self.stock_jf['Stock Report'][i])

            choice = int(input("Enter choice \n"))

            print('Enter Number of share you want to sell to', self.stock_jf['Stock Report'][choice]['Stock Name'],
                  'company')  # Ask for a user which share u want to sell
            sell_share = int(input("Number of shares to sell\n"))
            updated_stock_share = self.stock_jf["Stock Report"][choice]["Number of Share"] + sell_share
            # New Share updates
            with open("stock.json", "w") as jf:
                self.stock_jf["Stock Report"][choice]["Number of Share"] = updated_stock_share
                jf.write(json.dumps(self.stock_jf, indent=2))

            updated_person_share = self.person_json_value['Person'][index]["Number of Share"] - sell_share
            # Decrementing the shares

            person_share_price = int(input("price for per share you want from company\n"))
            person_updated_balance = self.person_json_value['Person'][index][
                                         "Total Balance"] + person_share_price * sell_share  # updated balance

            print(' --> ', person_share_price * sell_share, '<--will be Added to your total balance\n')
            print('Now Your Updated Balance is ', person_updated_balance, "\n")

            print('Now Your Updated Number of share is ', updated_person_share, "\n")

            with open("customers.json", "w") as jf:
                self.person_json_value['Person'][index]['Total Balance'] = person_updated_balance
                self.person_json_value['Person'][index]['Number of Share'] = updated_person_share
                jf.write(json.dumps(self.person_json_value, indent=2))

    except Exception as e:
        print(e)


if __name__ == "__main__":
    person_object = Person()                                        # object for person class
    person_object.show_shares()
    print("\n")
    try:
        i = int(input("1: Admin Login or 2: User \n"))
        if i == 1:                                                  # If user selects as Admin
            print("welcome Admin")
            j = int(input("press 1 to add Company :\n"))
            if j == 1:
                person_object.add_new_company()
        elif i == 2:                                                # if user selects as User
            print("fill your details\n")
            person_object.check_validity()

        else:
            print("Invalid choice")

    except ValueError:
        print("Invalid Value")


