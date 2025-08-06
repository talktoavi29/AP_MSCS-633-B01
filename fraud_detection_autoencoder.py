import pandas as pd
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from pyod.models.auto_encoder import AutoEncoder
import pyod
import matplotlib.pyplot as plt

print(f"Using PyOD version: {pyod.__version__}")

#Load the dataset
data = pd.read_csv("data/creditcard.csv")
print("Dataset loaded successfully.")
print(f"Shape: {data.shape}")

#Split features and label
X = data.drop("Class", axis=1)
y = data["Class"]

#Normalize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

#Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

#Initialize and train AutoEncoder

clf = AutoEncoder(
    contamination=0.005,
    epoch_num=30,
    batch_size=128,
    # hidden_neuron_list=[64, 32],
    hidden_neuron_list=[30, 16, 8, 16, 30],
    dropout_rate=0.1,
    batch_norm=True,
    random_state=42,
    verbose=1
)

clf.fit(X_train)

print("Model training complete.")

# Predict
y_test_scores = clf.decision_function(X_test)  # anomaly scores
y_test_pred = clf.predict(X_test)  # 0: inlier, 1: outlier

# Evaluation
print("\nClassification Report:")
print(classification_report(y_test, y_test_pred))

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_test_pred))


plt.hist(y_test_scores, bins=50)
plt.title("Anomaly Score Distribution")
plt.xlabel("Anomaly Score")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()