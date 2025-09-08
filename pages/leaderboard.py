import streamlit as st
import pandas as pd
from db import get_leaderboard

st.title("🏆 Crew Leaderboard")

# Fetch leaderboard rows from DB
rows = get_leaderboard()

if rows:
    st.subheader("Weekly Motivation Message")
    st.info("💬 Data-driven message rotation coming soon...")

    # Convert DB rows into DataFrame
    df = pd.DataFrame(rows, columns=["Name", "Workout Volume (lbs)", "Protein (g)", "Cardio Minutes"])
    st.dataframe(df, use_container_width=True)
else:
    st.warning("⚠️ No leaderboard data found. Add users/goals first.")
