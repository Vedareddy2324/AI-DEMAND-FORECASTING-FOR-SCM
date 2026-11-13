import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="AI Demand Forecasting - SCM", layout="wide")
st.title("📦 AI Demand Forecasting for SCM")
st.markdown("**Product:** FOODS_3_090 (CA_1) | **Model:** XGBoost | **Dataset:** M5 Walmart")

# Load data
df = pd.read_csv('forecast_28_days.csv')
df['date'] = pd.to_datetime(df['date'])

# KPIs
col1, col2, col3 = st.columns(3)
rmse = np.sqrt(np.mean((df['sales'] - df['predicted'])**2))
col1.metric("RMSE (28-day)", f"{rmse:.2f}")
col2.metric("Mean Daily Sales", f"{df['sales'].mean():.1f}")
col3.metric("Total Forecasted Demand (28d)", f"{int(df['predicted'].sum())} units")

st.subheader("Actual vs Predicted - Last 28 Days")
st.line_chart(df.set_index('date')[['sales','predicted']])

st.subheader("Forecast Table + Reorder Suggestion")
df['reorder_qty'] = np.maximum(df['predicted'] - df['sales'], 0).round(0).astype(int)
df['safety_stock'] = (df['predicted'] * 0.2).round(0).astype(int)
st.dataframe(df, use_container_width=True)

st.markdown("---")
st.markdown("**Business Insight:** lag_7 (20.9%) and sell_price (20.8%) drive 42% of demand. Adding price improved RMSE by 13.5% (32.39 → 28.01).")
