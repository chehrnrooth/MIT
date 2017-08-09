#author chehrnrooth 
low = 0
high = 100
guess = (high + low)//2
print ('Please think of a number between 0 and 100!')
h = 'h'
l = 'l'
c = 'c'
while True: #secret number engine for Bisection Search
	print ('Is your secret number '+ str(guess)+ '?')
	userInput = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
	if userInput == 'h':
		high = guess
		guess = (high + low)//2
		guess = int(guess)
		continue
	elif userInput == 'l':
		low = guess
		guess = (high + low)//2
		guess = int(guess)
		continue
	elif userInput == 'c':
		break
	else:
		print ("Sorry, I did not understand your input")
		continue
print ('Game over. Your secret number was:', guess)
