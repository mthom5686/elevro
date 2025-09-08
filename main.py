import streamlit as st

st.set_page_config(page_title="Elevro", layout="wide")

st.title("Elevro 🚀")
st.write("Welcome! Use the sidebar to navigate.")

st.sidebar.title("Navigation")
st.sidebar.page_link("pages/leaderboard.py", label="🏆 Leaderboard")
st.sidebar.page_link("pages/profiles.py", label="👤 Profiles")
st.sidebar.page_link("pages/settings.py", label="⚙️ Settings")
