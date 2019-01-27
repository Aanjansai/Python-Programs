""" Maintain the List of CompanyShares in a Linked List So new CompanyShares can be added or removed easily.
    Do not use any Collection Library to implement Linked List.
"""

import json
from UtilityMethods.ds_utility import *

linked_list_object = LinkedList()
with open("inventory_management.json", "r") as file:  # converting a
    stock = json.load(file)

for items in stock["stock"]:
    linked_list_object.append(items)
print(linked_list_object.display_content())

name = input(" Enter the name of Share\n")
number = int(input("Enter no of Shares\n"))
price = int(input("Enter the price\n"))

add = {"Stock Name": name,
       "Number of Share": number,
       "Share Price": price}

linked_list_object.append(add)
print(linked_list_object.size())
print(linked_list_object.display_content())

add_stock = {"stock": []}
for item in linked_list_object.display_content():
    add_stock["stock"].append(item)

with open("inventory_management.json", "w") as file:
    data = json.dumps(add_stock, indent=2)
    file.write(data)
print(data)

print("Enter the Company to be delete\n")
with open('inventory_management.json', 'r') as file:
    data = json.loads(file)
    data_string = str(data)
for element in data_string:
    if "IBM" in element:
        del element["IBM"]
        print("")

with open('inventory_management.json', 'w') as file:
    data = json.dump(data, file)

