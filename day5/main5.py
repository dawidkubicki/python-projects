import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(f"{logo}\n")
print("Welcome to the secret auction program")

auction = {}
work = True

while work:
    name = str(input("What is your name?: "))
    bid = int(input("What is your bid?: $"))

    def add_bid(name: str, bid: int):
        auction[name] = bid

    add_bid(name, bid)

    ans = str(input("Are there any other bidders? Type 'yes' or 'no'.\n"))
    if ans == "yes":
        work = True
        os.system('clear')
    else:
        work = False
else:
    highest_bid=0
    for key in auction:
        amount = auction[key]
        if amount>highest_bid:
            highest_bid = amount
            winner = key

    print(f"The winner is {key} with a bid of {highest_bid}")
            
        
