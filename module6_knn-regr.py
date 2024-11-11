### MSCS2202
### HW6.2
### Yuxin Zhang

#The program asks the user for input N (positive integer) and reads it.
#Then the program asks the user for input k (positive integer) and reads it.
#Then the program asks the user to provide N (x, y) points (one by one) and reads all of them: 
#first: x value, then: y value for every point one by one. X and Y are the real numbers.
#In the end, the program asks the user for input X and outputs: the result (Y) of k-NN Regression if k <= N, or any error message otherwise.
#The basic functionality of data processing (data initialization, data insertion, data calculation) should be done using Numpy library as much as possible 
#(note: you can combine with OOP from the previous task).

import numpy as np

class KNNRegression:
	def __init__(self, N, k, points):
		self.N = N
		self.k = k
		self.points = np.array(points)
	
	def predict(self, X):
		if self.k > self.N:
			raise ValueError("k should be less than or equal to N")
		distances = np.abs(self.points[:, 0] - X)  
		sorted_indices = np.argsort(distances) 
		nearest_neighbors = self.points[sorted_indices[:self.k]]
		return np.mean(nearest_neighbors[:, 1])  

def main():
	N = int(input("How many data points would you set: "))
	k = int(input("Which level of kNN would you use(number of neighbors): "))
	if k > N:
		return "Error: k should be less than or equal to N!"
	
	points = []
	for i in range(N):
		x = float(input(f"Enter x value for point {i+1} : "))
		y = float(input(f"Enter y value for point {i+1} : "))
		points.append((x, y))
	
	model = KNNRegression(N, k, points)
	
	X = float(input("Enter the test value X to predict its correlative Y: "))
	Y = model.predict(X)
	print(f"The Y is  {Y} ")

if __name__ == "__main__":
	main()
