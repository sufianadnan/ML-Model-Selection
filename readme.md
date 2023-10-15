# Malware Machine Learning Model Selection and Evaluation

In this project, we focus on model selection and evaluation using cross-validation and apply machine learning techniques to classify malware and benignware samples.

## Project Overview

This Project involves several tasks, each of which contributes to the overall goal of selecting the best model for classification and evaluating its performance. The key tasks in this project include:

1. **Task 1: Split the Dataset**
   - Randomly select 30 malware samples and 30 benign samples from the dataset.
   - Create a file with MD5 hash and the true label of each sample.
   - Remove these selected samples from the full dataset.
   - Save the test samples to the Kali host.

2. **Task 2: Feature Selection using Cross-Validation**
   - Compare four different feature selection strategies using cross-validation.
   - Write a Python script to calculate the cross-validation F1 score for each strategy.
   - Calculate the mean and standard deviation of the scores.

3. **Task 3: Model Selection using Cross-Validation**
   - Compare four different models (Decision Tree, Random Forest, SVC, and BernoulliNB) with a chosen feature selection strategy.
   - Calculate the cross-validation F1 scores for each model and strategy.
   - Determine the best model based on the results.

4. **Task 4: Live Classification and Performance Evaluation**
   - Create scripts for live classification and performance evaluation using a selected model.
   - Move selected samples to a separate folder.
   - Train the classifier and save the model.
   - Run the model on live files and log the results.
   - Generate classification reports, confusion matrices, and ROC curves.

## Repository Structure

The repository is organized into separate Python scripts for each task, following the instructions provided in the project document. Here is a breakdown of the files and their purposes:

- `task1_split_dataset.py`: Script for Task 1, which splits the dataset into test and reduced datasets.

- `task2_feature_selection.py`: Script for Task 2, which performs feature selection and cross-validation using different methods.

- `task3_model_selection.py`: Script for Task 3, which selects the best model and performs cross-validation for each model.

- `task4a_move_samples.py`: Script for Task 4, part 1, which moves selected samples to a separate folder for live classification.

- `task4b_train_classifier.py`: Script for Task 4, part 2, which trains the classifier, saves the model, and prepares it for live classification.

- `live_classification.py`: Script for live classification, utilizing the saved model to classify live files.

- `task4c_evaluation_and_plots.py`: Script for Task 4, part 3, which evaluates the performance of the model on live files and generates classification reports and plots.

- `requirements.txt`: Lists the required Python packages for this project.

- `README.md`: This README file.

## Running the Code

To run the code for each task, follow the instructions in the project document, and make sure to install the required Python packages listed in `requirements.txt`. You can execute the Python scripts individually for each task.

