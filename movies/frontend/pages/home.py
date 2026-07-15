import streamlit as st
import requests

API_URL = "http://localhost:8000"

if not st.session_state.get("logged_in"):
    st.switch_page("app.py")

st.title(f"Welcome {st.session_state.username} 🎬")
if st.button("Logout"):
    st.session_state.logged_in = False
    st.switch_page("app.py")

headers = {"Authorization": f"Bearer {st.session_state.token}"}

try:
    res = requests.get(f"{API_URL}/movies", headers=headers)
    movies_data = res.json()
except:
    st.error("Unable to connect to the backend server.")
    st.stop()

movie_dict = {m["title"]: m["movie_id"] for m in movies_data}
selected_title = st.selectbox("Select Movies:", list(movie_dict.keys()))

if st.button("🎯 Recommend Similar Movies", type="primary"):
    payload = {"movie_id": movie_dict[selected_title], "movie_title": selected_title}
    
    with st.spinner("Model is generating recommendations.."):
        response = requests.post(f"{API_URL}/recommend", json=payload, headers=headers)

    if response.status_code == 200:
        data = response.json()
        st.subheader(f"**{selected_title}** types movies:")
        for movie in data["recommendations"]:
            st.write(f"🎬 **{movie['title']}**")
    else:
        st.error(f"Error: {response.text}")