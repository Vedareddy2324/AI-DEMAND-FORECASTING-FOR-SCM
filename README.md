#AI DEMAND FORECASTING FOR SCM
ML model to forecast demand for 1000+ SKUs using XGBoost &amp; LSTM | Built with Supply Chain domain knowledge from Oracle Fusion SCM
**Problem:** In Oracle Fusion SCM, procurement fails because demand is guessed, not predicted.
Solution: Predict next 28 days demand using XGBoost vs LSTM.
Dataset: M5 Forecasting (Walmart) - 30k products, 5 years sales.
Stack: Python, Pandas, XGBoost, Streamlit
## Results
- Product: FOODS_3_090 (CA_1)
- Baseline XGBoost RMSE: 32.39
- With Price + Lag Features RMSE: 28.01 (13.5% improvement)
- Top Drivers: lag_7 (20.9%), sell_price (20.8%)

