import openai
import os
from dotenv import load_dotenv
from gtts import gTTS
import uuid
# from googletrans import Translator

#load envirnonment Variables
load_dotenv()

#get api key

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = openai.OpenAI(api_key = OPENAI_API_KEY)

# def generate_ai_story(genre: str, theme: str, length: str):
#     prompt=f"Write a complete {length} {genre} story that fully explores the theme of {theme}. Focus on developing the characters and their journeys, crafting a narrative that flows smoothly from beginning to end, keeping readers engaged throughout"

#     response=client.chat.completions.create(
#         model='gpt-4',
#         messages=[
#             {"role":"system","content":"you area creative storyteller"},
#             {"role":"user","content":prompt}
#         ],
#         max_tokens=500
#     )

#     story=response.choices[0].message.content
#     return story

def generate_story_directly_in_hindi(genre, theme, length):
    prompt = (
        f"Write a {length} {genre} story in Hindi that explores the theme of {theme}. "
        "Make the story emotionally engaging, rich in imagination, and culturally relevant."
    )

    response = client.chat.completions.create(
        model='gpt-4',
        messages=[
            {"role": "system", "content": "You are a professional Hindi storyteller."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1000
    )

    return response.choices[0].message.content


def generate_story_directly_in_english(genre, theme, length):
    prompt = (
        f"Write a {length} {genre} story in English that explores the theme of {theme}. "
        "Make the story emotionally engaging and rich in imagination."
    )

    response = client.chat.completions.create(
        model='gpt-4',
        messages=[
            {"role": "system", "content": "You are a professional English storyteller."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1000
    )

    return response.choices[0].message.content

   

# def translate_to_hindi_with_openai(text):
#     prompt = (
#         "Translate the following English story to Hindi, preserving the style and emotional tone:\n\n"
#         f"{text}"
#     )

#     response = client.chat.completions.create(
#         model='gpt-4',
#         messages=[
#             {"role": "system", "content": "You are a professional English to Hindi literary translator."},
#             {"role": "user", "content": prompt}
#         ],
#         max_tokens=1500
#     )

#     return response.choices[0].message.content

# def text_to_speech(story_text, language='hi'):
#     print("\n--- Final Hindi Text Passed to gTTS ---\n", story_text[:300], "\n----------------------\n")
#     try:
#         from gtts import gTTS
#         import uuid, os

#         if len(story_text) > 4900:
#             story_text = story_text[:4900]

#         tts = gTTS(text=story_text, lang=language)
#         filename = f'story_{uuid.uuid4().hex}.mp3'
#         os.makedirs("static", exist_ok=True)
#         file_path = f"static/{filename}"
#         tts.save(file_path)

#         return file_path

#     except Exception as e:
#         print(f"TTS error: {e}")
#         return None


def text_to_speech(text, language="en", filename=None):
    if not filename:
        filename = f"output_{uuid.uuid4().hex[:8]}.mp3"
    
    # Clear old mp3 files to avoid clutter
    for f in os.listdir("static"):
        if f.endswith(".mp3"):
            os.remove(os.path.join("static", f))

    tts = gTTS(text=text, lang=language)
    output_path = os.path.join("static", filename)
    tts.save(output_path)
    return output_path


