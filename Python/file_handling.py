#Wrote this to practice with handling files

try:
	output_file = open("python_test_file.txt", "w")
	output_file.write("Writing to the file.\n")
	output_file.write("This is pretty easy.\n")
except:
	print("Some error occured.")
finally:
	output_file.close()

input_file = open("python_test_file.txt", "r")
for line in input_file:
	line = line.strip() #strip the line so that whitespaces and blank lines are removed
	print(line)
input_file.close()


print()
#use the with construciton to automatically close files

try:
	with open("python_test_file.txt", "w") as output_file:
		output_file.write("This time I don't need to manually close the output file.\n")
		output_file.write("This is still pretty easy.\n")
except:
	print("Some error occured.")


with open("python_test_file.txt", "r") as input_file:
	for line in input_file:
		line = line.strip()
		print(line)

