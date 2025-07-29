import subprocess
import os
import glob

NSE_PATH = "/usr/share/nmap/scripts"

def list_nse_scripts():
    scripts = glob.glob(os.path.join(NSE_PATH, "*.nse"))
    return [os.path.basename(s) for s in scripts]

def run_nmap(domain):
    print("""
    =========================
         Nmap Scan Options
    =========================
    [1] Quick Scan (-T4 -F)
    [2] Full Port Scan (-p-)
    [3] Version Detection (-sV)
    [4] Vulnerability Scan (vuln scripts)
    [5] Choose NSE Script from List
    """)
    choice = input("Select an option: ")

    output_file = f"results/{domain}_nmap.txt"

    # Default command list
    cmd = ["nmap", domain]

    if choice == "1":
        cmd = ["nmap", "-T4", "-F", domain, "-oN", output_file]
    elif choice == "2":
        cmd = ["nmap", "-T4", "-p-", domain, "-oN", output_file]
    elif choice == "3":
        cmd = ["nmap", "-T4", "-sV", domain, "-oN", output_file]
    elif choice == "4":
        # vuln NSE scripts
        cmd = ["nmap", "-T4", "--script", "vuln", domain, "-oN", output_file]
    elif choice == "5":
        scripts = list_nse_scripts()

        print(f"\nFound {len(scripts)} NSE scripts:\n")
        for i, s in enumerate(scripts, 1):
            print(f"[{i}] {s}")

        script_choice = input("\nSelect script number (comma separated for multiple): ")

        try:
            selected = []
            for idx in script_choice.split(","):
                idx = int(idx.strip()) - 1
                if 0 <= idx < len(scripts):
                    selected.append(scripts[idx])

            if not selected:
                print("No valid script selected!")
                return

            selected_scripts = ",".join([os.path.splitext(s)[0] for s in selected])

            cmd = ["nmap", "-T4", "--script", selected_scripts, domain, "-oN", output_file]
        except ValueError:
            print("Invalid input!")
            return
    else:
        print("Invalid option!")
        return

    print(f"\n[+] Running: {' '.join(cmd)}\n")
    subprocess.run(cmd)
    print(f"[+] Nmap results saved to {output_file}")
if __name__ == "__main__":
    domain = input("Enter target IP or domain: ")
    
    # Pastikan folder results wujud
    os.makedirs("results", exist_ok=True)
    
    run_nmap(domain)

