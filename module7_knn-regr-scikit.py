### MSCS2202
### HW7.2
### Yuxin Zhang

#The program asks the user for input N (positive integer) and reads it.
#Then the program asks the user for input k (positive integer) and reads it.
#Then the program asks the user to provide N (x, y) points (one by one) and reads all of them: 
#first: x value, then: y value for every point one by one. X and Y are the real numbers.
#In the end, the program asks the user for input X and outputs: the result (Y) of k-NN Regression if k <= N, or any error message otherwise.
#Additionally, provide the variance of labels in the training dataset.
#The basic functionality of data processing (data initialization, data insertion), 
#should be done using Numpy library while the computation (ML) part should be done using Scikit-learn library as much as possible 
#(note: you can combine with what you've done from the previous task).

import numpy as np
from sklearn.neighbors import KNeighborsRegressor

def KNNregression(X, y, X_test, k):
	
	model = KNeighborsRegressor(n_neighbors=k)
	model.fit(X, y)
	Y_pred = model.predict([X_test])
	variance = np.var(y)
	
	return Y_pred[0], variance


if __name__ == "__main__":
	N = int(input("How many data points would you set: "))
	k = int(input("Which level of kNN would you use(number of neighbors): "))
	if k > N:
		return "Error: k should be less than or equal to N!"
			
	X = np.zeros((N, 2))
	y = np.zeros(N)
	
	for i in range(N):
		x, y[i] = map(float, input(f"Enter x and y values for point {i+1}: ").split())
		X[i] = [x, y[i]]
	

	X_test = float(input("Enter the test value X to predict its correlative Y: "))
	Y_pred, variance = KNNregression(X, y, X_test, k)

	print(f"The Y is  {Y_pred} ")
	print(f"The variance is {variance} ")

