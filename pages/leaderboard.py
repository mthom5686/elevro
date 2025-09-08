import streamlit as st
import pandas as pd
from auth import login
from db import get_leaderboard

# -------------------
# LOGIN REQUIRED
# -------------------
user = login()
if not user:
    st.stop()

# -------------------
# PAGE CONTENT
# -------------------
st.title("🏆 Crew Leaderboard")

rows = get_leaderboard()
if rows:
    df = pd.DataFrame(rows, columns=["Name", "Workout Volume (lbs)", "Protein (g)", "Cardio Minutes"])
    st.dataframe(df, use_container_width=True)
else:
    st.info("No data yet — add some goals in ⚙️ Settings.")
