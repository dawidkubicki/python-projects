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
    global money

    q = int(input("how many quarters: "))
    d = int(input("how many dimes: "))
    n = int(input("how many nickles: "))
    p = int(input("how many pennies: "))

    usr_money = q*0.25 + d*0.10 + n*0.05 + p*0.01

    if usr_money >= coffee_price:

            change = usr_money - coffee_price
            print(f"Here is ${change} in change.")
            money+=coffee_price

            return True

    else:
        print("Sorry that's not enough money. Money refunded.")

        return False


def usr_Order():
    opt = str(input("What would you like? (espresso/latte/cappuccino): "))

    global water, milk, coffee, money

    if opt == "report":
        print(f"Water: {water}ml\n"
              f"Milk: {milk}ml\n"
              f"Coffee: {coffee}g\n"
              f"Money: ${money}\n")

    elif opt == "espresso":

        if water >= 50 and coffee >=18:
            if check_sufficent(coffee_price=1.50):
                water -= 50
                coffee -= 18

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
                water -= 200
                coffee -= 24
                milk -= 150

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
            if check_sufficent(coffee_price=2.50):
                water -= 250
                coffee -= 24
                milk -= 100

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
        global turned_on
        turned_on = False

    else:
        print("Wrong command!")

while turned_on:
    usr_Order()

if turned_on == False:
    print("End of the program")



# TODO:2 Make order and update resources
# TODO:3 Check resources sufficient do due usr_Order function
# TODO:4 Process coins -> quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# TODO:5 Check the transaction successful