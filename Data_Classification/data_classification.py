import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    accuracy_score, 
    classification_report, 
    confusion_matrix, 
    f1_score)

# ─────────────────────────────────────────
# INPUT — Load & Explore Data
# ─────────────────────────────────────────

iris = load_iris()
X = iris.data
y = iris.target
feature_names = iris.feature_names
class_names = iris.target_names

# Convert to DataFrame for easier viewing
df = pd.DataFrame(X, columns=feature_names)
df['species'] = [class_names[i] for i in y]

print("=" * 50)
print("IRIS DATASET OVERVIEW")
print("=" * 50)
print(df.head(10))
print(f"\nShape: {df.shape}")
print(f"\nClass Distribution:\n{df['species'].value_counts()}")
print(f"\nBasic Statistics:\n{df.describe()}")

# ─────────────────────────────────────────
# PROCESS — Split, Scale, Train
# ─────────────────────────────────────────

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    shuffle=True,
    stratify=y  # Ensures balanced class distribution in both sets
)

print(f"\nTraining set size: {X_train.shape[0]}")
print(f"Test set size: {X_test.shape[0]}")

# Scale
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train with K=5
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train_scaled, y_train)

# ─────────────────────────────────────────
# Evaluate & Visualize
# ─────────────────────────────────────────

predictions = model.predict(X_test_scaled)

# Accuracy
accuracy = accuracy_score(y_test, predictions)
f1 = f1_score(y_test, predictions, average='weighted')

print("\n" + "=" * 50)
print("MODEL PERFORMANCE")
print("=" * 50)
print(f"Accuracy:  {accuracy * 100:.2f}%")
print(f"F1 Score:  {f1:.4f}")

print("\nDetailed Classification Report:")
print(classification_report(y_test, predictions, target_names=class_names))

# Confusion Matrix Visualization
cm = confusion_matrix(y_test, predictions)
plt.figure(figsize=(8, 6))
sns.heatmap(
    cm,
    annot=True,
    fmt='d',
    cmap='Blues',
    xticklabels=class_names,
    yticklabels=class_names
)
plt.title('Confusion Matrix')
plt.ylabel('Actual Label')
plt.xlabel('Predicted Label')
plt.tight_layout()
plt.savefig('confusion_matrix.png')
plt.show()

# Find Optimal K (The Elbow Method)
print("\nFinding optimal K...")
error_rates = []
k_range = range(1, 21)

for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train_scaled, y_train)
    preds = knn.predict(X_test_scaled)
    error_rates.append(1 - accuracy_score(y_test, preds))

plt.figure(figsize=(10, 5))
plt.plot(k_range, error_rates, 'bo-', markersize=8)
plt.title('Error Rate vs K Value')
plt.xlabel('K (Number of Neighbors)')
plt.ylabel('Error Rate')
plt.xticks(k_range)
plt.grid(True)
plt.savefig('k_optimization.png')
plt.show()

best_k = k_range[error_rates.index(min(error_rates))]
print(f"Best K: {best_k} with error rate: {min(error_rates):.4f}")

# Predict on a brand new flower
print("\n" + "=" * 50)
print("PREDICTING A NEW FLOWER")
print("=" * 50)

new_flower = np.array([[5.1, 3.5, 1.4, 0.2]])  # Your input values
new_flower_scaled = scaler.transform(new_flower)
prediction = model.predict(new_flower_scaled)
probability = model.predict_proba(new_flower_scaled)

print(f"Measurements: Sepal L={new_flower[0][0]}, W={new_flower[0][1]}, "
      f"Petal L={new_flower[0][2]}, W={new_flower[0][3]}")
print(f"Predicted Species: {class_names[prediction[0]]}")
print(f"Confidence: {probability[0][prediction[0]] * 100:.1f}%")