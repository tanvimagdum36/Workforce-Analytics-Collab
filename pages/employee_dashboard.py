import streamlit as st
from utils.auth import require_login, show_role_badge

@require_login
def main():
    st.title("👤 Employee Dashboard")
    show_role_badge()

    st.subheader("Employee Controls")
    st.write("Here you can view your tasks, submit reports, and track your performance.")
