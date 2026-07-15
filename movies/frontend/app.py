import streamlit as st
st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="wide")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

st.title("🎬 Movie Recommendation System")

if not st.session_state.logged_in:
    st.write("Please log in or sign up to view movie recommendations")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Login", use_container_width=True):
            st.switch_page("pages/login.py")
    with col2:
        if st.button("Sign Up", use_container_width=True):
            st.switch_page("pages/signup.py")
else:
    st.switch_page("pages/home.py")