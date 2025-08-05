# fraud_detection_autoencoder.py

import pandas as pd
import matplotlib.pyplot as plt
from pyod.models.auto_encoder import AutoEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import numpy as np

# Load the dataset
data = pd.read_csv("data/creditcard.csv")
print("Dataset loaded successfully.")

# Prepare the features and labels
X = data.drop(columns=["Class"])
y = data["Class"]

# Normalize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Initialize AutoEncoder model
clf = AutoEncoder(hidden_neurons=[32, 16, 16, 32], epochs=30, batch_size=128, verbose=1)
clf.fit(X_train)

# Predict
y_test_scores = clf.decision_function(X_test)  # anomaly scores
y_test_pred = clf.predict(X_test)  # binary labels (0: inlier, 1: outlier)

# Evaluation
print("\nClassification Report:")
print(classification_report(y_test, y_test_pred))

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_test_pred))