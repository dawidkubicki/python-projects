import os

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

#Calculator

#Add 
def add(n1, n2):
	return n1+n2

#Subtract
def subtract(n1, n2):
	return n1-n2

#Multiply
def multiply(n1, n2):
	return n1*n2

#Divide
def divide(n1, n2):
	return n1/n2

operations = {
	"+": add,
	"-": subtract,
	"*": multiply,
	"/": divide
	}


print(f"{logo}\n")

decision='y'

num1 = int(input("What's the first number: "))
num2 = int(input("What's the second number: "))

for key in operations:
	print(key)

operation_symbol = str(input("Pick an operation: "))
function = operations[operation_symbol]

answer = function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")

decision = str(input(f"Type 'y' to continue with {answer}, or type 'n' to exit: "))

while decision=='y':
	operation_symbol = str(input("Pick an operation: "))
	num = int(input("What's the next number: "))
	function = operations[operation_symbol]
	new_answer = function(answer, num)

	print(f"{answer} {operation_symbol} {num} = {new_answer}")
	decision = str(input(f"Type 'y' to continue with {new_answer}, or type 'n' to exit: "))

	answer=new_answer	

if decision=='n':
	print("the end")






