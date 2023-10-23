import pandas as pd
import random

# Read the original dataset
original_dataset = pd.read_csv('dataset.csv')

# Randomly select 30 malware and 30 benign samples
random.seed(42)  # for reproducibility
malware_samples = random.sample(original_dataset[original_dataset['label'] == 'malware'].index.tolist(), 30)
benign_samples = random.sample(original_dataset[original_dataset['label'] == 'benignware'].index.tolist(), 30)

# Combine the selected samples
selected_samples = pd.concat([original_dataset.loc[malware_samples], original_dataset.loc[benign_samples]])

# Remove the selected samples from the original dataset
reduced_dataset = original_dataset.drop(selected_samples.index)

# Save the reduced dataset to "reduceddataset.csv"
reduced_dataset.to_csv('reduceddataset.csv', index=False)

# Create a file containing MD5 hash and labels of selected samples
selected_samples[['MD5', 'label']].to_csv('samples.csv', index=False)

# The selected samples are now in 'selected_samples' DataFrame
