import openai
import os
from dotenv import load_dotenv
from gtts import gTTS
import uuid

#load envirnonment Variables
load_dotenv()

#get api key

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = openai.OpenAI(api_key = OPENAI_API_KEY)

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


