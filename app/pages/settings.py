import streamlit as st

st.title("⚙️ Settings")

st.subheader("Your Goals")
protein = st.number_input("Protein Target (g/day)", value=140)
volume = st.number_input("Workout Volume Goal (lbs/week)", value=9000)
cardio = st.number_input("Cardio Minutes (per week)", value=120)

st.button("Save Goals")

st.subheader("Join a Crew")
invite = st.text_input("Enter Crew Invite Code")
st.button("Join Crew")
