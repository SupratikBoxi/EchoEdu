
import sounddevice as sd
import scipy.io.wavfile as wav
import numpy as np
from nlp_modules import process_audio_input

def record_audio(filename, duration=5, fs=44100):
    print("🎙️ Recording started...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()  # Wait until recording is finished
    print("✅ Recording finished.")
    wav.write(filename, fs, audio)

def main():
    filename = "your_audio.wav"
    record_audio(filename)
    process_audio_input(filename)

if __name__ == "__main__":
    main()

