### MSCS2202 
### HW9.2
### Yuxin Zhang

#The program asks the user for input N (positive integer) and reads it.
#Then the program asks the user to provide N (x, y) pairs (one by one) and reads all of them: first: x value, then: y value for every pair one by one. X is treated as the input feature and Y is treated as the class label. X is a real number, Y is a non-negative integer.
#This set of pairs constitutes the training set TrainS = {(x, y)_i}, i = 1..N.
#Then the program asks the user for input M (positive integer) and reads it.
#Then the program asks the user to provide M (x, y) pairs (one by one) and reads all of them: first: x value, then: y value for every pair one by one. X is treated as the input feature and Y is treated as the class label. X is a real number, Y is a non-negative integer.
#This set of pairs constitutes the test set TestS = {(x, y)_i}, i = 1..M.
#In the end, the program outputs: the best k for the kNN Classification method and the corresponding test accuracy. kNN Classifier should be trained on pairs from TrainS, tested on x values from TestS and compared with y values from TestS.
#The basic functionality of data processing (data initialization, data insertion), should be done using Numpy library while the computation (ML) part should be done using Scikit-learn library as much as possible (note: you can combine with what you've done from the previous tasks). 
#Note: you can try the following range of k: 1 <= k <= 10.


import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score

def main():
	N = int(input("How many training pairs would you set: "))
	TrainS = np.zeros(N, 2)
	for i in range(N):
		x = float(input(f"Enter real number for X(input feature) for training pair {i+1}: "))
		y = int(input(f"Enter non-negative integer for Y(class label) for training pair {i+1}: "))
		TrainS[i] = [x, y]

	M = int(input("How many test pairs would you set: "))
	TestS = np.zeros(N, 2)
	for i in range(M):
		j = float(input(f"Enter real number for X(input feature) for test pair {i+1}: "))
		k = int(input(f"Enter non-negative integer for Y(class label) for test pair {i+1}: "))
		TestS[i] = [j, k]
	
	param_grid = {'n_neighbors': range(1, 11)}
	grid_search = GridSearchCV(KNeighborsClassifier(), param_grid)
	grid_search.fit(x, y)
	print("Best parameters:", grid_search.best_params_)
	best_knn = grid_search.best_estimator_
	y_pred = best_knn.predict(j)
	test_accuracy = accuracy_score(k, y_pred)
	print("Test accuracy:", test_accuracy)

if __name__ == "__main__":
	main()
