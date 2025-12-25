# Credit Card Fraud Detection System

An end-to-end machine learning project focused on detecting fraudulent financial transactions using exploratory data analysis, feature engineering, class imbalance handling, and classification models.

This project demonstrates a complete fraud detection workflow suitable for real-world financial datasets.

---

## 📌 Problem Statement
Financial fraud causes significant losses every year. The objective of this project is to build a machine learning model that can accurately identify fraudulent credit card transactions while handling highly imbalanced data.

---

## 📊 Dataset
- Source: Kaggle – Credit Card / Financial Transaction Fraud Dataset
- Size: ~145 MB (not uploaded due to GitHub file size limits)

### Dataset Access
Download the dataset from:
https://www.kaggle.com/datasets/kartik2112/fraud-detection

After downloading, place the file inside:

A small sample dataset is provided in:
to allow quick testing and reproducibility.

---

## 🧠 Project Workflow
1. Data Understanding & Cleaning  
2. Exploratory Data Analysis (EDA)  
3. Feature Engineering  
4. Handling Class Imbalance using SMOTE  
5. Model Training & Evaluation  
6. Model Selection based on Recall, Precision & ROC-AUC  

---

## 🔍 Exploratory Data Analysis (EDA)
Key insights explored:
- Fraud vs Non-Fraud distribution (high class imbalance)
- Transaction amount patterns
- Time-based fraud behavior (hour, night vs day, weekend)
- Category & merchant-level fraud risk
- Location-based fraud using customer–merchant distance

---

## ⚙️ Feature Engineering
Key engineered features:
- Transaction hour & night-time indicator
- Weekend flag
- Customer age (derived from DOB)
- Haversine distance between customer and merchant
- Log-transformed transaction amount
- City population bins

Removed non-informative or leakage-prone columns:
- Card numbers, transaction IDs, names, street details, raw timestamps

---

## 🤖 Model Building
Models used:
- Logistic Regression (baseline)
- Random Forest Classifier

### Class Imbalance Handling
- SMOTE applied **only on training data** to avoid data leakage

### Evaluation Metrics
- Recall (fraud class – primary metric)
- Precision
- F1-score
- ROC-AUC
- Confusion Matrix


---

## 🛠️ Tech Stack
- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn
- Imbalanced-learn (SMOTE)

---

## 🚀 Key Learnings
- Importance of handling imbalanced datasets correctly
- Avoiding data leakage in fraud detection
- Feature engineering plays a bigger role than model complexity
- Business-driven evaluation metrics matter more than accuracy

---

## 📌 Future Improvements
- Hyperparameter tuning
- Threshold optimization
- Model deployment using Streamlit or FastAPI
- Real-time fraud detection simulation

---

## 👤 Author

**Shivam Singh**
Aspiring Data Scientist | Machine Learning Enthusiast

🔗 GitHub: [https://github.com/shivamsingh-itds]
🔗 LinkedIn: [www.linkedin.com/in/shivamsinghds]

---

⭐ If you find this project helpful, feel free to star the repository!gi