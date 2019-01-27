""" Desc -> Create a JSON file having Inventory Details for Rice, Pulses and
    Wheat with properties name, weight, price per kg.
    Use Library : Java JSON Library, For IOS JSON Library use NSJSONSerialization for parsing the JSON.
    I/P -> read in JSON File
    Logic -> Get JSON Object in Java or NSDictionary in iOS. Create Inventory Object from JSON.
    Calculate the value for every Inventory.
    O/P -> Create the JSON from Inventory Object and output the JSON String
"""

import json


class FoodInventory:
    """ This class is created to display the details of the
        inventory data which is containing the grains.
    """

    def food_grains(self):

        # json file is created to store the data inside the file.
        with open("inventory_data.json", "r") as file:
            file_read = file.read()
            file.close()
            items = json.loads(file_read)
        print(items, "\n")
        print("rice price details")
        print(" ", " ", " ", "||")
        print(" ", " ", " ", "||")
        print(" ", " ", " ", "\/")

        # this loop displays the details of the rice and value of rice inventory
        for rice in items["Rice"]:
            rice_total_price = int(rice["price per kg"]) * int(rice["weight"])
            print(rice["name"], " = ", rice_total_price)
        print("\n")

        print("wheat price details")
        print(" ", " ", " ", "||")
        print(" ", " ", " ", "||")
        print(" ", " ", " ", "\/")

        # this loop displays the details of the wheat and value of wheat inventory
        for wheat in items["Wheat"]:
            wheat_total_price = int(wheat["price per kg"]) * int(wheat["weight"])
            print(wheat["name"], " = ", wheat_total_price)
        print("\n")

        print("pulse price details")
        print(" ", " ", " ", "||")
        print(" ", " ", " ", "||")
        print(" ", " ", " ", "\/")

        # this loop displays the details of the pulse and value of pulse inventory
        for pulse in items["Pulse"]:
            pulse_total_price = int(pulse["price per kg"] * int(pulse["weight"]))
            print(pulse["name"], " = ", pulse_total_price)


object_grain = FoodInventory()                  # Food inventory object is created

if __name__ == '__main__':
    object_grain.food_grains()                  # food grain method is called
