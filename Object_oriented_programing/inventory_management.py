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
for sto_det in data["stock"]:
    rice_total_price = int(sto_det["number_of_shares"]) * int(sto_det["share_price"])
    print(sto_det["stock_name"], " = ", rice_total_price)
with open('inventory_management.json', 'w') as file:
    data = json.dump(data, file)









