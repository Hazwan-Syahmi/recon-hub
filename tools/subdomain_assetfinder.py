import subprocess
import os
from datetime import datetime

def run_assetfinder(domain):
    print("""
    =============================
         Assetfinder Options
    =============================
    [1] Default (passive only)
    [2] Include Subdomains (--subs-only)
    [3] Custom Wordlist (use with grep)
    [4] Update Assetfinder (go install)
    """)

    choice = input("Select an option: ")

    # Buat folder results
    os.makedirs("results", exist_ok=True)

    choice_labels = {
        "1": "default",
        "2": "subs-only",
        "3": "custom",
        "4": "update"
    }

    label = choice_labels.get(choice, "unknown")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"results/{domain}_assetfinder_{label}_{timestamp}.txt"

    if choice == "1":
        cmd = ["assetfinder", domain]

    elif choice == "2":
        cmd = ["assetfinder", "--subs-only", domain]

    elif choice == "3":
        wordlist = input("Enter path to custom wordlist: ")
        if not os.path.exists(wordlist):
            print("[!] Wordlist not found!")
            return
        cmd = ["bash", "-c", f"cat {wordlist} | assetfinder {domain}"]

    elif choice == "4":
        print("\n[+] Updating assetfinder...\n")
        try:
            subprocess.run("go install github.com/tomnomnom/assetfinder@latest", shell=True, check=True)
            print("[+] Assetfinder updated successfully!")
        except subprocess.CalledProcessError:
            print("[!] Failed to update assetfinder! Pastikan Go ada.")
        return

    else:
        print("[!] Invalid option!")
        return

    print(f"\n[+] Running: {' '.join(cmd)}\n")
    try:
        # Jalankan command dan tulis ke file + tunjuk output live
        with open(output_file, "w") as out_file:
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            count = 0
            for line in process.stdout:
                print(line.strip())
                if line.strip():
                    count += 1
                    out_file.write(line)

            process.wait()

        print(f"\n[+] Scan complete! {count} subdomains found.")
        print(f"[+] Results saved to {output_file}")

    except FileNotFoundError:
        print("[!] assetfinder is not installed or not in PATH!")
    except subprocess.CalledProcessError:
        print("[!] Assetfinder failed to run!")

if __name__ == "__main__":
    domain = input("Enter target domain: ")
    run_assetfinder(domain)

