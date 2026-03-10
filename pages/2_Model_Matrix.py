import streamlit as st
import pickle
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

st.title("Model Performance Metrics")

st.markdown("""
This page shows the performance metrics of the **Customer Churn Prediction** model.

These metrics are calculated on the entire dataset to evaluate how well the model can predict customer churn.
""")

st.divider()

# load model and dataset
model = pickle.load(open("model.pkl","rb"))
df = pd.read_csv("./data/Telco_Customer_Churn_lyst1769326950438.csv")

df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df["Churn"] = df["Churn"].map({"No":0,"Yes":1})

X = df.drop(columns=["customerID","Churn"])
y = df["Churn"]

# ===============================
# MODEL PERFORMANCE CALCULATION
# ===============================

y_pred = model.predict(X)

accuracy = accuracy_score(y, y_pred)
precision = precision_score(y, y_pred)
recall = recall_score(y, y_pred)
f1 = f1_score(y, y_pred)

cm = confusion_matrix(y, y_pred)

# -----------------------------
# Metric Cards
# -----------------------------

col1, col2, col3, col4 = st.columns(4)

col1.metric("Accuracy", f"{accuracy*100:.1f}%",delta="Overall correctness",delta_arrow="off", delta_color="off",border=True)
col2.metric("Precision", f"{precision*100:.1f}%",delta="Positive prediction accuracy",delta_arrow="off", delta_color="off",border=True)
col3.metric("Recall", f"{recall*100:.1f}%",delta="Churn detection rate",delta_arrow="off", delta_color="off",border=True)
col4.metric("F1 Score", f"{f1*100:.1f}%",delta="Harmonic mean",delta_arrow="off", delta_color="off",border=True)

st.divider()

# -----------------------------
# Metric Explanations
# -----------------------------

with st.expander("What is Accuracy?"):
    st.markdown("""
**Accuracy** measures the overall correctness of the model.

Formula:  
`(TP + TN) / Total Predictions`

Example:  
If accuracy is **75%**, the model correctly predicts churn **75 out of 100 times**.
""")

with st.expander("What is Precision?"):
    st.markdown("""
**Precision** measures how many predicted churners actually churned.

Formula:  
`TP / (TP + FP)`

When the model says **customer will churn**, how often is it correct?
""")

with st.expander("What is Recall?"):
    st.markdown("""
**Recall** measures how many actual churners the model identifies.

Formula:  
`TP / (TP + FN)`

Out of all churned customers, how many did the model catch?
""")

with st.expander("What is F1 Score?"):
    st.markdown("""
**F1 Score** balances Precision and Recall.

Formula:  
`2 × (Precision × Recall) / (Precision + Recall)`
""")

st.divider()

# -----------------------------
# Confusion Matrix
# -----------------------------

st.subheader("Confusion Matrix")

cm_df = pd.DataFrame(
    cm,
    index=["Actual No Churn","Actual Churn"],
    columns=["Predicted No Churn","Predicted Churn"]
)

st.dataframe(cm_df, use_container_width=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
**TN (True Negative)**  
Correctly predicted "No Churn"

**FP (False Positive)**  
Incorrectly predicted "Churn"
""")

with col2:
    st.markdown("""
**FN (False Negative)**  
Missed churn predictions

**TP (True Positive)**  
Correctly predicted "Churn"
""")

st.divider()

# -----------------------------
# Model Info
# -----------------------------

st.subheader("Model Information")

st.markdown(f"""
**Algorithm:** Logistic Regression  
**Dataset:** [Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)  
**Total Samples:** {len(df):,}  
**Features Used:** 19
""")