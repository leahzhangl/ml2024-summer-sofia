### MSCS2202
### Yuxin Zhang
### HW5.2

#Create the functionality outside of the main running code: 
#i.e., create the module with the Class described in the item above, and name this module "module5_mod.py" + 
#create the main program "module5_call.py" that uses the Class description from the "*_mod" file.

from module5_mod import Integer

def main():
	N = int(input("Please input a positive integer N: "))
	M = Integer()
	M.inputnumbers(N)
	
	X = int(input("Enter the integer X to search for: "))
	M.findindex(X)

if __name__ == "__main__":
	main()
