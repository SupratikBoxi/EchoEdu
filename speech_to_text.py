import whisper
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wavfile

def record_audio(filename="input.wav", duration=5):
    fs = 16000
    print("Recording...")
    data = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    wavfile.write(filename, fs, data)
    return filename

def get_transcription():
    model = whisper.load_model("base")
    filename = record_audio()
    result = model.transcribe(filename)
    return result["text"]
