import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.svm import SVC
from sklearn.model_selection import StratifiedKFold, RandomizedSearchCV
# from sklearn.utils.fixes import loguniform
from scipy.stats import loguniform

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
cv = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)

model = SVC()

# Define search space
space = dict()
space['kernel'] = ["linear", "poly", "rbf", "sigmoid"]
space['C'] = loguniform(1e-5, 100)
space['tol'] = loguniform(1e-5, 100)

# Define search
search = RandomizedSearchCV(model, space, n_iter=500, scoring='f1', cv=cv)

# Execute search to fetch the results
search.fit(x_train, y_train)

# Print the best results
print("Random Search Results:")
print("Results:", search.cv_results_)
print("Best Score:", search.best_score_)
print("Best Parameters:", search.best_params_)
