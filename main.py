# Importing "random" module.
import random

# Creating a storage of the range of numbers.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# Creating a variable in which guessed number contains.
guessed_number = random.choice(numbers)

# Creating a message for player.
print('I guessed the number between 1 and 20. Try to assume the number!')

# Creating a cycle which checks the player's assumed number.
while guessed_number in numbers:
	assumed_number = int(input())
	if assumed_number < guessed_number:
		print('Oh... Your number is smaller than mine! Try again.')
		continue
	elif assumed_number > guessed_number:
		print('Hah! Your number is bigger than mine! Try again.')
		continue
	else:
		print(f'Good job! You are right, predicted number was: {guessed_number}')
		break