import streamlit as st
import requests

API_URL = "http://localhost:8000"
st.title("Login")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login", type="primary"):
    if username and password:
        res = requests.post(f"{API_URL}/login", json={"username": username, "password": password})
        if res.status_code == 200:
            st.session_state.logged_in = True
            st.session_state.token = res.json()["access_token"]
            st.session_state.username = username
            st.success("Login successful!")
            st.switch_page("pages/home.py")
        else:
            st.error("Invalid username or password")
    else:
        st.warning("Fill all fields")