import random

print("Welcome to the Number Guessing Game!")

'''
	1. Randomly choose a number from a list of 1-100
	2. Choose by user a difficulty (easy or hard) 
	3. Regarded of a chosen difficulty -> Give a user 5 or 10 attempts to guess the number
	4. Whether the number is higher or lower, print 'To low. Guess again' or 'To high. Guess again'
	5. If the user win print -> 'You got it! The answer is answer'
	6. Else print 'You lose!'
'''

EASY_MODE = 10
HARD_MODE = 5

play = True

def draw_random() -> int:
	return random.randint(1,100)

def choose_difficulty():
	decision = input("Choose a difficulty. Type 'easy' or 'hard': ")
	
	if decision == 'hard':
		return HARD_MODE
	if decision == 'easy':
		return EASY_MODE

def check_number(usr_guess: int, number: int) -> bool:
	if int(usr_guess)>number:
		print("That's too high! \nGuess again.")
		return False
	if int(usr_guess)<number:
		print("That's too low! \nGuess again.")
		return False
	if int(usr_guess) == number:
		print(f"You got it! The answer is {number}")
		return True

def game():
	com_number = draw_random()
	print("I am thinking of a number between 1 and 100.")

	difficulty = choose_difficulty()


	while(difficulty>0):
		print(f"You have {difficulty} attempts remaining to guess the number ")
		usr_input = input("Make a guess: ")
		ans = check_number(int(usr_input), int(com_number))

		if ans:
			difficulty=1

		difficulty -= 1

	if ans==False:
		print("You have run out of attempts!")


while play:
	game()
	decision = input("Would you like to play a game ('yes' or 'no'): ")

	if decision=='yes':
		play=True
	else:
		play=False
		print("Bye!")
		
	

