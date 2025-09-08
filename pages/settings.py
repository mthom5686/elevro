import streamlit as st

st.title("⚙️ Settings")

st.subheader("Your Goals")
protein = st.number_input("Protein Target (g/day)", value=140)
volume = st.number_input("Workout Volume Goal (lbs/week)", value=9000)
cardio = st.number_input("Cardio Minutes (per week)", value=120)

if st.button("Save Goals"):
    st.success("✅ Goals saved (demo only, DB coming soon).")

st.subheader("Join a Crew")
invite = st.text_input("Enter Crew Invite Code")
if st.button("Join Crew"):
    st.success(f"✅ Joined crew with code: {invite} (demo only)")
