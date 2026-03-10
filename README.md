# Customer Churn Prediction (Streamlit ML App)

## Project Overview

Customer churn refers to customers who stop using a company's product or service.
In subscription-based industries like telecom, predicting churn helps businesses take proactive retention actions.

This project builds a **Machine Learning model to predict customer churn** using the **Telco Customer Churn Dataset** and deploys it using **Streamlit** to provide an interactive web application.

The application allows users to input customer details and instantly predict whether the customer is likely to churn.

---

# Live Application Features

### 1. Customer Churn Prediction

Users can input customer information such as:

- Customer demographics
- Services used
- Billing details
- Contract type
- Payment method

The model predicts:

- Whether the customer will churn
- Churn probability

---

### 2. Sample Customer Loader

The app provides example customers such as:

- Random sample customer
- High churn risk customer
- Low churn risk customer

This allows quick testing without manually entering all fields.

---

### 3. Model Metrics

Displays performance metrics of the trained model including:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

---

### 4. Machine Learning Pipeline Explanation

The application also explains the complete ML pipeline used in the project, including:

- Data preprocessing
- Feature engineering
- Model training
- Evaluation
- Deployment

---

# Machine Learning Pipeline

The model training pipeline consists of the following stages:

1. Business Problem Definition
2. Data Collection
3. Data Cleaning
4. Exploratory Data Analysis (EDA)
5. Feature Engineering
6. Train-Test Split
7. Model Training
8. Model Evaluation
9. Model Deployment

---

# Dataset

**Dataset Name:** Telco Customer Churn Dataset

Source:
https://www.kaggle.com/datasets/muhammadshahidazeem/customer-churn-dataset

Dataset Details:

| Property        | Value                   |
| --------------- | ----------------------- |
| Total Records   | 7044                    |
| Features        | 20                      |
| Target Variable | Churn                   |
| Data Type       | Structured Tabular Data |

---

# Features Used

### Customer Profile

- Gender
- SeniorCitizen
- Partner
- Dependents

### Service Information

- PhoneService
- MultipleLines
- InternetService
- OnlineSecurity
- OnlineBackup
- DeviceProtection
- TechSupport
- StreamingTV
- StreamingMovies

### Billing Information

- Contract
- PaperlessBilling
- PaymentMethod
- MonthlyCharges
- TotalCharges

### Customer History

- Tenure

---

# Model Used

**Algorithm:** Logistic Regression

Why Logistic Regression?

- Works well with structured data
- Highly interpretable
- Efficient for binary classification
- Fast prediction time

Output:

- 0 → Customer will stay
- 1 → Customer will churn

---

# Tech Stack

### Programming

- Python

### Libraries

- Pandas
- NumPy
- Scikit-Learn
- Joblib

### Web Framework

- Streamlit

### Environment Management

- uv / Python Virtual Environment

---

# Project Structure

```
Customer-Churn-Prediction

├── app.py / main.py
├── model.pkl
├── dataset.csv
├── requirements.txt
├── README.md
│
├── pages
│   ├── 1_Home.py
│   ├── 2_Model_Metrics.py
│   └── 3_Pipeline.py
│
└── assets
```

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/gcoder-group/Customer-Churn-Prediction.git
cd Customer-Churn-Prediction
```

---

## 2. Install uv (if not installed)

```bash
pip install uv
```

or using official installer

```bash
curl -Ls https://astral.sh/uv/install.sh | sh
```

---

## 3. Create Project Environment

Initialize the environment and install dependencies:

```bash
uv sync
```

This will:

- Create a `.venv` automatically
- Install all dependencies defined in `pyproject.toml` or `requirements.txt`

---

## 4. Activate the Environment

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

---

# Running the Application

Start the Streamlit server:

```bash
uv run streamlit run main.py
```

The app will open in your browser:

```
http://localhost:8501
```

---

# Running the Application

Start the Streamlit server

```
streamlit run main.py
```

The app will open in your browser:

```
http://localhost:8501
```

---

# Future Improvements

Possible enhancements:

- Add more ML models (Random Forest, XGBoost)
- Model comparison dashboard
- Feature importance visualization
- Explainable AI using SHAP
- Cloud deployment
- Real-time API integration

---

# Author

Developed as a Machine Learning and Streamlit project demonstrating end-to-end ML deployment.

---

# License

This project is for educational and learning purposes.
