#author chehrnrooth 
while True:
	#validation of number, not really needed in the project.
	x = int(input("Please enter a number between 0 and 100: "))
	if x < 0 or x > 100:
		print "I'm sorry, but your entry of", x, "isn't within the bounds of 0 to 100, please try again"
		continue
	else:
		break

print ('Your secret number is', x)
low = 0
high = 100
guess = (high + low)/2.0

while True: #secret number engine for Bisection Search
	print 'Is your secret number', guess, '?'
	userInput = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
	print''
	if userInput == 'h':
		high = guess
		guess = (high + low)/2
		continue
	elif userInput == 'l':
		low = guess
		guess = (high + low)/2
		continue
	elif userInput == 'c':
		break
	else:
		print "Sorry, I did not understand your input"
		continue
