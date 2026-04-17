import whisper
import nltk
import requests
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write








SAMPLE_RATE = 16000  # Whisper-friendly
recording = []
is_recording = False


def callback(indata, frames, time, status):
    if is_recording:
        recording.append(indata.copy())


def start_recording():
    global is_recording, recording
    recording = []
    is_recording = True
    print("🔴 Recording started... Press ENTER to stop.")


def stop_recording(filename="output.wav"):
    global is_recording
    is_recording = False

    audio = np.concatenate(recording, axis=0)

    # Convert to int16 for WAV
    audio = (audio * 32767).astype(np.int16)

    write(filename, SAMPLE_RATE, audio)
    print(f"✅ Saved recording as {filename}")


def main():
    print("=== CLI Audio Recorder ===")
    print("Press ENTER to start recording")
    input()

    # Start stream
    with sd.InputStream(samplerate=SAMPLE_RATE, channels=1, callback=callback):
        start_recording()
        input()  # wait for ENTER to stop
        stop_recording()


if __name__ == "__main__":
    main()



# --- NLTK setup (run once, then you can comment this out) ---
nltk.download('punkt')
nltk.download('punkt_tab')

from nltk.tokenize import sent_tokenize

# --- Load Whisper model ---
model = whisper.load_model("base")

# --- Transcribe audio ---
result = model.transcribe("output.wav")

# --- Sentence tokenization ---
sentences = sent_tokenize(result["text"])

# --- Fallacy Analyzer ---
def analyze(text):
    prompt = f"""
    Analyze the following statement for logical fallacies.

    Possible fallacies:
    - Ad hominem
    - Strawman
    - False dilemma
    - Slippery slope
    - Hasty generalization

    If none are present, return:
    Fallacy: None

    Text: "{text}"

    Output format strictly:
    Fallacy: <type or None>
    Explanation: <short explanation>
    """

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]


# --- Open file to write report ---
with open("report.txt", "w") as f:

    f.write("=== FULL TRANSCRIPT ===\n\n")
    f.write(result["text"] + "\n\n")

    fallacy_results = []

    f.write("=== ANALYSIS ===\n\n")

    for i, sentence in enumerate(sentences, 1):
        sentence = sentence.strip()

        # skip very short/noisy sentences
        if len(sentence.split()) < 5:
            continue

        output = analyze(sentence)

        # Only keep sentences where fallacy is detected
        if "Fallacy: None" not in output:
            print(f"Detected fallacy at line {i}")  # minimal terminal feedback

            f.write(f"Line {i}: {sentence}\n")
            f.write(output + "\n")
            f.write("-" * 50 + "\n")

            fallacy_results.append({
                "line": i,
                "text": sentence,
                "analysis": output
            })

    # --- Final Summary ---
    f.write("\n=== FINAL FALLACY LIST ===\n\n")

    for item in fallacy_results:
        f.write(f"Line {item['line']}: {item['text']}\n")
        f.write(item["analysis"] + "\n\n")

print("\n✅ Report saved to report.txt")