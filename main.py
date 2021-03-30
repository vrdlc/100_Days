

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def make_coffee():
    """This is the main function that makes the drink using other functions"""
    choose_drink()


def choose_drink():
    type = MENU.get(choice)
    ingredients = type.get("ingredients")

    check_resources(type, ingredients)


def check_resources(type, ingredients):
    """This function checks to make sure there are enough ingredients for the chosen drink"""

    if "milk" not in ingredients:
        ingredients.update({"milk":0})

    if resources.get("milk") >= ingredients.get("milk"):
        if resources.get("water") >= ingredients.get("water"):
            if resources.get("coffee") >= ingredients.get("coffee"):
                print(f"We can make {choice}!")
                get_money(resources, type)
                calc_ingredients(resources, ingredients)
            else:
                print("We don't have enough coffee")
        else:
            print("We don't have enough water")
    else:
        print("We don't have enough milk")


def get_money(resources, type):
    print(choice)
    total = 0
    quarters = input("How many quarters will you insert? ")
    total = float(quarters) * .25
    print(f"You have inserted {total} so far.")
    dimes = input("How many dimes will you insert? ")
    total = round(total, 2) + (float(dimes) * .1)
    print(f"You have inserted {total} so far.")
    nickels = input("How many nickels will you insert? ")
    total = round(total, 2) + (float(nickels) * .05)
    print(f"You have inserted {total} so far.")
    pennies = input("How many pennies will you insert? ")
    total = round(total, 2) + (float(pennies) * .01)

    if total > type.get("cost"):
        print("Making drink...")
    # Checks to see if any cost has been added to the resources dict. If it's not there, create it, otherwise just
        # add new total to it
        total = total - type.get("cost")
        print(f"Here is your {choice} and here is ${round(total, 2)} in change. Enjoy!")
    else:
        print(f"You did not insert enough money. Here is your ${round(total, 2)} back. Thank you.")
    if "cost" in resources:
        resources["cost"] = resources.get("cost") + total
    else:
        resources.update({"cost": 0})
        resources["cost"] = resources.get("cost") + total


def calc_ingredients(resources, ingredients):
    print(ingredients)

    resources["milk"] = resources.get("milk") - ingredients.get("milk")
    resources["water"] = resources.get("water") - ingredients.get("water")
    resources["coffee"] = resources.get("coffee") - ingredients.get("coffee")

    print(resources)


machine_power = True


while machine_power == True:
    choice = input("What do you want? Select espresso, latte, or cappuccino").lower()
    if choice == "report":
        for key, value in resources.items():
            print(key, value)
    elif choice == "off":
        machine_power = False
        print("Turning off")
        exit()
    else:
        make_coffee()


