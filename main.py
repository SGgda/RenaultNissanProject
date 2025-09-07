from fastapi import  FastAPI,UploadFile,File
import whisper
import shutil

app=FastAPI()
model=whisper.load_model("base")

@app.get("/")
def home():
    return {"message": "renault-Nissan meeting transcription working"}

@app.post("/transcribe")
async def transcribe_audio(file:UploadFile=File(...)):
    with open(file.filename, "wb") as buffer:
        shutil.copyfileobj(file.file,buffer)

    result = model.transcribe(file.filename)
    return {"transcript": result["text"]}
