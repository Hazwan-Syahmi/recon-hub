import subprocess
import os
from datetime import datetime

def run_amass(domain):
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

    # Map choice ke label untuk file output
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

    # Base command
    cmd = ["amass", "enum", "-d", domain, "-o", output_file]

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
        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            print(result.stdout)
            print("[+] Amass updated!")
        except FileNotFoundError:
            print("[!] amass is not installed or not in PATH!")
        return

    else:
        print("Invalid option!")
        return

    print(f"\n[+] Running: {' '.join(cmd)}\n")
    try:
        subprocess.run(cmd, check=True)

        # Kira berapa result jumpa
        if os.path.exists(output_file):
            with open(output_file, "r") as f:
                lines = [line.strip() for line in f if line.strip()]
            count = len(lines)
            print(f"\n[+] Scan complete! {count} subdomains found.")
            print(f"[+] Amass results saved to {output_file}")
        else:
            print("[!] Scan complete but no results file was created!")

    except FileNotFoundError:
        print("[!] amass is not installed or not in PATH!")
    except subprocess.CalledProcessError:
        print("[!] Amass failed to run!")

if __name__ == "__main__":
    domain = input("Enter target domain: ")
    run_amass(domain)

