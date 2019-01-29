# author: Sai Anjan
# task  : Object Oriented programming
# date  : 23/01/19

""" Desc -> Extend the above program to Create InventoryManager to manage the Inventory.
    The Inventory Manager will use InventoryFactory to create Inventory Object from JSON.
    The InventoryManager will call each Inventory Object in its list to calculate the Inventory Price
    and then call the Inventory Object to return the JSON String. The main program will be with InventoryManager
    I/P -> read in JSON File
    Logic -> Get JSON Object in Java or NSDictionary in iOS. Create Inventory Object from JSON.
    Calculate the value for every Inventory.
    O/P -> Create the JSON from Inventory Object and output the JSON String.
"""

import json
from UtilityMethods.ds_utility import *


class InventoryManagement:
    """ This class is created to add the stock data to
        the inventory management
    """
    @staticmethod
    def inventory_management():                               # This method is used to add and delete the data in stock

        linked_list_object = LinkedList()
        with open("inventory_management.json", "r") as file:  # converting json file to python
            stock = json.load(file)

        # this loop is used to add the data to the stock
        for items in stock["stock"]:
            linked_list_object.append(items)
        print(linked_list_object.display_content())
        try:
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
        except ValueError:
            print("enter valid data")


inventory_object = InventoryManagement()                    # inventory object is created

if __name__ == '__main__':
    try:
        inventory_object.inventory_management()                 # inventory management method is called
    except UnboundLocalError:
        print("try again by entering valid data")






