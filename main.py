# importing libraries
import numpy as np
from sklearn.model_selection import LeaveOneOut

# creating the data
X = np.array([[1, 2], [3, 4]])
y = np.array([1, 2])

# Independent variable
print("\nIndependent variable :")
print(X)

# Dependent variable
print("\nDependent variable :")
print(y)

# creating the leav one out function
loo = LeaveOneOut()
loo.get_n_splits(X)

# printing the training and validation data
for train_index, test_index in loo.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    
print("\ntraining set:", X_train, y_train)
print("\nvalidation set :", X_test, y_test)


## NOTE: you can try out other validation techniques as well in this live coding window