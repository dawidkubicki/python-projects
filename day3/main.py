import random

while True:
    decision = input("Welcome to Rock Paper Scissors game. Make your decision: \n 1.Rock \n 2. Paper \n 3.Scissors \n \n")

    decision = int(decision)

    rock = """
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """

    paper = """
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """

    scissors = """
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """ 

    options = [rock, paper, scissors]

    bot = random.randrange(0,2)

    bot_move = options[bot] 
    player_move = options[decision-1]

    if bot == 0:
        if int(decision-1) == 0:
            print(f"Tight! \n {rock} {rock}")
        elif decision-1 == 1:
            print(f"You have won! \n {rock} {paper}")
        elif decision-1 == 2:
            print(f"You have lost! \n {rock} {scissors}")

    if bot == 1:
        if int(decision-1) == 0:
            print(f"You lost! \n {paper} {rock}")
        elif decision-1 == 1:
            print(f"Thight! \n {paper} {paper}")
        elif decision-1 == 2:
            print(f"You have won! \n {paper} {scissors}")

    if bot == 3:
        if int(decision-1) == 0:
            print(f"You have won! \n {scissors} {rock}")
        elif decision-1 == 1:
            print(f"You have lost! \n {scissors} {paper}")
        elif decision-1 == 2:
            print(f"Thight! \n {scissors} {scissors}")


