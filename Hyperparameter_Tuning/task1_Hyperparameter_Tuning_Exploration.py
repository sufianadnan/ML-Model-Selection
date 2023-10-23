import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.svm import SVC
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.metrics import make_scorer, f1_score

# Load the data
data = pd.read_csv("reduceddataset.csv")

# Add the 'label' column with binary labels
data["Target"] = np.where(data["label"] == "benignware", 0, 1)

# Create a feature DataFrame without label information
features = data.drop(columns=['MD5', 'label', 'Target'])
class_distribution = data['label'].value_counts()
print(class_distribution)

# Select features using SelectKBest with chi2 and k=15
selector = SelectKBest(chi2, k=15)
selected_features = selector.fit_transform(features, data['label'])

# Get the list of selected features
selected_feature_indices = selector.get_support(indices=True)
selected_feature_names = features.columns[selected_feature_indices]

# Set the values for x_train and y_train
x_train = selected_features
y_train = data['Target']
# Create a cross-validation object
cv = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)

# Define space search
kernels = ['linear', 'poly', 'rbf', 'sigmoid']
c_values = [100, 10, 1.0, 0.1, 0.001]
# Calculate and print the cross-validation F1 score for each scenario
for kernel in kernels:
    for C in c_values:
        model = SVC(kernel=kernel, C=C)
        scores = cross_val_score(model, x_train, y_train, cv=cv, scoring='f1')
        print(f"Kernel: {kernel}, C: {C}")
        print("Cross-validation F1 Scores:", scores)
        print("Mean Score:", np.mean(scores))
        print("Standard Deviation:", np.std(scores))
        print("----------------------------")
