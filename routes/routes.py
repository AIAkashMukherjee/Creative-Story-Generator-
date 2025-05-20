from fastapi import APIRouter
from pydantic import BaseModel
from fastapi import HTTPException
import traceback
from services.service import text_to_speech,generate_story_directly_in_hindi,generate_story_directly_in_english

router=APIRouter()

class StoryRequest(BaseModel):
    genre: str
    theme: str
    length: str
    language: str


@router.post("/generate_story")
def generate_story(request: StoryRequest):
    try:
        print("Incoming request:", request)
        if request.language == "hi":
            story = generate_story_directly_in_hindi(request.genre, request.theme, request.length)
            audio_path = text_to_speech(story, language="hi")
        else:
            story = generate_story_directly_in_english(request.genre, request.theme, request.length)
            audio_path = text_to_speech(story, language="en")

        print("Generated story:", story)
        print("Audio saved to:", audio_path)

        audio_filename = audio_path.split("/")[-1] if audio_path else None
        audio_url = f"http://127.0.0.1:8000/static/{audio_filename}" if audio_filename else None

        result = {
            "story": story,
            "audio_url": audio_url
        }
        print("Returning response:", result)
        return result

    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"❌ Error: {str(e)}")