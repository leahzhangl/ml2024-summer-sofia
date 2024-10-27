### MSCS2202
### HW4-2
### Yuxin Zhang

#The program asks the user for input N (positive integer) and reads it

def main():
	"""Input prompt"""
	N = int(input("Please input a positive integer N: "))
	print(f"{N}")

#Then the program asks the user to provide N numbers (one by one) and reads all of them (again, one by one)
	numbers = []
	
	for i in range(N):
		num = int(input(f"Enter number {i + 1}: "))
		print(f"{num}")
		numbers.append(num)

#In the end, the program asks the user for input X (integer) and outputs: "-1" if there were no such X among N read numbers, 
#or the index (from 1 to N) of this X if the user inputed it before.
	X = int(input("Enter the integer X to search for: "))
	
	if X in numbers:
		index = numbers.index(X) + 1
		print(f"{index}")
	else:
		print("-1")


########################################################################################



