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