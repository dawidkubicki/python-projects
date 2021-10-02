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

def generate_rivals(database: list) -> list:
    rivals = []
    for i in range(2):
        opt = random.choice(database)
        rivals.append(opt)

    return rivals

def display_them(rivals: list):
    print(f"{rivals[0]['name']}, a {rivals[0]['description']}, from {rivals[0]['country']}")
    print(art.vs)
    print(f"{rivals[1]['name']}, a {rivals[1]['description']}, from {rivals[1]['country']}")
    

def compare_rivals(rivals: list):
    for score in rivals:
        print(score["follower_count"])


rivals = generate_rivals(game_data.data)
display_them(rivals)

compare_rivals(rivals)
