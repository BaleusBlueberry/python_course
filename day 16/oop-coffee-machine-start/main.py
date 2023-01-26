
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
working_machine = True

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
drinks = Menu()
menu_item = MenuItem
def star_coffee_machine():
    user_choice = input("What would you like? (espresso/latte/cappuccino/):").lower()
    if user_choice == "off":
        working = False
        pass
    elif user_choice == "report":
        coffee_maker.report()
        money_machine.report()

    else:
        drink = drinks.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)







while working_machine:
    star_coffee_machine()