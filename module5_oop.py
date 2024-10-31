### MSCS2202
### Yuxin Zhang
### HW5.2

#The basic functionality of data processing (data initialization, data insertion, data search) should be done via Object-Oriented Programming Paradigm (i.e. using Classes)
#The program asks the user for input N (positive integer) and reads it
#Then the program asks the user to provide N numbers (one by one) and reads all of them (again, one by one)
#In the end, the program asks the user for input X (integer) and outputs: "-1" if there were no such X among N read numbers, or the index (from 1 to N) of this X if the user inputted it before.

class Integer():
	def __init__(self):
		self.numbers = []
	def readnumbers(self, N):
		for i in range(N):
			num = int(input(f"Enter number {i + 1}: "))
			numbers.append(num)
	def findindex(Self, X): 
		if X in self.numbers:
			index = self.numbers.index(X) + 1\
			print(f"{index}")
		else:
			print("-1")

def main()
	M = NumM()
	N = int(input("Please input a positive integer N: "))
	M.readnumbers(N)
	X = int(input("Enter the integer X to search for: "))
	outcome = M.findindex
	print(outcome)


main()


