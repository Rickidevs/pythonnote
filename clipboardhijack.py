import pyperclip
import time
from datetime import datetime

def monitor_clipboard():
    # İlkin qurulum
    print("Aktiv Clipboard Monitor başladı...")
    print("Ctrl+C ile proqramı dayandıra bilərsiniz")
    
    # Fayl adını təyin et
    file_name = "clipboard_history.txt"
    last_content = ""
    
    try:
        while True:
            # Clipboard məzmununu al
            current_content = pyperclip.paste()
            
            # Əgər məzmun dəyişibsə və boş deyilsə
            if current_content != last_content and current_content.strip():
                # Yeni məzmunu fayla yaz
                with open(file_name, 'a', encoding='utf-8') as f:
                    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    f.write(f"\n\n=== {timestamp} ===\n")
                    f.write(current_content)
                
                print(f"[{timestamp}] Yeni məzmun fayla yazıldı")
                last_content = current_content
            
            # Yoxlama aralığı (1 saniyə)
            time.sleep(1)
    
    except KeyboardInterrupt:
        print("\nProqram dayandırıldı")
    except Exception as e:
        print(f"Xəta baş verdi: {e}")

if __name__ == "__main__":
    monitor_clipboard()
