import random
from words import rd_list

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

while True:

	end_of_game = False
	word_list = ["ardvark", "baboon", "camel"]
	chosen_word = random.choice(rd_list)
	word_length = len(chosen_word)

	#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
	#Set 'lives' to equal 6.

	lives = 6

	#Testing code
	#print(f'Pssst, the solution is {chosen_word}.')


	print("Game starts now!")




	#Create blanks
	display = []
	for _ in range(word_length):
		display += "_"

	while not end_of_game:
		guess = input("Guess a letter: ").lower()

		for position in range(word_length):
			letter = chosen_word[position]
			
			if letter==guess:
				display[position] = letter

		if guess not in chosen_word:
			lives-=1
			print(f"{stages[lives]}")

	    #TODO-2: - If guess is not a letter in the chosen_word,
	    #Then reduce 'lives' by 1. 
	    #If lives goes down to 0 then the game should stop and it should print "You lose."

		print(f"{' '.join(display)}")

		if "_" not in display:
			end_of_game = True
			print("You win.")

		elif lives<=0:
			end_of_game = True
			print("You lose.")

	    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
