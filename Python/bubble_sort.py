#Bubble sort

from random import randint

def bubble_sort(a_list):
	'''
	This function implements the bubble sort algorithm. An iterator goes from the first element to one less than the last.
	Adjacent values in the list are compared; If the value on the left is greater, the values are swapped. 
	If no swaps were made after iterating through the entire list, the list is sorted already and it is returned.
	'''

	for stop_index in range(len(a_list)-1, 0, -1): 
		#stop_index is the index at which the inner for loop (using "i") will terminate.
		#stop_index decreases by one after each iteration because the right end of the list becomes sorted over time, so that portion does not need to be checked.
		did_at_least_one_swap = False
		#a_list will be immediately return if did_at_least_one_swap is False by the end of an inner for loop interation. If no swaps occured, the list is sorted.
		for i in range(0,stop_index):
			#The element at index i and i+1 will be compared to see if a swap needs to occur
			if a_list[i] > a_list[i+1]:
				#swap needs to occur since the left is greater
				a_list[i], a_list[i+1] = a_list[i+1], a_list[i] #swap 
				did_at_least_one_swap = True #since a swap occured, this variable is set to True
		if did_at_least_one_swap is False:
				return a_list #return the sorted list
	return a_list #return the sorted list

def list_is_sorted(a_list):
	'''
	This function returns True if the list argument is sorted, False if not.
	Consecutive elements in the list are compared to see if each successive element is greater or equal to the previous.
	'''

	for i in range(1, len(a_list)): #loop through the list, starting at index 1
		previous_element = a_list[i-1]
		current_element = a_list[i]
		if current_element < previous_element:
			return False #return False since successive elements should be greater or equivalent, not lesser
	return True #got through entire list without returning False, so the list must be sorted


my_list = [] 

for i in range(10):
	my_list.append(randint(0,9)) #adding 10 random values from 0 to 9 to my_list

print("unsorted: " + str(my_list)) #print the unsorted list
my_list = bubble_sort(my_list) #sort the list
print("sorted increasing: " + str(my_list)) #print the sorted list
print("sorted list is sorted: " + str(list_is_sorted(my_list))) #print whether the list has actually been sorted.


#run lots of tests to see if the list is consistently sorted
number_of_tests = 50
my_list_size = 15
actually_sorted_count = 0

print("Testing...")
for i in range(number_of_tests):

	for i in range(my_list_size):
		my_list.append(randint(0,my_list_size))

	my_list = bubble_sort(my_list)

	if (list_is_sorted(my_list)):
		actually_sorted_count += 1

print("Total tests ran: " + str(number_of_tests))
print("Number of tests where the list was actually sorted: " + str(actually_sorted_count))

