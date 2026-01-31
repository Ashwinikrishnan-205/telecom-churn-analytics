import streamlit as st
import pandas as pd
import joblib

# =========================================================
# Page configuration
# =========================================================
st.set_page_config(
    page_title="Customer Churn Risk Analytics",
    page_icon="📊",
    layout="wide"
)

# =========================================================
# Custom CSS (Enterprise-grade UI)
# =========================================================
st.markdown("""
<style>
            
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

* {
    font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;
}
.stApp {
    background: linear-gradient(135deg, #0f172a, #020617);
    color: #e5e7eb;
}

h1, h2, h3 {
    font-weight: 600 !important;
    color: #f8fafc;
}

section[data-testid="stSidebar"] {
    background-color: #020617;
    border-right: 1px solid #1e293b;
}

.stButton > button {
    background: linear-gradient(90deg, #2563eb, #1d4ed8);
    color: white;
    font-weight: 600;
    border-radius: 8px;
    padding: 0.6em 1.4em;
    border: none;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #1e40af, #1e3a8a);
}

.result-card {
    background: rgba(15, 23, 42, 0.85);
    padding: 16px;
    border-radius: 14px;
    border: 1px solid #1e293b;
    margin-top: 12px;
}

footer {
    visibility: hidden;
}
            
.center-title {
    text-align: center;
    margin-top: 10px;
    margin-bottom: 10px;
}

.center-subtitle {
    text-align: center;
    color: #cbd5f5;
    font-size: 1.05rem;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# Load model and feature columns
# =========================================================
model = joblib.load("model/churn_model.pkl")
feature_columns = joblib.load("model/feature_columns.pkl")

# =========================================================
# Title & description
# =========================================================
st.markdown(
    """
    <div class="center-title">
        <h1> Customer Churn Risk Analytics</h1>
    </div>
    <div class="center-subtitle">
        An executive-style analytics dashboard designed to help business teams
        proactively identify customers at risk of churn and take targeted retention actions.
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# =========================================================
# Sidebar inputs
# =========================================================
st.sidebar.markdown("## Customer Profile Inputs")
st.sidebar.markdown(
    "<span style='color:#94a3b8;'>Adjust customer attributes to evaluate churn risk</span>",
    unsafe_allow_html=True
)

tenure = st.sidebar.slider("Tenure (Months)", 0, 72, 12)
monthly_charges = st.sidebar.slider("Monthly Charges", 20, 150, 70)

contract = st.sidebar.selectbox(
    "Contract Type",
    ["Month-to-month", "One year", "Two year"]
)

internet_service = st.sidebar.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

payment_method = st.sidebar.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

# =========================================================
# Build input dataframe (safe alignment)
# =========================================================
input_df = pd.DataFrame(
    [[0] * len(feature_columns)],
    columns=feature_columns
)

if "Tenure_Months" in input_df.columns:
    input_df["Tenure_Months"] = tenure

if "Monthly_Charges" in input_df.columns:
    input_df["Monthly_Charges"] = monthly_charges

if f"Contract_{contract}" in input_df.columns:
    input_df[f"Contract_{contract}"] = 1

if f"Internet_Service_{internet_service}" in input_df.columns:
    input_df[f"Internet_Service_{internet_service}"] = 1

if f"Payment_Method_{payment_method}" in input_df.columns:
    input_df[f"Payment_Method_{payment_method}"] = 1

# =========================================================
# Prediction section (NO Streamlit alerts)
# =========================================================
st.markdown("### Churn Risk Assessment")

if st.button("Run Churn Risk Assessment"):
    churn_prob = model.predict_proba(input_df)[0][1]

    st.markdown('<div class="result-card">', unsafe_allow_html=True)

    if churn_prob < 0.3:
        st.markdown(f"### 🟢 Low churn risk — {churn_prob:.2%}")
        st.markdown(
            "**Recommended action:** Maintain regular engagement and monitor usage trends."
        )
    elif churn_prob < 0.6:
        st.markdown(f"### 🟡 Medium churn risk — {churn_prob:.2%}")
        st.markdown(
            "**Recommended action:** Consider personalized offers or proactive customer outreach."
        )
    else:
        st.markdown(f"### 🔴 High churn risk — {churn_prob:.2%}")
        st.markdown(
            "**Recommended action:** Immediate retention intervention is advised "
            "(discounts, plan optimization, or support outreach)."
        )

    st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# Footer
# =========================================================
st.markdown("---")
st.markdown(
    "<span style='color:#64748b; font-size:0.85rem;'>"
    "This dashboard demonstrates predictive analytics capabilities for decision support. "
    "Outputs are illustrative and should be validated before operational deployment."
    "</span>",
    unsafe_allow_html=True
)
