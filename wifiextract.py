import subprocess
import re

def get_saved_profiles():
    output = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors='ignore')
    profiles = re.findall("All User Profile\\s*:\\s(.*)", output)
    return [p.strip() for p in profiles]

def get_password(profile):
    output = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8', errors='ignore')
    password = re.search("Key Content\\s*:\\s(.*)", output)
    return password.group(1).strip() if password else "Tapılmadı"

print("[+] Saxlanılan Wi-Fi şəbəkələri və şifrələri:\n")
profiles = get_saved_profiles()
for profile in profiles:
    pwd = get_password(profile)
    print(f"SSID: {profile} | Şifrə: {pwd}")
