# Reading_proficiency_ML
The model leverages support vector machines (SVM) to predict key aspects of reading proficiency: Expression and Volume, Phrasing and Intonation, Smoothness, and Pace. Here's a summary of the process:

# Key Steps:
# Feature Extraction:

Audio data is processed using the Librosa and Parselmouth libraries to extract MFCCs (Mel-frequency cepstral coefficients) and pitch features.
For each second of audio, MFCCs, and pitch means/standard deviations are extracted to capture the audio's acoustic characteristics.
These extracted features are used to build a dataset for model training and evaluation.
# Data Processing:

The input data is read from Excel and CSV files. Audio files corresponding to each row are processed to extract features, which are then flattened and stored as new columns in a Pandas DataFrame.
This data frame serves as the training/testing data for the machine learning models.
# Data Cleaning and Imputation:

Missing values in the feature columns are filled either through forward filling or by using previously available pitch values.
A SimpleImputer is employed to handle any remaining missing data by imputing mean values.
# Model Training:

SVM classifiers are trained for each of the four target variables (Expression and Volume, Phrasing and Intonation, Smoothness, and Pace).
The features from the training dataset are scaled using StandardScaler to standardize the input for SVM.
The models are stored in a dictionary for later evaluation.
# Model Evaluation:

Predictions are made on the test dataset using the trained SVM models.
Accuracy scores are calculated for each target variable, comparing the predicted values to the ground truth labels from the test set.
F1 scores and confusion matrices can be used to evaluate the performance of each model further.
# Additional Notes:
The LibriSpeech ASR corpus serves as the data source, which provides a large variety of speech samples with diverse accents and reading styles, allowing the model to generalize well to real-world data.
The model achieves notable accuracy, with F1 scores validating its ability to predict reading proficiency across different levels.
This approach provides a scalable solution for evaluating reading proficiency based on real-world speech data, potentially supporting personalized learning and reading development across diverse demographics.
