print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? $")
percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
num_people = input("How many people to split the bill? ")

if int(num_people) > 0:
    amount = float(total_bill)/float(num_people)
    amount *= (float(percentage)/100+1)

    print(round(amount, 2))

elif float(num_people) == 0:
    amount = round(total_bill, 2)
    print(f"You should pay: ${amount}")

