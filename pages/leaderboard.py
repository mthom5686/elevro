import streamlit as st
import pandas as pd

st.title("🏆 Crew Leaderboard")

try:
    from db import get_leaderboard
    rows = get_leaderboard()

    if rows:
        df = pd.DataFrame(rows, columns=["Name", "Workout Volume (lbs)", "Protein (g)", "Cardio Minutes"])
        st.dataframe(df, use_container_width=True)
    else:
        st.info("No data yet — add some goals in ⚙️ Settings.")
except Exception as e:
    st.error(f"Leaderboard query failed: {e}")
