#Made this to practice raising exceptions

def number_contained_inclusive(number, min_value, max_value):
	'''
	returns True if number is between min_value and max_value, inclusive. Returns False if this is not the case. 
	raises an exception if min_value is greater than max_value.
	'''
	if (min_value > max_value):
		raise Exception("Error: lower bound is greater than upper bound.")
	try:
		number = int(number)
		if number >= min_value and number <= max_value:
			return True
		else:
			return False
	except ValueError:
		print("Must have an int argument. Function terminated.")

one_contained_inclusive_zero_ten = number_contained_inclusive(1, 0, 10)
print(one_contained_inclusive_zero_ten)
one_contained_inclusive_zero_ten = number_contained_inclusive("a string", 0, 10)
print(one_contained_inclusive_zero_ten)
one_contained_inclusive_zero_ten = number_contained_inclusive(1, 10, 0)
print(one_contained_inclusive_zero_ten)
