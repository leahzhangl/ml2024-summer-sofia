### MSCS2202 HW8.2
### Yuxin Zhang

###The program asks the user for input N (positive integer) and reads it.
###Then the program asks the user to provide N (x, y) points (one by one) and reads all of them: first: x value, then: y value for every point one by one. 
###X is treated as the ground truth (correct) class label and Y is treated as the predicted class. Both X and Y are either 0 or 1.
###In the end, the program outputs: the Precision and Recall based on the inputs.The basic functionality of data processing (data initialization, data insertion), 
###should be done using Numpy library while the computation (ML) part should be done using Scikit-learn library as much as possible 
###(note: you can combine with what you've done from the previous tasks).

import numpy as np
from sklearn.neighbors import KNeighborsRegressor

def KNNregression(X, y, X_test, k):
	
	model = KNeighborsRegressor(n_neighbors=k)
	model.fit(X, y)
	Y_pred = model.predict([X_test])
	variance = np.var(y)
	
	return Y_pred[0], variance


def main():
	N = int(input("How many data points would you set: "))
	k = int(input("Which level of kNN would you use(number of neighbors): "))
	if k > N:
		return "Error: k should be less than or equal to N!"
			
	X = np.zeros((N, 2))
	y = np.zeros(N)
	
	for i in range(N):
		x, y[i] = map(float, input(f"Enter x and y values for point {i+1}: ").split())
		X[i] = [x, y[i]]
	

	X_test = list(map(float, input("Enter the test value X to predict its correlative Y: "))
	Y_pred, variance = KNNregression(X, y, X_test, k)

	print(f"The Y is  {Y_pred} ")
	print(f"The variance is {variance} ")
	
if __name__ == "__main__":
	main()
