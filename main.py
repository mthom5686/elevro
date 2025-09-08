import streamlit as st
from auth import login

st.set_page_config(page_title="Elevro", layout="wide")

user = login()

if not user:
    st.warning("Please log in to continue.")
    st.stop()

# Logged in!
st.title(f"Welcome {user['name']} 👋")
st.write("This is your personal dashboard. Here’s how you’re doing relative to your goals:")

# TODO: query DB for user’s goals + progress and display progress bars
st.info("🚧 Coming soon: your progress against protein, workout volume, and cardio goals.")
