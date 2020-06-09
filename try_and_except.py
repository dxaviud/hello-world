#this shows how try/except can be used to force the user to input the correct thing

while True:
	try:
		int_input = int(input("enter a number: "))
		print("Good job, you entered " + str(int_input) + "!")
		break
	except ValueError:
		print("You didn't enter a number... try it again.")
		continue

