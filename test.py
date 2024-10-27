### MSCS2202
### HW4-2
### Yuxin Zhang

#The program asks the user for input N (positive integer) and reads it

def user_input1():
	"""Input prompt"""

	user_input1 = input("Please input a positive integer N")
	print(f"{user_input1}")

#Then the program asks the user to provide N numbers (one by one) and reads all of them (again, one by one)
integer_list = ["user_input1"]

def user_input2():
	"""Input prompt"""
	user_input2 = input("Please input 3 positive integers one at a time")
	print(f"{user_input2}")
integer_list.append = ["user_input2"]

def user_input3():
	"""Input prompt"""
	user_input3 = input("Please input 3 positive integers one at a time")
	print(f"{user_input3}")
integer_list.append = ["user_input3"]

def user_input4():
	"""Input prompt"""
	user_input4 = input("Please input 3 positive integers one at a time")
	print(f"{user_input4}")
integer_list.append = ["user_input4"]


#In the end, the program asks the user for input X (integer) and outputs: "-1" if there were no such X among N read numbers, 
#or the index (from 1 to N) of this X if the user inputed it before.

def X_input():
	"""Input prompt"""
	X_input = input("Please input an integer X")
	
	if X_input in integer_list
		print("{X_input}".format(index))
	else
		print("-1")



########################################################################################



