import streamlit as st
import pandas as pd

st.title("🏆 Crew Leaderboard")

st.subheader("Weekly Motivation Message")
st.info("💬 'Push for 1% better every day!' — Demo User")

# Demo leaderboard
data = {
    "Name": ["Matt", "Sarah", "Jake"],
    "Workout Volume (lbs)": [9333, 8500, 7200],
    "Protein Intake (g)": [140, 120, 135],
    "Cardio Minutes": [85, 60, 100],
}
df = pd.DataFrame(data)

st.dataframe(df, use_container_width=True)
