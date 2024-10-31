### MSCS2202
### Yuxin Zhang
### HW5.2

#Create the functionality outside of the main running code: 
#i.e., create the module with the Class described in the item above, and name this module "module5_mod.py" + 

class Integer():
	def __init__(self):
		self.numbers = []
		
	def inputnumbers(self, N):
		for i in range(N):
			num = int(input(f"Enter number {i + 1}: "))
			self.numbers.append(num)
			
	def findindex(self, X): 
		if X in self.numbers:
			index = self.numbers.index(X) + 1
			print(f"{index}")
		else:
			print("-1")

#create the main program "module5_call.py" that uses the Class description from the "*_mod" file.
