# 📉 Telco Customer Churn Prediction

This project predicts customer churn for a telecom company using Machine Learning and visualizes insights using Tableau. It also includes a Flask API for real-time predictions and a structured SQL database design.

---

## 🚀 Project Overview

Customer churn occurs when customers stop using a company’s service. Reducing churn can significantly increase profitability.

In this project, I:

✅ Analyzed churn patterns  
✅ Built Machine Learning models  
✅ Applied SMOTE for class imbalance  
✅ Used AdaBoost as final model  
✅ Built Flask API  
✅ Created Tableau dashboards  
✅ Designed SQL schema + ER Diagram  

---

## 🧠 Machine Learning

Final Model: **AdaBoost + SMOTE**

| Metric | Score |
|------|------|
| Accuracy | **78%** |
| Precision (Churn) | **0.56** |
| Recall (Churn) | **0.74** |
| F1-score (Churn) | **0.64** |
| ROC-AUC | **0.75** |

Reason selected: Best balance between **recall** and **accuracy** for minority class (churn customers).

---

## 📊 Dashboards (Tableau)

### 1. Before ML (Exploratory)
- Total customers
- Churn %
- Monthly charges impact
- Contract type distribution
- Payment method

### 2. After ML (Prediction-Based)
- Predicted churn rate
- Risk segmentation
- **Top 10 high risk customers**
- **Revenue loss estimate**
- High risk segments

---

## 🌐 Flask API

Endpoint:

Accepts customer data and returns:

```json
{
  "churn_prediction": "Yes",
  "churn_probability": 0.82
}

cd flask_app
python app.py



