fizz = "fizz"
buzz = "buzz"

#until should be > 1
def print_fizz_buzz(until):
	for number in range(1,until+1):
		if number%3 == 0:
			if number%5 == 0:
				print(fizz+buzz)
			else:
				print(fizz)
		elif number%5 == 0:
			print(buzz)
		else:
			print(number)

print_fizz_buzz(30)