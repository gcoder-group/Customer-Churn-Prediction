import streamlit as st

st.title("ML Pipeline Overview")

st.markdown("""
This page provides a comprehensive overview of the **Machine Learning pipeline**
used for **Customer Churn Prediction**.

The pipeline processes raw data through multiple stages to generate predictions.
""")

st.divider()

# Pipeline Flow
st.subheader("ML Pipeline Flow")

st.markdown("""
➡ **Business Problem**  
⬇  
➡ **Data Collection**  
⬇  
➡ **Data Cleaning**  
⬇  
➡ **EDA (Exploratory Data Analysis)**  
⬇  
➡ **Feature Engineering**  
⬇  
➡ **Model Training**  
⬇  
➡ **Model Evaluation**  
⬇  
➡ **Model Deployment**
""")

st.divider()

# 1 Problem Statement
st.subheader("1. Problem Statement")

st.markdown("""
**Customer churn** refers to customers who stop using a company's service.

For telecom companies this directly impacts:

- Revenue
- Customer lifetime value
- Business growth

**Goal:**  
Predict whether a customer is likely to churn so the company can take proactive retention actions.
""")

st.divider()

# 2 Dataset Description
st.subheader("2. Dataset Description")

st.markdown("""
**Source:**  
https://www.kaggle.com/datasets/muhammadshahidazeem/customer-churn-dataset
""")

st.table({
"Property": ["Total Records", "Input Features", "Target Column", "Data Type"],
"Value": ["7,044", "20", "Churn", "Structured Tabular Data"]
})

st.divider()

# 3 Understanding Features
st.subheader("3. Understanding the Features")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Customer Profile")
    st.markdown("""
- Gender  
- SeniorCitizen  
- Partner  
- Dependents
""")

    st.markdown("### Billing Information")
    st.markdown("""
- MonthlyCharges  
- TotalCharges  
- PaymentMethod  
- Contract
""")

with col2:
    st.markdown("### Service Information")
    st.markdown("""
- InternetService  
- PhoneService  
- StreamingTV  
- OnlineSecurity
""")

    st.markdown("### Customer History")
    st.markdown("""
- Tenure (months stayed)
""")

st.divider()

# 4 Data Preprocessing
st.subheader("4. Data Preprocessing")

st.markdown("### Handling Missing Values")

st.markdown("""
- `TotalCharges` had missing values  
- Converted to numeric  
- Missing values handled using **median imputation**
""")

st.markdown("### Handling Categorical Features")

st.markdown("""
Many features are categorical:

- Contract Type
- Internet Service
- Payment Method

Converted to numeric using **One Hot Encoding**.
""")

st.divider()

# 5 Feature Engineering Pipeline
st.subheader("5. Feature Engineering Pipeline")

st.markdown("A **Scikit-Learn Pipeline** was created to automate preprocessing and model training.")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Numeric Features Processing")
    st.markdown("""
- Missing value imputation (median)
- Feature scaling (StandardScaler)
""")

with col2:
    st.markdown("### Categorical Features Processing")
    st.markdown("""
- Missing value imputation (most frequent)
- One-hot encoding
""")

st.markdown("### Advantages of Pipeline")

st.markdown("""
- Ensures consistent preprocessing
- Prevents data leakage
- Simplifies model deployment
- Easy integration with APIs
""")

st.divider()

# 6 Train Test Split
st.subheader("6. Train-Test Split")

st.table({
"Split": ["Training Data", "Testing Data", "Sampling Method"],
"Value": ["80%", "20%", "Stratified Sampling"]
})

st.markdown("""
**Why Stratified Sampling?**

Ensures both sets maintain the same proportion of churn and non-churn customers.
""")

st.divider()

# 7 Model Selection
st.subheader("7. Model Selection")

st.markdown("""
**Algorithm:** Logistic Regression

Why Logistic Regression?

- Works well with structured data
- Highly interpretable
- Computationally efficient
- Suitable for binary classification

**Output:**

- `0` → Customer will stay  
- `1` → Customer will churn
""")

st.divider()

# 8 Model Deployment
st.subheader("8. Model Deployment")

st.markdown("""
The trained Machine Learning model is deployed using **Streamlit**, which provides
an interactive web interface for users to test churn predictions.

Users can input customer information through the UI form and the model will
generate predictions instantly.
""")

st.table({
"Application Component":[
"Home Page",
"Prediction Form",
"Sample Customer Loader",
"Model Metrics Page",
"Pipeline Page"
],
"Description":[
"Overview of the project and instructions",
"Users enter customer information to predict churn",
"Loads example customers to quickly test predictions",
"Displays model performance metrics",
"Explains the ML pipeline used in the project"
]
})
st.divider()

# 9 Business Impact
st.subheader("9. Business Impact")

st.markdown("""
Customer churn prediction helps companies:

- Identify high-risk customers
- Take proactive retention actions
- Reduce customer loss
- Increase revenue and customer lifetime value
""")