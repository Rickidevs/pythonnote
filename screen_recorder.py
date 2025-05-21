import cv2
import numpy as np
import pyautogui
import time
import os

class ScreenRecorder:
    def __init__(self, save_dir="recordings/", duration=10, frame_rate=10):
        self.save_dir = save_dir
        self.duration = duration 
        self.frame_rate = frame_rate
        self.screen_size = pyautogui.size()
        self.is_recording = True

        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

    def start(self):
        file_index = 1
        print("[+] Screen recorder başladı...")

        while self.is_recording:
            filename = os.path.join(self.save_dir, f"screen_{file_index}.mp4")
            fourcc = cv2.VideoWriter_fourcc(*"mp4v")
            out = cv2.VideoWriter(filename, fourcc, self.frame_rate, self.screen_size)

            start_time = time.time()
            while time.time() - start_time < self.duration:
                img = pyautogui.screenshot()
                frame = np.array(img)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                out.write(frame)

            out.release()
            print(f"[+] Fayl saxlanıldı: {filename}")
            file_index += 1

    def stop(self):
        self.is_recording = False

if __name__ == "__main__":
    try:
        recorder = ScreenRecorder(duration=10)
        recorder.start()
    except KeyboardInterrupt:
        recorder.stop()
        print("\n[-] Qeydiyyat dayandırıldı.")
