import pickle
import os
import subprocess
import re
import numpy
import json
import datetime
import time
import pandas as pd

# Read reduceddataset.csv file
data = pd.read_csv('reduceddataset.csv')

# Extract feature names from the dataset
data = data.drop(['MD5', 'label', 'Target'], axis=1)
feature_names = data.columns.tolist()

# Save the feature names to a file
with open("feature_names.pkl", "wb") as f:
    pickle.dump(feature_names, f)

# Load the classifier and feature selector
with open("saved_detector.pkl", "rb") as f:
    clf, feature_selector = pickle.load(f)

# Get the indices of the selected features
selected_features_indices = feature_selector.get_support(indices=True)

# Load the original feature names
with open("feature_names.pkl", "rb") as f:
    all_feature_names = pickle.load(f)

# Extract selected feature names
selected_features = [all_feature_names[i] for i in selected_features_indices]

basepath = "/home/user/Desktop/samples/"

# Function to remove ANSI escape sequences from a string
def remove_escape_sequences(text):
    ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
    return ansi_escape.sub('', text)

while True:
    try:
        # Enumerate the files in the folder
        for basename in os.listdir(basepath):
            if os.path.isfile(os.path.join(basepath, basename)):
                fullpathname = os.path.join(basepath, basename)

                # Calculate the md5
                process = subprocess.run(["md5sum", fullpathname], check=True, stdout=subprocess.PIPE, universal_newlines=True)
                output = process.stdout
                md5hash = output.split()[0].strip()

                # Creates timestamp
                currenttime = datetime.datetime.now()
                timestamp = json.dumps(currenttime.isoformat())
                logMessage = "{ \"timestamp\": "+ timestamp + ", \"md5\": \""+ md5hash +"\""

                print("Processing file:", fullpathname)

                try:
                    process = subprocess.run(["capa", "-v", fullpathname], check=True, capture_output=True, universal_newlines=True)
                    sections = process.stdout.split('\n\n', 1)[1]
                    present_in_file = list()

                    # Scan to see which features are present in the file
                    for section in sections.split('\n\n'):
                        line = section.split('\n')[0]
                        if line != '':
                            # Remove ANSI escape sequences and add to the list
                            present_in_file.append(remove_escape_sequences(re.split(r'\(\d', line)[0].strip()))

                    print("Features present in file:", present_in_file)

                    # Create the vector to predict the file
                    X = numpy.zeros(len(selected_features))
                    for i, feature in enumerate(selected_features):
                        X[i] = 1 if feature in present_in_file else 0

                    X = X.reshape(1, -1)

                    # Call the classifier
                    prediction = clf.predict(X)

                    if prediction:
                        logMessage = logMessage + ", \"classification\": \"malware\" }"
                    else:
                        logMessage = logMessage + ", \"classification\": \"benignware\" }"

                    print("Classification result for", fullpathname, ":", "Malware" if prediction else "Benignware")

                except KeyboardInterrupt:
                    logMessage = logMessage + ", \"classification\": \"ND\" } "
                except Exception as e:
                    print("Error:", e)
                    logMessage = logMessage + ", \"classification\": \"ND\" } "

                os.remove(fullpathname)
                if os.path.isfile(fullpathname + ".viv"):
                    os.remove(fullpathname + ".viv")


                with open("detector2.log", "a") as f:
                    f.write(json.dumps(logMessage) + "\n")

        print("Waiting for the next iteration...")
        time.sleep(5)
    except KeyboardInterrupt:
        exit(0)


