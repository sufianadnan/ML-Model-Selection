import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.svm import SVC
from sklearn.model_selection import StratifiedKFold, GridSearchCV

# Load the data
data = pd.read_csv("reduceddataset.csv")

# Add the 'label' column with binary labels
data["Target"] = np.where(data["label"] == "benignware", 0, 1)

# Create a feature DataFrame without label information
features = data.drop(columns=['MD5', 'label', 'Target'])

# Select features using SelectKBest with chi2 and k=15
selector = SelectKBest(chi2, k=15)
selected_features = selector.fit_transform(features, data['label'])

# Set the values for x_train and y_train
x_train = selected_features
y_train = data['Target']

# Create a cross-validation object
cv = StratifiedKFold(n_splits=10)

# Create the SVC model object
model = SVC()

# Define search space
param_grid = {
    'kernel': ["linear", "poly", "rbf", "sigmoid"],
    'C': [0.001, 0.1, 1.0, 10, 100],
    'tol': [1e-5, 1e-4, 1e-3, 1e-2, 1e-1]
}

# Define search
search = GridSearchCV(model, param_grid, scoring='f1', cv=cv)

# Execute search to fetch the results
search.fit(x_train, y_train)

# Print the best results
print("Results:", search.cv_results_)
print("Best score:", search.best_score_)
print("Best parameters:", search.best_params_)
