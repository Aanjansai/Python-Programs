import json


str1_dist = {"stock": [{"stock_name": "IBM", "number_of_shares": 20, "share_price": 200},
                       {"stock_name": "ICICI", "number_of_shares": 30, "share_price": 250},
                       {"stock_name": "AXIS", "number_of_shares": 40, "share_price": 300}]}

store = json.dumps(str1_dist, indent=4)
with open("inventory_management.json", 'w+') as file:
    file.write(store)


with open("inventory_management.json", 'r') as file:
    read = file.read()
    load = json.loads(read)
print(load)

for stock in load["stock"]:
    total_stock_value = int(stock["number_of_shares"]) * int(stock["share_price"])
    print(stock["stock_name"], "total stock value =", total_stock_value)




