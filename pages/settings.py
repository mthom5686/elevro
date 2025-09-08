import streamlit as st
from auth import login
from db import get_goals, save_goals

# -------------------
# LOGIN REQUIRED
# -------------------
user = login()
if not user:
    st.stop()

# -------------------
# PAGE CONTENT
# -------------------
st.title("⚙️ Settings")

st.subheader("Your Goals")
current_goals = get_goals(user["id"])

protein_default = current_goals.get("protein", 140)
volume_default = current_goals.get("workout_volume", 9000)
cardio_default = current_goals.get("cardio_minutes", 120)

protein = st.number_input("Protein Target (g/day)", value=protein_default)
volume = st.number_input("Workout Volume Goal (lbs/week)", value=volume_default)
cardio = st.number_input("Cardio Minutes (per week)", value=cardio_default)

if st.button("Save Goals"):
    save_goals(user["id"], {
        "protein": protein,
        "workout_volume": volume,
        "cardio_minutes": cardio
    })
    st.success("✅ Goals saved to database!")
