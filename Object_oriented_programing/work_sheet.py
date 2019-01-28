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

#
# import json
# from UtilityMethods.ds_utility import *
#
# ll = LinkedList()
# with open("stock.json", "r") as jf:  # converting a
#     stock = json.load(jf)
#
# for i in stock['Stock Report']:
#     ll.append(i)
# print(ll.display_content())
# print(ll.size())
#
# name = input(" Enter the name of Share")
# number = int(input("Enter no of Shares"))
# price = int(input("Enter the price"))
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
# add_stock = {"Stock Report": []}
# for item in ll.display_content():
#     add_stock["Stock Report"].append(item)
#
#
# with open("stock.json", "w") as f:
#     data = json.dumps(add_stock, indent=2)
#     f.write(data)
# print(data)
#
# print("Enter the Company to be delete")
# with open('stock.json', 'r') as jf:
#     data = json.load(jf)
# for element in data:
#     if'abcd' in element:
#         del element['abcd']
#         print("")
#
# with open('stock.json', 'w') as jf:
#     data = json.dump(data,jf)


from UtilityMethods.ds_utility import LinkedList

import json


def linked_list_stock():
    l = LinkedList()
    with open('stock.json', "r") as f:
        f = json.load(f)

    for i in f["Stock Report"]:

        l.append(i)

    l.display()
    print("\n1.add stocks\n2.remove stocks\n3.exit")
    choice = int(input("Enter choice: \n"))

    if choice == 1:
        # print(l.display())
        comp_name = input("stock name\n")
        no_of_share = int(input("No of shares \n"))
        price_per_share = int(input("price per share : \n"))

        new_comp = {'Stock Name': comp_name,
                    'Number of Share': no_of_share,
                    'Share Price': price_per_share}
        l.append(new_comp)
        e = l.display()
        print(e)
    elif choice == 2:
        with open("stock.json", 'r') as jf:
            json_str = jf.read()        # read json file
            jf.close()
        json_value = json.loads(json_str)
        print(json_value)
        list3 = []
        data = input("Enter company name to remove: \n")
        for i in range(len(json_value['Stock Report'])):
            for key in (json_value['Stock Report'][i]):
                list3.append(json_value['Stock Report'][i][key])
        print(list3)

        for i in (json_value['Stock Report']):
            for key in (json_value['Stock Report'][i]):
                if list3.__contains__(data):
                    l.remove(json_value['Stock Report'][i][key])
                    break
        e = l.display()
        print(e)

    elif choice == 3:
        exit(0)

    else:
        print("you have entered wrong input")
        exit(0)


if __name__ == "__main__":
    linked_list_stock()
