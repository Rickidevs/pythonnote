import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import time
import os
from datetime import datetime

class MicRecorder:
    def __init__(self, duration=20, fs=44100, output_folder="recordings"):
        self.duration = duration  # saniyə cinsindən (20 saniyə)
        self.fs = fs  # Səslərin keyfiyyəti (Hz)
        self.output_folder = output_folder
        os.makedirs(self.output_folder, exist_ok=True)

    def record_and_save(self):
        while True:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = os.path.join(self.output_folder, f"audio_{timestamp}.wav")
            print(f"[+] Səs yazılır ({self.duration} saniyə)... Fayl: {filename}")

            # Səsi yaz
            recording = sd.rec(int(self.duration * self.fs), samplerate=self.fs, channels=1, dtype='int16')
            sd.wait()  # Yazma tamamlanana qədər gözləyir

            # Fayla yaz
            write(filename, self.fs, recording)
            print("[+] Yadda saxlanıldı.")

if __name__ == "__main__":
    try:
        recorder = MicRecorder(duration=20)
        recorder.record_and_save()
    except KeyboardInterrupt:
        print("\n[!] Proses dayandırıldı.")
