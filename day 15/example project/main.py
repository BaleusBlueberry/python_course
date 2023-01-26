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

profit = 0
resources = {
    "water": 3,
    "milk": 200,
    "coffee": 100,
}


# TODO 1 Prompt user by asking “What would you like? (espresso/latte/cappuccino):
# TODO 2 Turn off the Coffee Machine by entering “off” to the prompt.
# TODO 3 Print report.
# TODO 4 Check resources sufficient?
def check_resources(cofy):
    req_water = MENU[cofy]["ingredients"]["water"]
    req_coffee = MENU[cofy]["ingredients"]["coffee"]
    if any(MENU[cofy]["ingredients"]) == "milk":
        req_milk = MENU[cofy]["ingredients"]["milk"]
    else:
        req_milk = 0
    for key in resources:
        if resources[key] >= eval("req_" + key):
           print(key)
        else:
            fail = True
            break


# TODO 5 Process coins.
# TODO 6 Check transaction successful?
# TODO 7 Make Coffee.

user_choice = ()

while user_choice != "off":
    print(f"prices: espresso(1.5$), latte(2.5$), cappuccino(3.0$)")
    user_choice = input("What would you like? ").lower()

    if user_choice == "off":
        pass
    elif user_choice == "report":
        print(f'water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffee: {resources["coffee"]}g')
        print(f'Money: ${profit}')
    elif user_choice == "espresso" or "latte" or "cappuccino":
        check_resources(user_choice)

