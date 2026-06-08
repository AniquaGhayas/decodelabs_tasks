# 🤖 Project 2: Data Classification Using AI

A supervised machine learning project that classifies Iris flower species using the **K-Nearest Neighbors (KNN)** algorithm. Built as part of the DecodeLabs AI Engineering internship track.

---

## Overview

This project demonstrates the **full supervised learning pipeline** — from raw data to model evaluation. Instead of writing rules manually (like Project 1), the machine learns patterns from labeled examples and predicts the species of unseen flowers on its own.

**Dataset:** Iris Benchmark (built into scikit-learn)  
**Algorithm:** K-Nearest Neighbors (KNN, K=5)  
**Task:** Multi-class classification (3 species)  
**Expected Accuracy:** ~96–100%

---

## Project Structure

```
project2-classification/
│
├── classification.py        ← Main script (the professional version)
├── confusion_matrix.png     ← Generated after running the script
├── k_optimization.png       ← Generated after running the script
└── README.md                ← This file
```

---

## Concepts Covered

| Concept | What It Does |
|---|---|
| **Supervised Learning** | Machine learns from labeled examples |
| **Iris Dataset** | 150 flowers × 4 measurements × 3 species |
| **Train-Test Split** | 80% train / 20% test — prevents cheating |
| **Feature Scaling** | StandardScaler — balances feature ranges |
| **KNN Algorithm** | Classifies by majority vote of K nearest neighbors |
| **Confusion Matrix** | Shows exactly where the model makes mistakes |
| **F1 Score** | Balanced metric — better than raw accuracy alone |
| **Elbow Method** | Finds the optimal value of K |

---

## Requirements

- Python 3.8 or higher
- pip (Python package manager)

**Libraries used:**

```
numpy
pandas
matplotlib
seaborn
scikit-learn
```

---

## Installation

**Step 1 — Clone or download the project files into a folder.**

**Step 2 — Open your terminal in that folder and install dependencies:**

```bash
pip install numpy pandas matplotlib seaborn scikit-learn
```

**Step 3 — Verify installation:**

```bash
python -c "import sklearn; print('scikit-learn version:', sklearn.__version__)"
```

You should see a version number printed (e.g., `scikit-learn version: 1.3.0`).

---

## Usage

Run the main script from your terminal:

```bash
python classification.py
```

The script will automatically:
1. Load and display the Iris dataset
2. Split into training and test sets
3. Scale the features
4. Train a KNN model with K=5
5. Print accuracy, F1 score, and a classification report
6. Display and save a confusion matrix heatmap
7. Plot error rate vs. K value to find the optimal K
8. Predict the species of a custom new flower

---

## Understanding the Output

### Terminal Output

```
==================================================
IRIS DATASET OVERVIEW
==================================================
   sepal length (cm)  sepal width (cm)  ...  species
0                5.1               3.5  ...   setosa
...

Shape: (150, 5)
Class Distribution:
  setosa        50
  versicolor    50
  virginica     50

Training set size: 120
Test set size: 30

==================================================
MODEL PERFORMANCE
==================================================
Accuracy:  100.00%
F1 Score:  1.0000

Detailed Classification Report:
              precision    recall  f1-score   support
      setosa       1.00      1.00      1.00        10
  versicolor       1.00      1.00      1.00        10
   virginica       1.00      1.00      1.00        10
```

### Classification Report — What Each Column Means

| Column | Meaning | When to prioritize |
|---|---|---|
| **Precision** | Of all predicted positives, how many were correct? | When false alarms are costly (spam filters) |
| **Recall** | Of all actual positives, how many did you catch? | When missing cases is dangerous (medical diagnosis) |
| **F1-Score** | Harmonic mean of precision and recall | When you need a balanced single metric |
| **Support** | Number of actual samples in that class | For context — ensures classes are balanced |

### Confusion Matrix

The heatmap saved as `confusion_matrix.png` shows:

```
                Predicted Setosa  Predicted Versicolor  Predicted Virginica
Actual Setosa        TP                  FP                    FP
Actual Versicolor    FP                  TP                    FP
Actual Virginica     FP                  FP                    TP
```

- **Diagonal cells** (top-left to bottom-right) = correct predictions
- **Off-diagonal cells** = mistakes — darker means more errors there

### K Optimization Chart

The chart saved as `k_optimization.png` shows error rate for K=1 through K=20.  
- **Too low K** (K=1): overfitting — memorizes noise
- **Too high K** (K=20): underfitting — too generic
- **The elbow point**: lowest error rate — this is your best K

---

## File Outputs

| File | Description |
|---|---|
| `confusion_matrix.png` | Heatmap showing model predictions vs actual labels |
| `k_optimization.png` | Line chart of error rate across different K values |

Both files are saved in the same directory as the script.

---

## How to Customize

### Change the test size split

```python
# Default is 80/20 — change test_size to adjust
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.3,   # ← change to 0.3 for 70/30 split
    random_state=42
)
```

### Change the value of K

```python
# Default is 5 — experiment with different values
model = KNeighborsClassifier(n_neighbors=7)  # ← change K here
```

### Predict a different flower

```python
# Change these 4 values: [sepal_length, sepal_width, petal_length, petal_width]
new_flower = np.array([[6.3, 2.5, 5.0, 1.9]])  # ← your custom flower
```

### Try a different algorithm (same 3-step pattern)

```python
# Decision Tree — swap in without changing anything else
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()

# Random Forest
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=100)

# Support Vector Machine
from sklearn.svm import SVC
model = SVC()
```

The `.fit()` and `.predict()` calls stay exactly the same — this is the power of scikit-learn's unified API.

---

## Pipeline Summary

```
RAW DATA (Iris Dataset: 150 samples)
         ↓
   EXPLORE DATA
   (shape, class distribution, statistics)
         ↓
   SHUFFLE + SPLIT
   ┌─────────────┐     ┌──────────┐
   │  Train (80%)│     │ Test(20%)│ ← locked, not touched until final eval
   └──────┬──────┘     └────┬─────┘
          ↓                  ↓
   StandardScaler        .transform()
   .fit_transform()      (no fitting!)
          ↓
   KNN (K=5)
   .fit(X_train, y_train)
          ↓
   .predict(X_test)
          ↓
   EVALUATE
   ├── Accuracy Score
   ├── Classification Report (Precision / Recall / F1)
   └── Confusion Matrix Heatmap
         ↓
   OPTIMIZE
   └── Elbow Method → find best K
         ↓
   PREDICT NEW DATA
   └── Custom flower → predicted species + confidence %
```

---

## Key Rule to Remember

> **Always fit the scaler on training data only, then use it to transform both sets.**  
> Fitting on test data would leak future information into your model — this is called *data leakage* and gives artificially inflated results that won't hold in the real world.

```python
# ✅ CORRECT
scaler.fit_transform(X_train)   # fit + transform on train
scaler.transform(X_test)        # only transform on test

# ❌ WRONG — never do this
scaler.fit_transform(X_test)    # leaks test information
```

---

## Built With

- [scikit-learn](https://scikit-learn.org/) — ML algorithms and dataset
- [pandas](https://pandas.pydata.org/) — Data manipulation
- [matplotlib](https://matplotlib.org/) — Plotting
- [seaborn](https://seaborn.pydata.org/) — Heatmap visualization
- [numpy](https://numpy.org/) — Numerical operations

---