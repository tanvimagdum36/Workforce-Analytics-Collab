 

import streamlit as st
from utils.auth import require_login, show_role_badge

@require_login
def main():
    st.title("👑 Admin Dashboard")
    show_role_badge()

    st.subheader("Admin Controls")
    st.write("Here you can manage users, view analytics, and perform administrative tasks.")
