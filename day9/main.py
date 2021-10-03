import art
import game_data
import random

#print(art.go)
#print(art.vs)


'''
Plan of a attack: 

Link to a game: https://replit.com/@appbrewery/higher-lower-final?embed=1&output=1#main.py

1. Create a function reading random question
2. Create a function comparing results
    a) If its return True -> Add point, add a question index number to not readable agai    n questions. 

    You can create a list of indexes and use it as index, and every single time you are 
    will be reading from it use function pop to delete it. Remember it game will be starting again to update numbers of the elements.

    Else return False -> Show numnber of points
3. Create a function adding a point

'''

#generate rivals and return list of two of them
def generate_rivals(database: list) -> list:
    rivals = []
    for i in range(2):
        opt = random.choice(database)
        rivals.append(opt)

    return rivals

#show the rivals
def display_them(rivals: list):
    print(f"{rivals[0]['name']}, a {rivals[0]['description']}, from {rivals[0]['country']}")
    print(art.vs)
    print(f"{rivals[1]['name']}, a {rivals[1]['description']}, from {rivals[1]['country']}")
    
def compare_rivals(rivals: list, usr_choice: str):
    score_A = int(rivals[0]['follower_count'])
    score_B = int(rivals[1]['follower_count'])

    if usr_choice=="a":
        if score_A > score_B:
            return True
        else:
            return False

    elif usr_choice=="b":
        if score_A < score_B:
            return True
        else:
            return False

def game():

    score = 0
    play= True

    while play:

        rivals = generate_rivals(game_data.data)
        display_them(rivals)
        usr_choice = input("Who has more followers? Type 'A' or 'B': ")

        if compare_rivals(rivals, usr_choice):
            score += 1
            print(f"You are right! Current score: {score}.")
    
        elif compare_rivals(rivals, usr_choice)==False:
            print(f"Sorry, that's wrong. Final score: {score}.")
            play = False

    decision = input("If you want to play again type 'yes' or 'no': ")
    if decision == "yes":
        play = True
    else:
        play = False
        running_program = False

running_program = True

while running_program: 
    game()




