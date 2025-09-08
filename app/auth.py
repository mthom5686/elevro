import streamlit as st

def login():
    """Dummy login for MVP. Replace with real auth later."""
    if "user" not in st.session_state:
        st.session_state["user"] = {"id": 1, "name": "Demo User"}
    return st.session_state["user"]
