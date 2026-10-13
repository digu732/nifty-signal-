
import streamlit as st

st.set_page_config(page_title="NIFTY Signal Bot", layout="wide")
st.title("NIFTY Live Signal Bot")
st.caption("EMA + RSI + VWAP | 5-minute signals")
st.warning("Demo only: Live market data is not connected yet.")

col1, col2, col3 = st.columns(3)
col1.metric("Market", "NIFTY 50")
col2.metric("Timeframe", "5 Minutes")
col3.metric("Signal", "WAIT")
