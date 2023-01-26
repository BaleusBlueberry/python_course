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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def check_resources(coffee_type):
    global missing_element
    missing_element = ""
    for key in MENU[coffee_type]["ingredients"]:
        locals()[key] = MENU[coffee_type]["ingredients"][key]
        if resources[key] >= eval(key):
            pass
        else:
            missing_element = key
            return True
    return False


def payment(choice):
    coins = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01,
    }

    user_money = 0
    payment_price = float(MENU[choice]["cost"])
    print(f"the amount of money required: ${payment_price}")
    for coin in coins:
        coin_choice = int(input(f"how many {coin}: "))
        user_money += coin_choice * coins[coin]
        print(f"total amount inputted: ${user_money}")
    if user_money < payment_price:
        print(f"'not enough money' transaction cancelled, refunded ${user_money} back")
        return 0
    else:
        change = round((user_money - payment_price), 2)
        if change != 0:
            print(f"Here is ${change} in change.")
            return payment_price


# TODO 5 Process coins.
# TODO 6 Check transaction successful?
# TODO 7 Make Coffee.

user_choice = ""

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
        if check_resources(user_choice):
            print(f"sorry there is not enough {missing_element}")
        else:
            pays = payment(user_choice)
            if pays != 0:
                profit += pays
                for key in MENU[user_choice]["ingredients"]:
                    resources[key] -= MENU[user_choice]["ingredients"][key]
                print(f"Here is your {user_choice}. Enjoy!")


