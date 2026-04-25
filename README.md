# 🚨 AI-Powered Anomaly Detection for Fraudulent System Activities

## 📌 Project Overview

This project focuses on detecting anomalies in network traffic using unsupervised machine learning techniques. The goal is to identify unusual patterns that may indicate potential cybersecurity threats.

Based on real-world IT experience, traditional rule-based monitoring systems are limited because they rely on predefined rules and cannot easily detect new or unknown attack patterns. This project applies machine learning models to automatically identify abnormal behavior without relying on labeled data.

---

## 🎯 Problem Statement

In cybersecurity, detecting new or evolving threats is challenging due to the lack of labeled data. This project addresses that problem by using unsupervised learning to detect anomalies in network traffic.

The objective is to identify unusual behavior that may represent security risks, while minimizing false alerts and improving detection efficiency.

---

## 📊 Dataset

* **Source:** Public cybersecurity network traffic dataset
* **Records:** 25,192
* **Features:** 42 columns (numerical and categorical)

### Feature Categories:

* Traffic metrics (e.g., `src_bytes`, `dst_bytes`)
* Connection features (e.g., `count`, `srv_count`)
* Login indicators (e.g., `num_failed_logins`)
* Network attributes (e.g., `protocol_type`, `service`, `flag`)

---

## 🧠 Models Used

This project compares three unsupervised learning models:

* **Isolation Forest** *(Final Model)*
* **K-Means Clustering**
* **DBSCAN**

### Approach Types:

* Isolation-based → Isolation Forest
* Distance-based → K-Means
* Density-based → DBSCAN

---

## ⚙️ Project Structure

```
your-capstone-project/
│
├── README.md
├── requirements.txt
│
├── notebooks/
│   ├── 01_EDA.ipynb
│   ├── 02_Feature_Engineering.ipynb
│   ├── 03_Modeling.ipynb
│   └── 04_Evaluation.ipynb
│
├── src/
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   └── model_training.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│   └── best_model.pkl
│
├── reports/
│   ├── technical_presentation.pdf
│   └── business_presentation.pdf
│
└── docs/
    └── data_dictionary.md
```

---

## 🚀 Key Highlights

* Built an anomaly detection system using real-world cybersecurity data
* Compared multiple unsupervised learning models
* Applied feature engineering using domain-based ratios
* Implemented feature selection using VarianceThreshold
* Performed bias auditing using subgroup anomaly rates
* Designed as a decision-support tool for IT systems

---

## 🔧 Installation Instructions

1. Clone the repository:

```
git clone https://github.com/your-username/your-capstone-project.git
cd your-capstone-project
```

2. Install dependencies:

```
pip install -r requirements.txt
```

---

## ▶️ How to Run the Project

Run the notebooks in order:

1. `01_EDA.ipynb` → Data understanding and visualization
2. `02_Feature_Engineering.ipynb` → Preprocessing and feature creation
3. `03_Modeling.ipynb` → Model training
4. `04_Evaluation.ipynb` → Model comparison and results

---

## 📈 Results Summary

* **Isolation Forest** was selected as the best-performing model
* It provided the most **consistent and stable anomaly detection**
* Anomalies are mainly driven by:

  * Unusual traffic volume
  * Abnormal connection patterns
  * Imbalanced feature ratios

Additional improvements:

* Feature selection to reduce noise
* PCA for visualization
* Subgroup bias analysis using `protocol_type`, `service`, and `flag`

---

## ⚖️ Ethical Considerations & Limitations

* No ground truth labels (unsupervised learning limitation)
* Possible false positives and false negatives
* Model sensitivity to parameter tuning
* Potential bias in system behavior patterns

This model is intended as a **decision-support tool**, not a fully automated decision system.

---

## 👤 Author

**Ryan Dale Maquidato**
System Developer (Insurance Industry)
Machine Learning Capstone Project

---

## 📌 Final Note

This project demonstrates how machine learning can be applied to real-world cybersecurity problems. It focuses not only on model performance but also on explainability, fairness, and responsible AI usage.
