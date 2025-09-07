import whisper
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)  

model=whisper.load_model("base")




result=model.transcribe("SampleAudio.mp3")
prompt_text = f'{result["text"]} Summarize the above text in 50 words.'
print("Transcript:")
response = client.models.generate_content(
    model="gemini-2.5-flash", contents=prompt_text
)

print(response.text)
