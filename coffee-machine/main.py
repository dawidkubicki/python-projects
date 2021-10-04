from data import MENU
from data import resources

# https://replit.com/@appbrewery/coffee-machine-final?embed=1&output=1#main.py

turned_on = True

money = 0.0
water = resources['water']
milk = resources['milk']
coffee = resources['coffee']


def check_sufficent(coffee_price: int):

    change = 0.0

    q = int(input("how many quarters: "))
    d = int(input("how many dimes: "))
    n = int(input("how many nickles: "))
    p = int(input("how many pennies: "))

    usr_money = q*0.25 + d*0.10 + n*0.05 + p*0.01

    if usr_money >= coffee_price:

            change = usr_money - coffee_price
            print(f"Here is ${change} in change.")

            return True

    else:
        print("Sorry that's not enough money. Money refunded.")

        return False



while turned_on:

    opt = str(input("What would you like? (espresso/latte/cappuccino): "))

    if opt == "report":
        print(f"Water: {water}ml\n"
              f"Milk: {milk}ml\n"
              f"Coffee: {coffee}g\n"
              f"Money: ${money}\n")

    elif opt == "espresso":

        if water >= 50 and coffee >=18:
            if check_sufficent(coffee_price=1.50):
                #TODO: add change resources function here
                water -= 50
                coffee -= 18
                money += 1.50


        else:
            if water < 50:
                print("Sorry there is not enough water")
            if coffee < 18:
                print("Sorry there is not enough cofeee")
            if water < 50 and coffee < 18:
                print("Sorry there is not enough water and coffee")


    elif opt == "latte":
        if water >= 200 and coffee >= 24 and milk >= 150:
            if check_sufficent(coffee_price=2.50):
                #TODO: add change resources function here
                water -= 200
                coffee -= 24
                milk -= 150
                money += 2.50
        else:
            if water < 200:
                print("Sorry there is not enough water")
            if coffee < 24:
                print("Sorry there is not enough cofeee")
            if milk < 150:
                print("Sorry there is not enough milk")
            if water < 200 and coffee < 24 and milk < 150:
                print("Sorry there is not enough water, coffee, milk")

    elif opt == "cappucino":
        if water >= 250 and coffee >= 24 and milk >= 100:
            if check_sufficent(coffee_price=3.00):
                #TODO: add change resources function here
                water -= 250
                coffee -= 24
                milk -= 100
                money += 3.50

        else:
            if water < 250:
                print("Sorry there is not enough water")
            if coffee < 24:
                print("Sorry there is not enough cofeee")
            if milk < 100:
                print("Sorry there is not enough milk")
            if water < 250 and coffee < 24 and milk < 100:
                print("Sorry there is not enough water, coffee, milk")

    elif opt == "off":
        #TODO: turn off the program
        turned_on = False

    else:
        print("Wrong command!")


    # print(f"Water: {water}ml\n"
    #       f"Milk: {milk}ml\n"
    #       f"Coffee: {coffee}g\n"
    #       f"Money: ${money}\n")

if turned_on == False:
    print("End of the program")

