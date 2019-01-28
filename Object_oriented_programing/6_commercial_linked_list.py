# author: Sai Anjan
# task  : Object Oriented programming
# date  : 26/01/19

""" Maintain the List of CompanyShares in a Linked List So new CompanyShares can be added or removed easily.
    Do not use any Collection Library to implement Linked List.
"""
import json
from UtilityMethods.ds_utility import *


class CommercialLinkedList:
    """ This class is created to add the stock data to
        the inventory management
    """

    def commercial_linked_list(self):                        # This method is used to add and delete the data in stock

        linked_list_object = LinkedList()
        with open("inventory_management.json", "r") as file:  # converting json file to python
            stock = json.load(file)

        # this loop is used to add the data to the stock
        for items in stock["stock"]:
            linked_list_object.append(items)
        print(linked_list_object.display_content())

        name = input(" Enter the name of Share\n")
        number = int(input("Enter no of Shares\n"))
        price = int(input("Enter the price\n"))

        # add dict is used to add name, no. of share and price
        add = {"Stock Name": name,
               "Number of Share": number,
               "Share Price": price}

        linked_list_object.append(add)                      # linked list append is used to add elements
        print(linked_list_object.size())
        print(linked_list_object.display_content())

        add_stock = {"stock": []}

        # this list is used to append the items
        for item in linked_list_object.display_content():
            add_stock["stock"].append(item)

        # open file to convert python to json file
        with open("inventory_management.json", "w") as file:
            data = json.dumps(add_stock, indent=2)
            file.write(data)
        print(data)

        # this loop is used to calculate the stock value
        for sto_det in data["stock"]:
            rice_total_price = int(sto_det["number_of_shares"]) * int(sto_det["share_price"])
            print(sto_det["stock_name"], " = ", rice_total_price)

        # open file to convert python to json file
        with open('inventory_management.json', 'w') as file:
            data = json.dump(data, file)
            file.write(data)
        print(data)


commercial_object = CommercialLinkedList()                    # inventory object is created

if __name__ == '__main__':
    commercial_object.commercial_linked_list()                 # inventory management method is called
