#author chehrnrooth
import random
for x in range(1):
	secretNumber = random.randint(1,101) #lmao now the computer plays itself
print("I'm thinking of a number between 0 and 100!")
low = 0
high = 100
guess = (high + low)/2

while True: #secret number engine for Bisection Search
	print 'Is your secret number', guess, '?'
	#userInput = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
	print('')
	if guess > secretNumber:
		high = guess
		guess = (high + low)/2
		continue
	elif guess < secretNumber:
		low = guess
		guess = (high + low)/2
		continue
	elif guess == secretNumber:
		break
print "My guess is that", guess,"is your secret number"
