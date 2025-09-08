import streamlit as st
from db import get_goals, save_goals

st.title("⚙️ Settings")

# For now, hardcode demo user (id=1). Later this will come from login.
USER_ID = 1

# Load existing goals from DB
current_goals = get_goals(USER_ID)

protein_default = current_goals.get("protein", 140)
volume_default = current_goals.get("workout_volume", 9000)
cardio_default = current_goals.get("cardio_minutes", 120)

st.subheader("Your Goals")
protein = st.number_input("Protein Target (g/day)", value=protein_default)
volume = st.number_input("Workout Volume Goal (lbs/week)", value=volume_default)
cardio = st.number_input("Cardio Minutes (per week)", value=cardio_default)

if st.button("Save Goals"):
    save_goals(USER_ID, {
        "protein": protein,
        "workout_volume": volume,
        "cardio_minutes": cardio
    })
    st.success("✅ Goals saved to database!")
