import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import streamlit as st
from etl.fetch_f1_data import get_race_results

st.title("🏎️ F1 Pitwall Analytics")
year = st.slider("Select Year", 2010, 2024, 2023)
round_num = st.number_input("Round Number", min_value=1, max_value=22, value=1)

df = get_race_results(year, round_num)

if df.empty:
    st.warning("No data available for this round.")
else:
    st.dataframe(df)
    st.bar_chart(df.set_index('driver')['position'].astype(int))
