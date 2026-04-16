import requests
import whisper

# model = whisper.load_model("base")  # start with base

# result = model.transcribe("a.wav")

# print(result["text"])





def analyze(text):
    prompt = f"""
    Analyze the following statement for logical fallacies.
    Identify if it contains:
    - Ad hominem
    - Strawman
    - False dilemma
    - Slippery slope
    - Hasty generalization

    Text: "{text}"

    Output format:
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

print(analyze("I understand your concern about remote work reducing collaboration, but recent data suggests many teams maintain productivity through structured communication tools."))