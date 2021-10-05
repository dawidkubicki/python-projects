from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

turned_on = True

while turned_on:

    decision = input(f"What would you like: ({menu.get_items()}): ")

    if decision == "report":
        coffee_maker.report()
        money_machine.report()

    elif decision == "off":
        turned_on = False

    else:
        coffee = menu.find_drink(decision)

        if money_machine.make_payment(coffee.cost):
            if coffee_maker.is_resource_sufficient(coffee):
                coffee_maker.make_coffee(coffee)

