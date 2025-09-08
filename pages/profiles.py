import streamlit as st

st.title("👤 Crew Profiles")

crew_members = ["Matt", "Alex", "Jake"]
selected = st.selectbox("Select a member", crew_members)

st.subheader(f"Stats for {selected}")
st.write("📈 Example charts and progress bars will go here.")
