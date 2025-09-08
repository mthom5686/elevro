import streamlit as st
from auth import login
from db import get_goals

st.set_page_config(page_title="Elevro", layout="wide")

# Login check
user = login()

if not user:
    st.stop()  # stop rendering until login succeeds

# Logged-in home page
st.title(f"Welcome {user['name']} 👋")

st.subheader("Your Current Goals")
goals = get_goals(user["id"])
if goals:
    for metric, value in goals.items():
        st.write(f"- {metric}: {value}")
else:
    st.info("No goals found yet. Go to ⚙️ Settings to add them.")

st.sidebar.title("Navigation")
st.sidebar.page_link("pages/leaderboard.py", label="🏆 Leaderboard")
st.sidebar.page_link("pages/profiles.py", label="👤 Profiles")
st.sidebar.page_link("pages/settings.py", label="⚙️ Settings")

# Logout button
if st.sidebar.button("Logout"):
    st.session_state["user"] = None
    st.experimental_rerun()
