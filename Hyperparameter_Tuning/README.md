# Hyperparameter Tuning

This project focuses on hyperparameter tuning for a machine learning model. It involves optimizing the hyperparameters of a Support Vector Classifier (SVC) using cross-validation. Below, I provide an overview of the project and describe each task in detail.

## Project Overview

In this project, I aim to fine-tune the hyperparameters of an SVC to achieve the best possible performance. I use a reduced dataset for training and evaluation and apply cross-validation to select the optimal hyperparameters. The tasks involved in this project are designed to explore and evaluate different hyperparameter settings for the SVC.

## Included Datasets

- `dataset.csv`: The original dataset, which served as the foundation for our analysis.
- `reduceddataset.csv`: This dataset is used for model training, and it excludes samples selected for testing in later stages of the project.
- `samples.csv`: A crucial dataset that contains a subset of samples used for testing. I use this dataset to assess the accuracy and effectiveness of our selected machine learning model.

** ALL CSV's are found in the Cross_Validation_Model Folderm this project is built on that dataset **

The inclusion of these datasets is fundamental to our project's success, as they play a pivotal role in our model selection and evaluation processes.

Now, let's delve into the details of our project and the tasks we've undertaken.

1. **Task 1: Feature Selection and Model Evaluation**

   - Loads the "reduceddataset.csv" and adds binary labels.
   - Performs feature selection using SelectKBest with chi2, selecting the top 15 features.
   - Creates a feature matrix (X) and a target vector (y).
   - Utilizes StratifiedKFold cross-validation with 10 folds to evaluate the model's performance.
   - Explores different hyperparameters for the Support Vector Classifier (SVC), including various kernel types and C values.
   - Calculates the cross-validation F1 score for each hyperparameter combination.
   - Prints the results, including the mean score and standard deviation.

2. **Task 2: Randomized Hyperparameter Tuning**

   - Loads the "reduceddataset.csv" and adds binary labels.
   - Performs feature selection using SelectKBest with chi2, selecting the top 15 features.
   - Creates a feature matrix (X) and a target vector (y).
   - Optimizes the Support Vector Classifier (SVC) through randomized hyperparameter tuning.
   - Explores different combinations of hyperparameters, including kernel types, C values, and tolerances.
   - Employs RandomizedSearchCV for the hyperparameter search.
   - Evaluates the models using the F1 score.
   - Prints the results, including the best score and parameters.

3. **Task 3: Grid Hyperparameter Tuning**

   - Loads the "reduceddataset.csv" and adds binary labels.
   - Performs feature selection using SelectKBest with chi2, selecting the top 15 features.
   - Creates a feature matrix (X) and a target vector (y).
   - Systematically explores various combinations of hyperparameters for the Support Vector Classifier (SVC).
   - The search space includes different kernel types, multiple C values, and different tolerance values.
   - Utilizes GridSearchCV for the hyperparameter search.
   - Assesses the models based on the F1 score.
   - Prints the results, including the best score and parameters.

4. **Task 4: Train and Save Model**

   - Loads "reduceddataset.csv" and extracts features using SelectKBest with chi2, selecting the top 15 features.
   - Creates a feature matrix (X) and a target vector (y).
   - Configures an optimized Support Vector Classifier (SVC) model with specific hyperparameters.
   - Trains the model using the selected features.
   - Saves the trained model to a file named "saved_detector.pkl" using the pickle module.

5. **Task 5: Model Evaluation and Plots**
   - Loads the "samples.csv" file, which contains a subset of samples used for testing.
   - Encodes the labels as "benignware" (0) and "malware" (1).
   - Reads the "detector.log" file generated during live classification to obtain classification results.
   - Calculates the classification report, including precision, recall, and F1-score.
   - Generates the Receiver Operating Characteristic (ROC) curve to visualize the model's ability to distinguish between benignware and malware.
   - Calculates the Area Under the Curve (AUC) as a performance measure.
   - Creates a confusion matrix as an image to display true positives, true negatives, false positives, and false negatives.
   - Displays the results and plots to assess the model's performance on the test dataset.

## Repository Structure

The repository is organized into separate Python scripts for each task, following the instructions provided in the project document. Here is a breakdown of the files and their purposes:

- `task1_Hyperparameter_Tuning_Exploration.py`: Script for Task 1, which explores hyperparameter tuning for different machine learning models.

- `task2_Randomized_Hyperparameter_Tuning.py`: Script for Task 2, which performs feature selection and cross-validation using different methods and explores randomized hyperparameter tuning for an SVM model.
- `task3_Grid_Hyperparameter_Tuning.py`: Script for Task 3, which performs feature selection and cross-validation using different methods and explores grid-search hyperparameter

- `task4_Train_and_Save_Model.py`: Script for Task 4, trains a pkl file for live classification.

- `task5_evaluation_and_plots.py`: Script for Task 5, which evaluates the model's performance on test data and generates classification reports and plots.

- `README.md`: This README file.

## Running the Code

To run the code for each task, and make sure to install the required Python packages `pip install matplotlib numpy pandas sklearn`. You can execute the Python scripts individually for each task.
