### MSCS2202 HW8.2
### Yuxin Zhang

###The program asks the user for input N (positive integer) and reads it.
###Then the program asks the user to provide N (x, y) points (one by one) and reads all of them: first: x value, then: y value for every point one by one. 
###X is treated as the ground truth (correct) class label and Y is treated as the predicted class. Both X and Y are either 0 or 1.
###In the end, the program outputs: the Precision and Recall based on the inputs.The basic functionality of data processing (data initialization, data insertion), 
###should be done using Numpy library while the computation (ML) part should be done using Scikit-learn library as much as possible 
###(note: you can combine with what you've done from the previous tasks).

import numpy as np
from sklearn.metrics import precision_score, recall_score

def main():
	N = int(input("How many data points would you set: "))
		
	X = np.zeros(N)
	Y = np.zeros(N)
	
	for i in range(N):
		X[i] = int(input(f"Enter either 0 or 1 for X (correct) values for point {i+1}: "))
		Y[i] = int(input(f"Enter either 0 or 1 for Y (predicted) values for point {i+1}: "))

	precision = precision_score(X, Y)
	recall = recall_score(X, Y)

	print(f"Precision: {precision:.2f}")
	print(f"Recall: {recall:.2f}")

if __name__ == "__main__":
	main()


