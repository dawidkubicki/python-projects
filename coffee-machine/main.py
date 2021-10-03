from data import MENU
from data import resources


# https://replit.com/@appbrewery/coffee-machine-final?embed=1&output=1#main.py

turned_on = True
money = 0

def usr_Order():
    opt = str(input("What would you like? ((espresso/latte/cappuccino): "))

    if opt == "report":
        print(f"Water: {resources['water']}ml\n"
              f"Milk: {resources['milk']}ml\n"
              f"Coffee: {resources['coffee']}g\n"
              f"Money: ${money}\n")

    elif opt == "espresso":
        pass

    elif opt == "latte":
        pass

    elif opt == "cappucino":
        pass

    elif opt == "off":
        turned_on = False

    else:
        print("Wrong command!")


usr_Order()


# TODO:2 Make order and update resources
# TODO:3 Check resources sufficient do due usr_Order function
# TODO:4 Process coins -> quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# TODO:5 Check the transaction successful
