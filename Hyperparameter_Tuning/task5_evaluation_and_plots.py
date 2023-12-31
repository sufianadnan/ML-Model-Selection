import pandas as pd
import numpy as np
import json
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import seaborn as sns

# Load samples.csv into a data frame object
samples = pd.read_csv("samples.csv")

# Add another label called "target" to encode labels 0 as benignware and 1 as malware
samples['target'] = np.where(samples['label'] == 'benignware', 0, 1)

# Open the "detector.log" file and read all lines into a list
with open("detector_pkl.log") as f:
    lines = f.readlines()

# Convert the list of JSON objects into simple strings for further processing
json_strings = [json.loads(line.strip()) for line in lines]

# Create the true and prediction vectors by reading the classification from the log generated by live classification
y_true = samples['target'].values
y_pred = []
for json_string in json_strings:
    if 'malware' in str(json_string):
        y_pred.append(1)
    else:
        y_pred.append(0)

# Print the classification report
classification_report = metrics.classification_report(y_true, y_pred)
print(classification_report)

# Calculate the ROC curve and AUC
fpr, tpr, thresholds = metrics.roc_curve(y_true, y_pred)
roc_auc = metrics.auc(fpr, tpr)

# Create and display the ROC curve
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, 'b', label='AUC = %0.2f' % roc_auc)
plt.legend(loc='lower right')
plt.plot([0, 1], [0, 1], 'r--')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.title('ROC Curve')
plt.show()

# Generate and display the confusion matrix as an image
confusion_mat = confusion_matrix(y_true, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(confusion_mat, annot=True, fmt="d", cmap="Blues")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()
