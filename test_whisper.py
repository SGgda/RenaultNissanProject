import whisper
model=whisper.load_model("base");

result=model.transcribe("SampleAudio.mp3")
print("Transcript:")
print(result["text"])