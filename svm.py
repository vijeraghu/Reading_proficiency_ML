import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Load train data into a DataFrame
train_data = pd.read_csv("/content/training_dataset.csv")
train_data.dropna(subset=['Expression and Volume', 'Phrasing and Intonation', 'Smoothness', 'Pace'], inplace=True)

train_data.reset_index(drop=True, inplace=True)

test_data = pd.read_csv("/content/real_world_test.csv")
target_variables_train = train_data[['Expression and Volume', 'Phrasing and Intonation', 'Smoothness', 'Pace']]
target_variables_test = test_data[['Expression and Volume', 'Phrasing and Intonation', 'Smoothness', 'Pace']]

cols_to_drop = ['File Name']
train_data.drop(cols_to_drop, axis=1, inplace=True)
test_data.drop(cols_to_drop, axis=1, inplace=True)

mfcc_cols = [col for col in train_data.columns if col.startswith('MFCC')]
train_data[mfcc_cols] = train_data[mfcc_cols].fillna(method='ffill')
test_data[mfcc_cols] = test_data[mfcc_cols].fillna(method='ffill')

pitch_cols = [col for col in train_data.columns if col.startswith('Pitch')]
for col in pitch_cols:
    second_num = int(col.split('_')[2])
    prev_pitch_col = f'Pitch_mean_{second_num-1}'
    if prev_pitch_col in train_data.columns:
        train_data[col].fillna(train_data[prev_pitch_col], inplace=True)
        test_data[col].fillna(test_data[prev_pitch_col], inplace=True)
    else:
        train_data[col].fillna(0, inplace=True)
        test_data[col].fillna(0, inplace=True)

scaler = StandardScaler()
train_data_scaled = scaler.fit_transform(train_data)
test_data_scaled = scaler.transform(test_data)

train_data_scaled = pd.DataFrame(train_data_scaled, columns=train_data.columns)
test_data_scaled = pd.DataFrame(test_data_scaled, columns=test_data.columns)

target_variables = ['Expression and Volume', 'Phrasing and Intonation', 'Smoothness', 'Pace']

models={}

missing_train = train_data_scaled.isnull().sum()
missing_test = test_data_scaled.isnull().sum()

from sklearn.impute import SimpleImputer

# Impute missing values
imputer = SimpleImputer(strategy='mean')
train_data_scaled_imputed = pd.DataFrame(imputer.fit_transform(train_data_scaled), columns=train_data_scaled.columns)
test_data_scaled_imputed = pd.DataFrame(imputer.transform(test_data_scaled), columns=test_data_scaled.columns)

for target_variable in target_variables:

    # Extract target variable
    y_train = target_variables_train[target_variable]

    # Initialize SVM classifier
    svm = SVC(kernel='linear', random_state=0)

    # Train the classifier
    svm.fit(train_data_scaled_imputed, y_train)

    # Store the trained model
    models[target_variable] = svm
    y_pred = svm.predict(test_data_scaled_imputed)

    # Evaluate the model
    accuracy = accuracy_score(target_variables_test[target_variable], y_pred)
    print(f"Accuracy for {target_variable}: {accuracy}")
# Create a DataFrame to store predicted values
predicted_values_df = pd.DataFrame(index=test_data.index)

for target_variable in target_variables:

    y_pred = models[target_variable].predict(test_data_scaled_imputed)

    predicted_values_df[target_variable] = y_pred

from sklearn.metrics import f1_score, confusion_matrix

for target_variable in target_variables:
    y_pred = models[target_variable].predict(test_data_scaled_imputed)

    f1 = f1_score(target_variables_test[target_variable], y_pred, average='macro')

    cm = confusion_matrix(target_variables_test[target_variable], y_pred)

    print(f"F1 Score for {target_variable}: {f1}")


import matplotlib.pyplot as plt
import seaborn as sns

def plot_confusion_matrix(cm, target_variable, cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    """
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt="d", cmap=cmap)
    plt.title(f'Confusion Matrix for {target_variable}')
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.show()

# Plot confusion matrices
for target_variable in target_variables:
    y_pred = models[target_variable].predict(test_data_scaled_imputed)
    cm = confusion_matrix(target_variables_test[target_variable], y_pred)
    plot_confusion_matrix(cm, target_variable)