import whisper
import nltk
import requests

# --- NLTK setup (run once, then you can comment this out) ---
nltk.download('punkt')
nltk.download('punkt_tab')

from nltk.tokenize import sent_tokenize

# --- Load Whisper model ---
model = whisper.load_model("base")

# --- Transcribe audio ---
result = model.transcribe("trial.wav")

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