fizz = "fizz"
buzz = "buzz"

#until should be > 1
def print_fizz_buzz(until):
	for number in range(1,until+1):
		output = ""
		if(first_mod_second_is_third(number, 3, 0)):
			output += fizz
		if(first_mod_second_is_third(number, 5, 0)):
			output += buzz
		if (output == ""):
			output = number

		print(output)

#first, second, and third must all be integers
def first_mod_second_is_third(first, second, third):
	if (first % second == third):
		return True
	return False

print_fizz_buzz(30)