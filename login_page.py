import streamlit as st
from utils.auth import USERS, verify_user

def main():
    st.title("🔐 Workforce Login Portal")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        role = verify_user(username, password)
        if role:
            # Save info in session state
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.session_state["role"] = role

            st.success(f"Welcome {username.title()} ({role})!")

            # Redirect to role-specific dashboard
            if role == "Admin":
                st.switch_page("admin_dashboard")
            elif role == "Manager":
                st.switch_page("manager_dashboard")
            elif role == "Employee":
                st.switch_page("employee_dashboard")
        else:
            st.error("Invalid username or password.")

if __name__ == "__main__":
    main()
