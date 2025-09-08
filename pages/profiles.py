import streamlit as st
from auth import login

# -------------------
# LOGIN REQUIRED
# -------------------
user = login()
if not user:
    st.stop()

# -------------------
# PAGE CONTENT
# -------------------
st.title("👤 Crew Profiles")

crew_members = ["Demo User"]  # TODO: fetch from DB
selected = st.selectbox("Select a member", crew_members)

st.subheader(f"Stats for {selected}")
st.write("📈 Example charts and progress bars will go here.")
