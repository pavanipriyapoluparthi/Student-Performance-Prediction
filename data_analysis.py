import pandas as pd

# Load the dataset
df = pd.read_csv("dataset/student_performance_50.csv")

# Display the first 5 students
print("First 5 students:")
print(df.head())

# Display number of rows and columns
print("\nDataset shape:")
print(df.shape)

# Display column names
print("\nColumn names:")
print(df.columns)

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Check for duplicate rows
print("\nDuplicate rows:")
print(df.duplicated().sum())

# Check data types
print("\nData types:")
print(df.dtypes)

# Basic statistics
print("\nBasic statistics:")
print(df.describe())

import matplotlib.pyplot as plt
import seaborn as sns

# Study hours vs final score
plt.figure(figsize=(7, 5))
sns.scatterplot(data=df, x="study_hours", y="final_score")
plt.title("Study Hours vs Final Score")
plt.xlabel("Study Hours")
plt.ylabel("Final Score")
plt.show()

# Attendance vs final score
plt.figure(figsize=(7, 5))
sns.scatterplot(data=df, x="attendance", y="final_score")
plt.title("Attendance vs Final Score")
plt.xlabel("Attendance (%)")
plt.ylabel("Final Score")
plt.show()

# Prepare data for Machine Learning

X = df[[
    "study_hours",
    "attendance",
    "assignment_score",
    "midterm_score",
    "sleep_hours"
]]

y = df["final_score"]

print("\nFeatures (X):")
print(X.head())

print("\nTarget (y):")
print(y.head())

print("\nX shape:")
print(X.shape)

print("\ny shape:")
print(y.shape) 

# Split data into training and testing sets

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining data:")
print("X_train shape:", X_train.shape)
print("y_train shape:", y_train.shape)

print("\nTesting data:")
print("X_test shape:", X_test.shape)
print("y_test shape:", y_test.shape)

 
# ==============================
# MACHINE LEARNING MODEL
# ==============================

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib

# Create the model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

print("\nModel training completed!")

# Make predictions on test data
y_pred = model.predict(X_test)

print("\nActual vs Predicted:")
for actual, predicted in zip(y_test, y_pred):
    print("Actual:", actual, "Predicted:", round(predicted, 2))

# Model evaluation
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation:")
print("Mean Absolute Error:", round(mae, 2))
print("Mean Squared Error:", round(mse, 2))
print("R2 Score:", round(r2, 2))

# Save the trained model
joblib.dump(model, "student_performance_model.pkl")

print("\nModel saved successfully!")                   























































