import cv2
import time
import os

class CameraMonitor:
    def __init__(self, video_source=0, video_duration=10, output_dir='./'):
        self.video_source = video_source
        self.video_duration = video_duration
        self.output_dir = output_dir
        
        # Fayl yolunu yoxlayırıq
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        self.capture = cv2.VideoCapture(self.video_source)

        # Kamera açılmasını yoxlayırıq
        if not self.capture.isOpened():
            print("Kamera açıla bilmədi!")
            exit()

        # Video codec və yazıcı
        fourcc = cv2.VideoWriter_fourcc(*'MJPG')  # Codec olaraq MJPG istifadə edirik
        self.frame_rate = 20.0
        self.frame_width = int(self.capture.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.frame_height = int(self.capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

        self.writer = None
        self.start_time = time.time()

    def start_recording(self):
        file_index = 1
        while True:
            # Hər bir kadrı oxuyuruq
            ret, frame = self.capture.read()
            if not ret:
                print("Kamera qırıldı.")
                break

            # Hər 10 saniyədə bir yeni fayl açırıq
            elapsed_time = time.time() - self.start_time
            if elapsed_time >= self.video_duration:
                if self.writer:
                    self.writer.release()
                
                # Yeni video faylı adı
                video_filename = f"{self.output_dir}output_{file_index}.avi"
                self.writer = cv2.VideoWriter(video_filename, cv2.VideoWriter_fourcc(*'MJPG'), self.frame_rate, (self.frame_width, self.frame_height))
                print(f"Yeni video faylı yaradıldı: {video_filename}")
                
                # Yeni faylda yazmağa başla
                self.start_time = time.time()  # Zamanı sıfırlamaq
                file_index += 1
            
            # Kadrı video faylına yazmaq
            if self.writer:
                self.writer.write(frame)

            # Görüntünü ekranda göstərmək
            cv2.imshow('Kamera Izleme', frame)

            # 'q' düyməsinə basıldıqda proqram dayandırılacaq
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Kameranı və yazıcını bağlayırıq
        self.capture.release()
        self.writer.release()
        cv2.destroyAllWindows()

# Kamera izləmə və qeydiyyat başlatma
camera_monitor = CameraMonitor(video_duration=10)  # Hər 10 saniyədə bir video faylı yaradacaq
camera_monitor.start_recording()
