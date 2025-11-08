import streamlit as st
from utils.auth import require_login, show_role_badge

@require_login
def main():
    st.title("📊 Manager Dashboard")
    show_role_badge()

    st.subheader("Manager Controls")
    st.write("Here you can track team performance, assign tasks, and review reports.")

