import json

with open("inventory_data.json", "r") as file:
    file_read = file.read()
    file.close()
    items = json.loads(file_read)
print(items, "\n")

print("rice price details")
print(" ", " ", " ", "||")
print(" ", " ", " ", "||")
print(" ", " ", " ", "\/")
for rice in items["Rice"]:
    rice_total_price = int(rice["price per kg"]) * int(rice["weight"])
    print(rice["name"], " = ", rice_total_price)
print("\n")

print("wheat price details")
print(" ", " ", " ", "||")
print(" ", " ", " ", "||")
print(" ", " ", " ", "\/")
for wheat in items["Wheat"]:
    wheat_total_price = int(wheat["price per kg"]) * int(wheat["weight"])
    print(wheat["name"], " = ", wheat_total_price)
print("\n")

print("pulse price details")
print(" ", " ", " ", "||")
print(" ", " ", " ", "||")
print(" ", " ", " ", "\/")
for pulse in items["Pulse"]:
    pulse_total_price = int(pulse["price per kg"] * int(pulse["weight"]))
    print(pulse["name"], " = ", pulse_total_price)

