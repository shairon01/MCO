# Importing necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('creditcard.csv')

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(data.head())

# Number of rows and columns
print(f"\nDataset shape: {data.shape}")

# Data types of each column
print("\nData types:")
print(data.dtypes)

# Check for missing values
print("\nMissing values in each column:")
print(data.isnull().sum())

# Count of fraudulent vs non-fraudulent transactions
print("\nClass distribution:")
print(data['Class'].value_counts())

# Percentage of fraudulent and non-fraudulent transactions
fraud_percentage = data['Class'].value_counts(normalize=True) * 100
print("\nFraudulent and non-fraudulent transaction percentages:")
print(fraud_percentage)

# Visualizing class distribution
plt.figure(figsize=(8, 6))
sns.countplot(x='Class', data=data)
plt.title("Class Distribution")
plt.xlabel("Class")
plt.ylabel("Count")
plt.show()

# Calculate the correlation matrix
correlation_matrix = data.corr()

# Visualize the correlation matrix
plt.figure(figsize=(16, 10))
sns.heatmap(correlation_matrix, cmap='coolwarm', annot=False)
plt.title("Correlation Matrix")
plt.show()






















print(f"\nDataset shape: {data.shape}")
print("\nData types:")
print(data.dtypes)
print("\nMissing values in each column:")
print(data.isnull().sum())
print("\nClass distribution:")
print(data['Class'].value_counts())
fraud_percentage = data['Class'].value_counts(normalize=True) * 100
print("\nFraudulent and non-fraudulent transaction percentages:")
print(fraud_percentage)
plt.figure(figsize=(8, 6))
sns.countplot(x='Class', data=data)
plt.title("Class Distribution")
plt.xlabel("Class")
plt.ylabel("Count")
plt.show()
correlation_matrix = data.corr()
plt.figure(figsize=(16, 10))
sns.heatmap(correlation_matrix, cmap='coolwarm', annot=False)
plt.title("Correlation Matrix")
plt.show()
