<h1 align="center">Telecom Customer Churn Risk Analytics System</h1>

<p align="center">
<b>A Machine Learning–Driven Analytics System for Customer Churn Prediction</b><br>
End-to-end predictive analytics application designed to identify customers at risk of leaving a telecom service and support data-driven retention strategies.
</p>

---

## 1. Overview

The **Telecom Customer Churn Risk Analytics System** is an end-to-end machine learning–based predictive analytics application designed to identify customers who are likely to discontinue telecom services.

Customer churn is a critical business challenge in the telecom industry, directly impacting revenue and customer lifetime value.  
This system analyzes customer demographics, service usage patterns, contract details, and billing behavior to estimate churn probability and classify risk levels.

The solution integrates data preprocessing, feature engineering, supervised model training, evaluation, and an interactive Streamlit dashboard for real-time churn risk assessment.

---

## 2. Key Features

- End-to-end customer churn prediction pipeline  
- Telecom domain–specific feature engineering  
- Binary classification using supervised machine learning  
- Probability-based churn risk scoring  
- Clear churn risk categorization (Low, Medium, High)  
- Business-oriented retention recommendations  
- Interactive Streamlit analytics dashboard  
- Modular and production-ready project structure  

---

## 3. Technologies Used

| Category | Details |
|--------|--------|
| Programming Language | Python 3.x |
| Data Analysis | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| Model Persistence | Joblib |
| Visualization & UI | Streamlit |
| Dataset | Telco Customer Churn Dataset |
| Environment | Virtual Environment (venv) |

---

## 4. Problem Statement

Telecom companies face significant revenue loss when customers discontinue their services.

The objective of this project is to:
- Predict whether a customer is likely to churn  
- Quantify churn risk using probability scores  
- Provide actionable insights for customer retention strategies  

---

## 5. Machine Learning Pipeline

The system follows a standard supervised machine learning workflow:

1. Data ingestion and cleaning  
2. Exploratory data analysis  
3. Feature engineering and encoding  
4. Train-test split with stratification  
5. Model training and validation  
6. Probability-based churn prediction  
7. Interactive risk assessment via dashboard  

Best model performance: Logistic Regression achieved ROC–AUC 0.842 on validation data.
---

## 6. Project Structure

<pre>
Telecom_Churn_Analytics/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   └── Telco-Customer-Churn.csv
│
├── model/
│   ├── churn_model.pkl
│   └── feature_columns.pkl
│
├── notebooks/
│   └── churn_model_training.ipynb
│
└── venv/
</pre>

---

## 7. Installation and Setup

### Step 1: Clone the Repository
```bash
git clone https://github.com/Ashwinikrishnan-205/telecom-churn-analytics.git
cd telecom-churn-analytics
```

### Step 2: Create and Activate Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
```bash
streamlit run app.py
```

Open the browser at:  
http://localhost:8501

---

## 8. Dashboard Functionality

The Streamlit dashboard allows users to:
- Adjust customer attributes such as tenure, monthly charges, contract type, internet service, and payment method  
- Generate real-time churn probability predictions  
- Classify customers into risk segments  
- View business-focused retention recommendations  

---

## 9. Output Interpretation

- **Low Churn Risk**  
  Customer is likely to remain with the service. Regular engagement is sufficient.

- **Medium Churn Risk**  
  Customer shows potential churn signals. Proactive offers or outreach is recommended.

- **High Churn Risk**  
  Customer is likely to churn. Immediate retention intervention is advised.

---

## 10. Use Cases

- Customer retention strategy planning  
- Telecom business analytics  
- Predictive modeling demonstration  
- Entry-level data science and analytics portfolio  
- Decision support for customer success teams  

---

## 11. Limitations

- Model performance depends on data quality  
- Periodic retraining is required for different telecom markets.
- Dataset represents historical behavior only  
- Requires retraining for different telecom markets  

---

## 12. Developer Information

<p align="justify">
<b>Author:</b> Ashwini Krishnan<br>
<b>Year:</b> 2025<br>
<b>Focus Areas:</b> Data Analytics · Machine Learning · Business Intelligence<br>
<b>GitHub:</b> <a href="https://github.com/Ashwinikrishnan-205" target="_blank">Ashwinikrishnan-205</a>
</p>

---

## 13. License

<p align="justify">
This project is developed for educational and professional demonstration purposes.  
All rights reserved © 2025 <b>Ashwini Krishnan</b>.
</p>
