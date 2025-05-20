import streamlit as st
import requests

API_URL = "http://localhost:8000/generate_story"

st.set_page_config(page_title="AI Story Generator", layout="centered")

st.title("📖 AI-Powered Creative Story Generator")
st.markdown("Generate unique AI-powered stories and listen to them!")

# User Inputs
genre = st.selectbox("Select Genre", [
    "Fantasy", "Sci-Fi", "Mystery", "Adventure", "Horror",
    "Romance", "Historical", "Thriller", "Comedy"
])
theme = st.text_input("Enter Story Theme")
length = st.selectbox("Select Story Length", ["short", "medium", "long"])
language = st.radio("Choose Language", ["English", "Hindi"])
language_code = "hi" if language == "Hindi" else "en"

# Only run on button click
if st.button("Generate Story"):
    if not theme.strip():
        st.warning("⚠️ Please enter a theme before generating the story.")
    else:
        with st.spinner("⏳ Generating your story..."):
            try:
                response = requests.post(API_URL, json={
                    "genre": genre,
                    "theme": theme,
                    "length": length,
                    "language": language_code
                })

                if response.status_code == 200:
                    result = response.json()
                    st.success("✅ Story generated successfully!")
                    st.markdown("### ✍️ Story:")
                    st.write(result['story'])

                    st.markdown("### 🔊 Audio:")
                    st.audio(result['audio_url'])

                else:
                    st.error("❌ Error generating the story. Please try again.")
            except Exception as e:
                st.error(f"🚫 Exception occurred: {str(e)}")

