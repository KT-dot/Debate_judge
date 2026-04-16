import whisper
import nltk

# --- FIX: download required NLTK resources ---
nltk.download('punkt')
nltk.download('punkt_tab')  # <-- this was missing

from nltk.tokenize import sent_tokenize

# --- Load Whisper model ---
model = whisper.load_model("base")  # good for MVP

# --- Transcribe audio ---
result = model.transcribe("trial.wav")

print("\n--- FULL TRANSCRIPT ---\n")
print(result["text"])

# --- Sentence tokenization ---
sentences = sent_tokenize(result["text"])

print("\n--- SENTENCES ---\n")
for i, sentence in enumerate(sentences, 1):
    print(f"{i}. {sentence.strip()}")