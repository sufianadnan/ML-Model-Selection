import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.feature_selection import SelectKBest, SelectPercentile, chi2, mutual_info_classif
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline

# Read the data from "reduceddataset.csv" into a pandas DataFrame object.
df = pd.read_csv("reduceddataset.csv")

# Add another label called "target" to encode labels as 0 and 1.
df["Target"] = np.where(df["label"] == "benignware", 0, 1)

# Extract the features only, i.e. by dropping the MD5 hash, label, and target columns.
X = df.drop(["MD5", "label", "Target"], axis=1)
y = df["Target"]

# Perform StratifiedKFold to split the data into 10 folds.
skf = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)

# Declare two lists, one to store the name of the method used and second to store the selected features.
titles = []
cases = []

# Perform the following selections one by one and append the results to the lists:
# a. SelectKBest Chi2
titles.append("SelectKBest Chi2")
cases.append(SelectKBest(chi2, k=15))

# b. SelectKBest Mutual info
titles.append("SelectKBest Mutual info")
cases.append(SelectKBest(mutual_info_classif, k=15))

# c. SelectPercentile Mutual info
titles.append("SelectPercentile Mutual info")
cases.append(SelectPercentile(mutual_info_classif, percentile=10))

# Add SelectPercentile with Chi2
titles.append("SelectPercentile Chi2")
cases.append(SelectPercentile(chi2, percentile=10))

# Use a for loop to iterate over the feature selection methods and calculate F1 scores.
for title, case in zip(titles, cases):
    pipeline = make_pipeline(case, SVC(kernel="linear"))
    scores = cross_val_score(pipeline, X, y, cv=skf, scoring="f1")
    print(f"{title}: {scores.mean():.3f} +/- {scores.std():.3f}")

# Calculate the mean and standard deviation of the F1 scores for the last feature selection method.
last_pipeline = make_pipeline(SelectPercentile(chi2, percentile=10), SVC(kernel="linear"))
f1_scores = cross_val_score(last_pipeline, X, y, cv=skf, scoring="f1")
print(f"Mean F1 score: {f1_scores.mean():.3f} +/- {f1_scores.std():.3f}")
