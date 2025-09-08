import streamlit as st
from auth import login
from db import init_db

st.set_page_config(page_title="Elevro", layout="wide")

# Initialize DB
init_db()

# Authentication
user = login()

if user:
    st.sidebar.success(f"Logged in as {user['name']}")
    st.sidebar.write("Active Crew: Downtown Gym (demo)")
    st.title("Welcome to Elevro 🚀")
    st.write("Use the sidebar to navigate between Leaderboard, Profiles, and Settings.")
else:
    st.warning("Please log in to continue.")
