import streamlit as st
import requests

API_URL = "http://localhost:8000"
st.title("Sign Up")

username = st.text_input("Username")
email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Sign Up", type="primary"):
    if username and email and password:
        try:
            res = requests.post(f"{API_URL}/signup", json={
                "username": username, 
                "email": email, 
                "password": password
            })
            
            if res.status_code == 200:
                st.success("Account created! Please login")
                st.switch_page("pages/login.py")
            else:
                # JSON nahi hai to text dikhao
                try:
                    st.error(res.json()["detail"])
                except:
                    st.error(f"Server Error {res.status_code}: {res.text}")
        except requests.exceptions.ConnectionError:
            st.error("The backend server is not running. Please start the Uvicorn server.")
    else:
        st.warning("Fill all fields")