import streamlit as st
import pandas as pd
import plotly.express as px

# Page layout
st.set_page_config(page_title="FinTech Baseline Demo", layout="wide")

st.title("FinTech Pipeline: Verification Node")
st.write("Virtual environment and dependency verification successful.")

# Sample financial transactional data
data = {
    "Merchant": ["Korzinka", "Yandex Go", "Uzum Market", "Click P2P", "Payme Merchant"],
    "Category": ["Groceries", "Transport", "E-Commerce", "Transfer", "Utilities"],
    "Amount_UZS": [145000, 32000, 480000, 1200000, 95000]
}
df = pd.DataFrame(data)

# Dashboard widgets
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Transaction Register")
    st.dataframe(df, use_container_width=True)

with col2:
    st.subheader("Expense Distribution")
    fig = px.pie(df, names="Category", values="Amount_UZS", hole=0.4)
    st.plotly_chart(fig, use_container_width=True)

st.success("Environment setup ready for API integrations.")
