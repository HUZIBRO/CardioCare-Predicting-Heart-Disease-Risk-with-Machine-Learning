# ❤️ CardioCare: Predicting Heart Disease Risk with Machine Learning

## 📌 Short Description  
This project aims to develop a predictive model to identify individuals at risk of developing heart disease based on a range of clinical and behavioral health indicators. It demonstrates a complete classification workflow—from data exploration and visualization to model training and evaluation—while addressing real-world challenges such as imbalanced datasets.

---

## 📊 Project Overview  

This project highlights key data science and machine learning techniques through a health-focused classification problem. It involves in-depth data analytics, data visualization, feature selection, model building, and model performance evaluation.

---

## 🚀 Key Steps & Skills Demonstrated

### 📂 Data Loading & Exploration
- Load structured health data using `pandas`.
- Perform descriptive analysis (`.info()`, `.describe()`) to understand data distribution.
- Check for and summarize missing values.

### 🧹 Data Cleaning & Preparation
- Remove records with missing values to ensure dataset quality.
- Prepare features for model training.

### 📊 Data Visualization & EDA
- Visualize heart disease distribution by:
  - **Gender**
  - **Age Groups**
  - **BMI, Glucose, Heart Rate**
  - **Smoking Status**, **Diabetes**, **Cigarette Consumption**
- Tools used: `matplotlib`, `seaborn`

### 🔍 Feature Selection
- Use a **correlation matrix** to assess feature relevance.
- Select top predictors based on correlation with the target variable.

### ⚖️ Handling Imbalanced Data
- Apply **SMOTE (Synthetic Minority Over-sampling Technique)** to balance the dataset and improve model generalization.

### 🧠 Model Training
Two classification models are trained and compared:
- 🌲 **Random Forest Classifier**
- 📍 **K-Nearest Neighbors (KNN)**

### 📈 Model Evaluation
Models are evaluated using:
- **Accuracy Score**
- **Confusion Matrix**
- **Classification Report** (Precision, Recall, F1-Score)

---

## 📌 Data Science & ML Skills Demonstrated

- **Data Analysis & Wrangling:** `pandas`, `numpy`
- **Statistical Visualization:** `matplotlib`, `seaborn`
- **Exploratory Data Analysis (EDA)**
- **Feature Engineering and Selection**
- **Class Imbalance Handling:** SMOTE
- **Machine Learning Classification:** `scikit-learn` (Random Forest, KNN)
- **Model Performance Evaluation:** Classification Metrics & Diagnostic Plots

---

## 🧰 Tools & Technologies Used

- **Python 3.11**
- **Libraries:**
  - `pandas`, `numpy`
  - `matplotlib`, `seaborn`
  - `scikit-learn`
  - `imblearn` (for SMOTE)

---
