import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.feature_selection import SelectPercentile, chi2
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import BernoulliNB
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline

# Read the data from "reduceddataset.csv" into a data frame
df = pd.read_csv("reduceddataset.csv")

# Extract the features only by dropping the MD5 hash, label, and target columns
X = df.drop(["MD5", "label", "Target"], axis=1)

# Extract the target variable
y = df["Target"]

# Create an instance of the StratifiedKFold class with 10 folds
kfold = StratifiedKFold(n_splits=10, shuffle=True)

# Create a SelectPercentile instance with chi2 scoring function and k=10
chi_filter = SelectPercentile(chi2, percentile=10)

# Create a list of pipelines for each model
pipelines = [
    Pipeline([
        ('feature_selection', chi_filter),
        ('classification', SVC(kernel='linear'))
    ]),
    Pipeline([
        ('feature_selection', chi_filter),
        ('classification', DecisionTreeClassifier())
    ]),
    Pipeline([
        ('feature_selection', chi_filter),
        ('classification', RandomForestClassifier())
    ]),
    Pipeline([
        ('feature_selection', chi_filter),
        ('classification', BernoulliNB())
    ])
]

# Create a list of model names
model_names = ['SVC', 'Decision Tree', 'Random Forest', 'Bernoulli Naive Bayes']

# Create an empty list to store the scores for each model
scores = []

# Loop over the pipelines and perform cross-validation on each one
for pipeline, model_name in zip(pipelines, model_names):
    score = cross_val_score(pipeline, X, y, cv=kfold)
    scores.append(score)
    print(model_name, "scores:", score)
    print(model_name, "mean score:", score.mean())
    print(model_name, "std score:", score.std())
    print()

# Create a boxplot to compare the scores for each model
plt.boxplot(scores, labels=model_names)
plt.ylim(0, 1)
plt.title("Model Selection using Cross-validation")
plt.show()
