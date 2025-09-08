import streamlit_authenticator as stauth
import streamlit as st
from db import get_user, verify_password

def login():
    if "user" not in st.session_state:
        st.session_state["user"] = None

    if st.session_state["user"]:
        return st.session_state["user"]

    # Login form
    st.sidebar.title("Login")
    email = st.sidebar.text_input("Email")
    password = st.sidebar.text_input("Password", type="password")

    if st.sidebar.button("Login"):
        user = get_user(email)
        if user and verify_password(password, user[3]):
            st.session_state["user"] = {"id": user[0], "name": user[1], "email": user[2]}
            st.sidebar.success(f"Welcome back, {user[1]}!")
            return st.session_state["user"]
        else:
            st.sidebar.error("❌ Invalid email or password")

    return None
