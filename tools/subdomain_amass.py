import subprocess
import os
import shutil
from datetime import datetime

def check_tool_installed(tool_name):
    """Check kalau tool ada, kalau tak ada tanya nak install ke tak"""
    if shutil.which(tool_name) is None:
        choice = input(f"[!] {tool_name} is not installed. Do you want to install it now? (y/n): ")
        if choice.lower() == "y":
            try:
                print(f"[+] Installing {tool_name} ...")
                subprocess.run(f"sudo apt install -y {tool_name}", shell=True, check=True)
                print(f"[+] {tool_name} installed successfully!")
            except subprocess.CalledProcessError:
                print(f"[!] Failed to install {tool_name}! Please install manually.")
                exit(1)
        else:
            print(f"[!] {tool_name} is required. Exiting...")
            exit(1)

def run_amass(domain):
    check_tool_installed("amass")   # <-- Check dulu

    print("""
    =========================
         Amass Scan Options
    =========================
    [1] Passive (default)
    [2] Active Enumeration (-active)
    [3] Brute Force (-brute)
    [4] Recursive Enumeration (-rf)
    [5] Custom Wordlist (-brute -w)
    [6] Custom Rate-Limit / Threads (-max-dns-queries)
    [7] Update Amass
    """)
    choice = input("Select an option: ")

    os.makedirs("results", exist_ok=True)

    choice_labels = {
        "1": "passive",
        "2": "active",
        "3": "bruteforce",
        "4": "recursive",
        "5": "wordlist",
        "6": "custom",
        "7": "update"
    }

    label = choice_labels.get(choice, "unknown")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"results/{domain}_amass_{label}_{timestamp}.txt"

    # base command ikut pilihan
    if choice == "1":
        cmd = ["amass", "enum", "-passive", "-d", domain, "-o", output_file]
    elif choice == "2":
        cmd = ["amass", "enum", "-active", "-d", domain, "-o", output_file]
    elif choice == "3":
        cmd = ["amass", "enum", "-brute", "-d", domain, "-o", output_file]
    elif choice == "4":
        cmd = ["amass", "enum", "-brute", "-dir", "output", "-d", domain, "-o", output_file]
    elif choice == "5":
        wordlist = input("Enter wordlist path (default: /usr/share/wordlists/seclists/Discovery/DNS/dns-Jhaddix.txt): ")
        if not wordlist:
            wordlist = "/usr/share/wordlists/seclists/Discovery/DNS/dns-Jhaddix.txt"
        cmd = ["amass", "enum", "-brute", "-w", wordlist, "-d", domain, "-o", output_file]
    elif choice == "6":
        rate = input("Enter max DNS queries per second (default 200): ")
        if not rate:
            rate = "200"
        cmd = ["amass", "enum", "-d", domain, "-max-dns-queries", rate, "-o", output_file]
    elif choice == "7":
        cmd = ["amass", "update"]
        print(f"\n[+] Running: {' '.join(cmd)}\n")
        subprocess.run(cmd)
        return
    else:
        print("Invalid option!")
        return

    print(f"\n[+] Running: {' '.join(cmd)}\n")
    subprocess.run(cmd)

    if os.path.exists(output_file):
        with open(output_file, "r") as f:
            lines = [line.strip() for line in f if line.strip()]
        print(f"\n[+] Scan complete! {len(lines)} subdomains found.")
        print(f"[+] Amass results saved to {output_file}")

if __name__ == "__main__":
    domain = input("Enter target domain: ")
    run_amass(domain)

