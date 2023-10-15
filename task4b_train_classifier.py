import pandas as pd
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.svm import SVC
import pickle


# Load the data
df = pd.read_csv('reduceddataset.csv')

# Extract features
X = df.drop(['MD5', 'label', 'Target'], axis=1)
y = df['Target']

# Feature selection using SelectKBest and chi2
kbest = SelectKBest(chi2, k=15)
X_selected = kbest.fit_transform(X, y)

# Train the classifier using SVC with linear kernel
classifier = SVC(kernel='linear')
classifier.fit(X_selected, y)

# Persist the SVC model
with open("saved_detector.pkl", "wb") as f:
    pickle.dump((classifier, kbest), f)
