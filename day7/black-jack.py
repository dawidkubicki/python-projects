import random
logo = '''

.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_/
      |  \/ K|                            _/ |                
      `------'                           |__/           

'''
print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#choose randomly 2 cards for your deck
def choose_cards(cards: list) -> list:
	picked = []
	for i in range(2):
		picked.append(random.choice(cards))
		
	return picked

#calculate score from a deck of cards
def calculate_score(cards: list) -> int:
	score=0
	for e in cards:
		score+=e
	return score		

#return a single move
def single_move(cards: list) -> int:
	return random.choice(cards)

#add a random card to a desk
def add_card(cards: list, deck: list):
	new_card = single_move(cards)
	deck.append(new_card)
	return deck

def show_first_elem_of_list(deck: list) -> int:
	return deck[0]

#The user and computer should each get 2 random cards
usr_deck = choose_cards(cards)
com_deck = choose_cards(cards)

first_elem = show_first_elem_of_list(com_deck)

draw_card = 'y'
play=True

while play:
	#Add up the user's and the computere's scores
	usr_score = calculate_score(usr_deck)
	com_score = calculate_score(com_deck)
	
	print(f"Your deck: {usr_deck}. Your score: {usr_score}.")
	print(f"Computer's first card: {first_elem}.")


	#check whether user or computer has a blackjack
	if usr_score == 21:
		print(f"Your final deck: {usr_deck}. Your final score: {usr_score}.")
		print(f"Computer's final deck: {com_deck}. Computer's final score: {com_score}.")
		print(f"You won!")
		draw_card = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
		usr_deck = []
		com_deck = []
		usr_deck = add_card(cards, usr_deck)
		com_deck = add_card(cards, com_deck)

	if com_score == 21:
		print(f"Your final deck: {usr_deck}. Your final score: {usr_score}.")
		print(f"Computer's final deck: {com_deck}. Computer's final score: {com_score}.")
		print(f"You lost!")
		draw_card = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
		usr_deck = []
		com_deck = []
		usr_deck = add_card(cards, usr_deck)
		com_deck = add_card(cards, com_deck)
	if usr_score > 21:
		if usr_score == com_score:
			print(f"Your final deck: {usr_deck}. Your final score: {usr_score}.")
			print(f"Computer's final deck: {com_deck}. Computer's final score: {com_score}.")
			print(f"It's a draw!")
			draw_card = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
			usr_deck = []
			com_deck = []
			usr_deck = add_card(cards, usr_deck)
			com_deck = add_card(cards, com_deck)
		else:
			print(f"Your final deck: {usr_deck}. Your final score: {usr_score}.")
			print(f"Computer's final deck: {com_deck}. Computer's final score: {com_score}.")
			print(f"You lost!")
			draw_card = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
			usr_deck = []
			com_deck = []
			usr_deck = add_card(cards, usr_deck)
			com_deck = add_card(cards, com_deck)
	if com_score > 21:
		if usr_score == com_score:
			print(f"Your final deck: {usr_deck}. Your final score: {usr_score}.")
			print(f"Computer's final deck: {com_deck}. Computer's final score: {com_score}.")
			print(f"It's a draw!")
			draw_card = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
			usr_deck = []
			com_deck = []
			usr_deck = add_card(cards, usr_deck)
			com_deck = add_card(cards, com_deck)
		else:
			print(f"Your final deck: {usr_deck}. Your final score: {usr_score}.")
			print(f"Computer's final deck: {com_deck}. Computer's final score: {com_score}.")
			print(f"You won!")
			draw_card = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
			usr_deck = []
			com_deck = []
			usr_deck = add_card(cards, usr_deck)
			com_deck = add_card(cards, com_deck)
	draw_card = input("Type 'y' to get another card, type 'n' to pass: ")

	if draw_card=='y':
		usr_deck = add_card(cards, usr_deck)
		com_deck = add_card(cards, com_deck)
	
	if draw_card=='n':

		com_deck = add_card(cards, com_deck)
		com_score = calculate_score(com_deck)

		if com_score > 21:
			print(f"Your final deck: {usr_deck}. Your final score: {usr_score}.")
			print(f"Computer's final deck: {com_deck}. Computer's final score: {com_score}.")
			print(f"You won!")
			draw_card = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
			usr_deck = []
			com_deck = []
		else:
			if usr_score > com_score:
				print(f"Your final deck: {usr_deck}. Your final score: {usr_score}.")
				print(f"Computer's final deck: {com_deck}. Computer's final score: {com_score}.")
				print(f"You won!")
				draw_card = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
				usr_deck = []
				com_deck = []
				
			if usr_score < com_score:
				print(f"Your final deck: {usr_deck}. Your final score: {usr_score}.")
				print(f"Computer's final deck: {com_deck}. Computer's final score: {com_score}.")
				print(f"You lost!")
				draw_card = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
				usr_deck = []
				com_deck = []
			if usr_score == com_score:
				print(f"Your final deck: {usr_deck}. Your final score: {usr_score}.")
				print(f"Computer's final deck: {com_deck}. Computer's final score: {com_score}.")
				print(f"It's draw!")
				draw_card = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
				usr_deck = []
				com_deck = []

