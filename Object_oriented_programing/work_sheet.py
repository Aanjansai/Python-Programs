# import json
#
#
# with open("inventory_management.json", 'r') as file:
#     file_read = file.read()
#     print(file_read)
# str2_dist = input("enter the stock name\n")
# str3_dist = int(input("enter the no.of shares\n"))
# str4_dist = int(input("enter the price of share\n"))
# string1 = str(str2_dist)
#
# with open("inventory_management.json", 'a') as file:
#     dis = json.dump((str2_dist, str3_dist, str4_dist), file)
#     fil_read = file.read()
#     print(fil_read)
#
#
# import json
# from UtilityMethods.ds_utility import *
#
# ll = LinkedList()
# with open("inventory_management.json", "r") as jf:  # converting a
#     stock = json.load(jf)
#
# for i in stock["stock"]:
#     ll.append(i)
# print(ll.display_content())
#
# name = input(" Enter the name of Share\n")
# number = int(input("Enter no of Shares\n"))
# price = int(input("Enter the price\n"))
#
# add = {
#       "Stock Name": name,
#       "Number of Share": number,
#       "Share Price": price
# }
#
# ll.append(add)
# print(ll.size())
# print(ll.display_content())
#
# add_stock = {"stock": []}
# for item in ll.display_content():
#     add_stock["stock"].append(item)
#
#
# with open("inventory_management.json", "w") as f:
#     data = json.dumps(add_stock, indent=2)
#     f.write(data)
# print(data)
#
# print("Enter the Company to be delete\n")
# with open('inventory_management.json', 'r') as jf:
#     data = json.load(jf)
# for element in data:
#     if'IBM' in element:
#         del element['IBM']
#         print("")
#
# with open('inventory_management.json', 'w') as jf:
#     data = json.dump(data, jf)


import json
from UtilityMethods.ds_utility import *

ll = LinkedList()
with open("stock.json", "r") as jf:  # converting a
    stock = json.load(jf)

for i in stock['Stock Report']:
    ll.append(i)
print(ll.display_content())
print(ll.size())

name = input(" Enter the name of Share")
number = int(input("Enter no of Shares"))
price = int(input("Enter the price"))

add = {
      "Stock Name": name,
      "Number of Share": number,
      "Share Price": price
}

ll.append(add)
print(ll.size())
print(ll.display_content())

add_stock = {"Stock Report": []}
for item in ll.display_content():
    add_stock["Stock Report"].append(item)


with open("stock.json", "w") as f:
    data = json.dumps(add_stock, indent=2)
    f.write(data)
print(data)

print("Enter the Company to be delete")
with open('stock.json', 'r') as jf:
    data = json.load(jf)
for element in data:
    if'abcd' in element:
        del element['abcd']
        print("")

with open('stock.json', 'w') as jf:
    data = json.dump(data,jf)



