import pandas as pd
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.svm import SVC
import pickle
# Load the data
df = pd.read_csv('reduceddataset.csv')

# Extract features
X = df.drop(['MD5', 'label', 'Target'], axis=1)
y = df['Target']

kbest = SelectKBest(chi2, k=15)
X_selected = kbest.fit_transform(X, y)

classifier = SVC(kernel='rbf', C=0.5, tol=1e-06)
classifier.fit(X_selected, y)

# Persist the SVC model
with open("saved_detector.pkl", "wb") as f:
    pickle.dump((classifier, kbest), f)
