import subprocess
import os
from datetime import datetime

def run_subfinder(domain):
    print("""
    =========================
       Subfinder Scan Options
    =========================
    [1] Passive (default)
    [2] Passive + Recursive (-recursive)
    [3] All Sources (-all)
    [4] Specific Sources (-s)
    [5] Exclude Sources (-es)
    [6] Bruteforce (-b + wordlist)
    [7] Active Only (-nW)
    [8] Custom Rate-Limit / Threads (-rl / -t)
    [9] Update Subfinder (-up)
    """)
    choice = input("Select an option: ")

    os.makedirs("results", exist_ok=True)

    # Map choice ke label untuk file output
    choice_labels = {
        "1": "passive",
        "2": "recursive",
        "3": "all",
        "4": "specific",
        "5": "exclude",
        "6": "bruteforce",
        "7": "active",
        "8": "custom",
        "9": "update"
    }

    label = choice_labels.get(choice, "unknown")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"results/{domain}_{label}_{timestamp}.txt"

    if choice == "1":
        cmd = ["subfinder", "-d", domain, "-o", output_file]

    elif choice == "2":
        cmd = ["subfinder", "-d", domain, "-recursive", "-o", output_file]

    elif choice == "3":
        cmd = ["subfinder", "-d", domain, "-all", "-o", output_file]

    elif choice == "4":
        sources = input("Enter specific sources (comma-separated): ")
        cmd = ["subfinder", "-d", domain, "-s", sources, "-o", output_file]

    elif choice == "5":
        exclude = input("Enter sources to exclude (comma-separated): ")
        cmd = ["subfinder", "-d", domain, "-es", exclude, "-o", output_file]

    elif choice == "6":
        wordlist = input("Enter wordlist path (default: /usr/share/wordlists/seclists/Discovery/DNS/dns-Jhaddix.txt): ")
        if not wordlist:
            wordlist = "/usr/share/wordlists/seclists/Discovery/DNS/dns-Jhaddix.txt"
        cmd = ["subfinder", "-d", domain, "-b", "-w", wordlist, "-o", output_file]

    elif choice == "7":
        cmd = ["subfinder", "-d", domain, "-nW", "-o", output_file]

    elif choice == "8":
        rl = input("Enter rate limit (req/sec, e.g. 50): ")
        threads = input("Enter number of threads (default 10): ")
        cmd = ["subfinder", "-d", domain, "-rl", rl, "-t", threads, "-o", output_file]

    elif choice == "9":
        cmd = ["subfinder", "-up"]
        print(f"\n[+] Running: {' '.join(cmd)}\n")
        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            if "permission denied" in result.stderr.lower():
                print("[!] Update failed: Permission denied.")
                print("[i] Try running the following command manually with sudo:\n")
                print("    sudo subfinder -up\n")
            else:
                print(result.stdout)
                print("[+] Subfinder updated!")
        except FileNotFoundError:
            print("[!] subfinder is not installed or not in PATH!")
        return

    else:
        print("Invalid option!")
        return

    print(f"\n[+] Running: {' '.join(cmd)}\n")
    try:
        subprocess.run(cmd, check=True)
        print(f"[+] Subfinder results saved to {output_file}")
    except FileNotFoundError:
        print("[!] subfinder is not installed or not in PATH!")
    except subprocess.CalledProcessError:
        print("[!] Subfinder failed to run!")

if __name__ == "__main__":
    domain = input("Enter target domain: ")
    run_subfinder(domain)

