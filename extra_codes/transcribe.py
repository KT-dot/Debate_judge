import whisper

model = whisper.load_model("base")  # start with base

result = model.transcribe("a.wav")

print(result["text"])