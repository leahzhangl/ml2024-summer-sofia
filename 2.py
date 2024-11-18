import numpy as np
from sklearn.neighbors import KNeighborsRegressor

def knn_regression(X, y, new_x, k):
    """
    Performs k-NN regression.

    Args:
        X: Input features (N x 2 array).
        y: Target values (N x 1 array).
        new_x: New input for prediction (1 x 2 array).
        k: Number of neighbors.

    Returns:
        Predicted value.
    """

    if k > len(X):
        return "Error: k cannot be greater than the number of data points"

    knn_regressor = KNeighborsRegressor(n_neighbors=k)
    knn_regressor.fit(X, y)
    predicted_y = knn_regressor.predict([new_x])

    # Calculate variance of labels in the training dataset
    variance = np.var(y)

    return predicted_y[0], variance

if __name__ == "__main__":
    N = int(input("Enter the number of data points (N): "))
    k = int(input("Enter the number of neighbors (k): "))

    X = np.zeros((N, 2))
    y = np.zeros(N)

    for i in range(N):
        x, y[i] = map(float, input(f"Enter x and y values for point {i+1}: ").split())
        X[i] = [x, y[i]]

    new_x = list(map(float, input("Enter the new x value for prediction: ").split()))

    predicted_y, variance = knn_regression(X, y, new_x, k)

    print("Predicted y value:", predicted_y)
    print("Variance of labels in the training dataset:", variance)
