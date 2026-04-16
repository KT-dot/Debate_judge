# AI-Powered Debate Judge (MVP)

## Overview

The AI-Powered Debate Judge is a local, end-to-end system that analyzes spoken arguments and identifies logical fallacies. The system records audio input, converts speech to text, segments the transcript into sentences, and evaluates each sentence using a locally hosted large language model to detect fallacies such as ad hominem, strawman, false dilemma, slippery slope, and hasty generalization.

This project is implemented as a Jupyter Notebook (`mvp.ipynb`) and runs entirely locally without requiring paid APIs or internet-based inference.

---

## Features

* Command-line audio recording
* Offline speech-to-text transcription
* Sentence-level argument analysis
* Detection of common logical fallacies
* Structured report generation (`report.txt`)
* Fully local pipeline (privacy-preserving and cost-free)

---

## System Architecture

Audio Recording
→ Speech-to-Text (Whisper)
→ Sentence Segmentation (NLTK)
→ Fallacy Detection (Local LLM via Ollama)
→ Filtering and Aggregation
→ Report Generation (`report.txt`)

---

## Tech Stack

* Python
* Whisper (speech-to-text)
* Ollama with Mistral (local LLM inference)
* NLTK (sentence tokenization)
* sounddevice (audio recording)
* scipy and numpy (audio processing)
* requests (communication with local LLM API)

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

Ensure the Ollama server is running before executing the notebook. The API will be available at:

```
http://localhost:11434
```

---

## Usage

### 1. Launch Jupyter Notebook

```bash
jupyter notebook
```

Open the file:

```
mvp.ipynb
```

---

### 2. Execute Cells in Order

Run all cells sequentially to ensure proper variable initialization.

---

### 3. Workflow

1. Run the recording cell
2. Press ENTER to start recording
3. Speak your input
4. Press ENTER again to stop
5. Audio is saved as a `.wav` file
6. The notebook transcribes the audio
7. The transcript is split into sentences
8. Each sentence is analyzed for logical fallacies
9. Results are written to `report.txt`

---

## Output

The system generates a file named `report.txt` containing:

* Full transcript
* Detected fallacies with corresponding sentences
* Explanations for each identified fallacy

Example:

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

* Fallacy detection is LLM-based and may not always be fully accurate
* Performance depends on local hardware (CPU/GPU)
* Sentence segmentation depends on transcription quality
* Notebook execution requires running cells in order

---

## Future Improvements

* Real-time streaming analysis
* Confidence scoring for detected fallacies
* Multi-fallacy detection per sentence
* Speaker diarization
* Web-based interface
* Highlighting trigger phrases within sentences
