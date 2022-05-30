#A revised oop version of my previous small program coffeeMaker.py
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True

while is_on == True:
    options = menu.get_items()
    drinkSelect = input(f"What would you like? {options}: \n")
    if drinkSelect == "off":
        is_on = False
    elif drinkSelect == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        choice = menu.find_drink(drinkSelect)
        if coffee_maker.is_resource_sufficient(choice) and money_machine.make_payment(choice.cost):
            coffee_maker.make_coffee(choice)






