import numpy as np
from sklearn.neighbors import KNeighborsRegressor

# Step 1: Read input
N = int(input("Enter the number of points (N): "))  # Number of data points
k = int(input("Enter the value of k for k-NN: "))  # Number of nearest neighbors

# Ensure that k is less than or equal to N
if k > N:
    print("Error: k must be less than or equal to N.")
    exit()

# Read the N points (x, y)
X_data = []  # Will hold the x values
y_data = []  # Will hold the y values
for i in range(N):
    x = float(input(f"Enter the x value for point {i+1}: "))
    y = float(input(f"Enter the y value for point {i+1}: "))
    X_data.append([x])  # X must be 2D for scikit-learn (each point is a feature vector)
    y_data.append(y)

# Convert to numpy arrays for easier manipulation
X_data = np.array(X_data)
y_data = np.array(y_data)

# Step 2: Compute the variance of y values in the training dataset
variance_y = np.var(y_data)
print(f"Variance of the labels (y values): {variance_y}")

# Step 3: k-NN Regression
# Initialize the k-NN regressor
knn_regressor = KNeighborsRegressor(n_neighbors=k)

# Fit the model to the data
knn_regressor.fit(X_data, y_data)

# Step 4: Read the test point (X) and predict the corresponding Y
X_test = float(input("Enter the X value to predict Y: "))
y_pred = knn_regressor.predict([[X_test]])  # Predict expects a 2D array for a single test point

# Output the prediction
print(f"The predicted value of Y for X = {X_test} is: {y_pred[0]}")
