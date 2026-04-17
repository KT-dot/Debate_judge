# AI-Powered Debate Judge (MVP)

## Overview

The AI-Powered Debate Judge is a local, end-to-end system designed to analyze spoken arguments and identify logical fallacies in near real-time. The system records audio input, converts speech to text, segments the transcript into sentences, and evaluates each sentence using a locally hosted large language model to detect common fallacies such as ad hominem, strawman, false dilemma, slippery slope, and hasty generalization.

The entire pipeline runs locally without reliance on paid APIs, ensuring privacy, low cost, and reproducibility.

---

## Features

* Audio recording via command-line interface
* Offline speech-to-text transcription
* Sentence-level argument analysis
* Detection of common logical fallacies
* Structured output saved to a report file
* Fully local execution (no external API dependencies)

---

## System Architecture

Audio Input
→ Speech-to-Text (Whisper)
→ Sentence Segmentation (NLTK)
→ Fallacy Detection (Local LLM via Ollama)
→ Filter & Aggregate Results
→ Output Report (report.txt)

---

## Tech Stack

* Python
* Whisper (speech-to-text)
* Ollama with Mistral (local LLM inference)
* NLTK (sentence tokenization)
* sounddevice (audio recording)
* scipy and numpy (audio processing)
* requests (API communication with local LLM)

---

## Installation

### 1. Clone the repository

```bash
git clone git@github.com:KT-dot/Debate_judge.git
cd Debate_judge
```

### 2. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 3. Install system dependencies

```bash
sudo apt install ffmpeg
sudo apt install portaudio19-dev
```

---

## Setting up the Local LLM

Install Ollama:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Download and run the model:

```bash
ollama run mistral
```

Ensure the Ollama server is running before executing the main script. The API will be available at:

```
http://localhost:11434
```

---

## Usage

Run the main script:

```bash
python main.py
```

### Workflow

1. Press ENTER to start recording
2. Speak your input
3. Press ENTER again to stop recording
4. Audio is saved as a `.wav` file
5. The system transcribes the audio
6. Each sentence is analyzed for logical fallacies
7. Results are saved to `report.txt`

---

## Output

The system generates a file named `report.txt` containing:

* Full transcript
* Detected fallacies with corresponding sentences
* Explanations for each identified fallacy

Example structure:

```
=== FULL TRANSCRIPT ===

...

=== ANALYSIS ===

Line 3: People like you always ruin everything
Fallacy: Ad hominem
Explanation: Attacks the person instead of addressing the argument

--------------------------------------------------

=== FINAL FALLACY LIST ===

Line 3: ...
Fallacy: ...
Explanation: ...
```

---

## Limitations

* Fallacy detection is heuristic and LLM-based; results may not always be perfectly accurate
* Latency may vary depending on hardware (CPU vs GPU)
* Real-time performance is approximated using chunk-based processing
* Sentence segmentation depends on transcription quality

---

## Future Improvements

* Real-time streaming analysis
* Confidence scoring for fallacy detection
* Multi-fallacy detection per sentence
* Speaker identification and tracking
* Web-based user interface
* Highlighting specific trigger phrases within sentences

---

## License

This project is intended for educational and experimental purposes.
