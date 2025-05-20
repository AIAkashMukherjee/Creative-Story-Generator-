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



# Generate Story Button
# if st.button("✨ Generate Story"):
#     with st.spinner("Generating your story... 🎭"):
#         response = requests.post(API_URL, json={"genre": genre, "theme": theme, "length": length})
       
#         if response.status_code == 200:
#             data = response.json()
#             story_text = data["story"]
#             audio_url = data["audio_url"]


#             # Display Story
#             st.subheader("📝 Your AI-Generated Story")
#             st.write(story_text)


#             # Play Audio
#             st.subheader("🎙️ Listen to Your Story")
#             st.audio(audio_url)


#             # Download Story as TXT
#             story_file = f"story_{genre}_{theme}.txt"
#             with open(story_file, "w", encoding="utf-8") as f:
#                 f.write(story_text)
           
#             st.download_button(label="📥 Download Story as Text", data=story_text, file_name=story_file, mime="text/plain")
       
#         else:
#             st.error("❌ Error generating the story. Please try again.")


# if st.button("Generate Story"):
#     with st.spinner("Generating your story..."):
#         response = requests.post(API_URL, json={
#             "genre": genre,
#             "theme": theme,
#             "length": length,
#             "language": "hi" if language == "Hindi" else "en"
#         })

#         if response.status_code == 200:
#             result = response.json()
#             st.success("✅ Story Generated!")
#             st.markdown(f"### Story:\n{result['story']}")
#             st.audio(result['audio_url'])
#         else:
#             st.error(f"❌ {response.json().get('detail', 'Error generating the story.')}")


# if 'clicked' not in st.session_state:
#     st.session_state.clicked = False

# if st.button("Generate Story"):
#     st.session_state.clicked = True

# if st.session_state.clicked:
#     with st.spinner("Generating your story..."):
#         try:
#             response = requests.post(API_URL, json={
#                 "genre": genre,
#                 "theme": theme,
#                 "length": length,
#                 "language": "hi" if language == "Hindi" else "en"
#             })

#             if response.status_code == 200:
#                 result = response.json()
#                 st.success("✅ Story Generated!")
#                 st.markdown(f"### Story:\n{result['story']}")
#                 st.audio(result['audio_url'])
#             else:
#                 st.error(f"❌ {response.json().get('detail', 'Error generating the story.')}")
#         except Exception as e:
#             st.error(f"❌ An error occurred: {e}")
#         finally:
#             st.session_state.clicked = False

