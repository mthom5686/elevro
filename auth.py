import streamlit as st
from db import get_user_by_email, verify_password

def login():
    # Already logged in
    if "user" in st.session_state and st.session_state["user"]:
        return st.session_state["user"]

    # Show login form
    st.title("🔐 Login to Elevro")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        user = get_user_by_email(email)
        if user and verify_password(password, user[3]):
            st.session_state["user"] = {"id": user[0], "name": user[1], "email": user[2]}
            st.experimental_rerun()
        else:
            st.error("❌ Invalid email or password")

    return None
