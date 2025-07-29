import os
import sys
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def banner():
    os.system("clear")
    print(Fore.CYAN + """
     ██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗    ██╗  ██╗██╗   ██╗██████╗ 
    ██╔═══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║    ██║ ██╔╝██║   ██║██╔══██╗
    ██║   ██║█████╗  ██║     ██║   ██║██╔██╗ ██║    █████╔╝ ██║   ██║██║  ██║
    ██║   ██║██╔══╝  ██║     ██║   ██║██║╚██╗██║    ██╔═██╗ ██║   ██║██║  ██║
    ╚██████╔╝███████╗╚██████╗╚██████╔╝██║ ╚████║    ██║  ██╗╚██████╔╝██████╔╝
     ╚═════╝ ╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝    ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ 

                """ + Fore.YELLOW + ">>> Recon Hub - Compiled by k1dd0sz <<<\n" + Style.RESET_ALL)


def main_menu():
    print(Fore.GREEN + """
    [1] Subdomain Enumeration
    [2] DNS Enumeration & Zone Transfer
    [3] Port & Service Scan
    [4] Directory & File Bruteforce
    [5] Parameter & Endpoint Finder
    [6] Content Discovery & Takeover

    [0] Exit
    """ + Style.RESET_ALL)


def run_script(script_name):
    base_dir = os.path.dirname(os.path.abspath(__file__))  # folder recon-hub
    tool_path = os.path.join(base_dir, "tools", f"{script_name}.py")
    os.system(f"python3 {tool_path}")



def submenu_subdomain():
    print(Fore.YELLOW + """
    === Subdomain Enumeration ===
    [1] subfinder
    [2] amass
    [3] assetfinder
    [0] Back
    """ + Style.RESET_ALL)
    choice = input(Fore.CYAN + "Select a tool: " + Style.RESET_ALL)

    if choice == "1":
        run_script("subdomain_subfinder")
    elif choice == "2":
        run_script("subdomain_amass")
    elif choice == "3":
        run_script("subdomain_assetfinder")
    elif choice == "0":
        return
    else:
        print(Fore.RED + "Invalid choice!")
    input(Fore.MAGENTA + "\nPress Enter to return..." + Style.RESET_ALL)


def submenu_dns():
    print(Fore.YELLOW + """
    === DNS Enumeration ===
    [1] dnsenum
    [2] dnsx
    [3] dig (manual)
    [0] Back
    """ + Style.RESET_ALL)
    choice = input(Fore.CYAN + "Select a tool: " + Style.RESET_ALL)

    if choice == "1":
        run_script("dns_dnsenum")
    elif choice == "2":
        run_script("dns_dnsx")
    elif choice == "3":
        run_script("dns_dig")
    elif choice == "0":
        return
    else:
        print(Fore.RED + "Invalid choice!")
    input(Fore.MAGENTA + "\nPress Enter to return..." + Style.RESET_ALL)


def submenu_portscan():
    print(Fore.YELLOW + """
    === Port & Service Scan ===
    [1] nmap (+ NSE)
    [2] naabu
    [3] masscan
    [0] Back
    """ + Style.RESET_ALL)
    choice = input(Fore.CYAN + "Select a tool: " + Style.RESET_ALL)

    if choice == "1":
        run_script("portscan_nmap")
    elif choice == "2":
        run_script("portscan_naabu")
    elif choice == "3":
        run_script("portscan_masscan")
    elif choice == "0":
        return
    else:
        print(Fore.RED + "Invalid choice!")
    input(Fore.MAGENTA + "\nPress Enter to return..." + Style.RESET_ALL)


def submenu_dirbrute():
    print(Fore.YELLOW + """
    === Directory & File Bruteforce ===
    [1] dirsearch
    [2] ffuf
    [3] gobuster
    [0] Back
    """ + Style.RESET_ALL)
    choice = input(Fore.CYAN + "Select a tool: " + Style.RESET_ALL)

    if choice == "1":
        run_script("dir_dirsearch")
    elif choice == "2":
        run_script("dir_ffuf")
    elif choice == "3":
        run_script("dir_gobuster")
    elif choice == "0":
        return
    else:
        print(Fore.RED + "Invalid choice!")
    input(Fore.MAGENTA + "\nPress Enter to return..." + Style.RESET_ALL)


def submenu_params():
    print(Fore.YELLOW + """
    === Parameter & Endpoint Finder ===
    [1] paramspider
    [2] waybackurls
    [3] gau (getallurls)
    [0] Back
    """ + Style.RESET_ALL)
    choice = input(Fore.CYAN + "Select a tool: " + Style.RESET_ALL)

    if choice == "1":
        run_script("params_paramspider")
    elif choice == "2":
        run_script("params_waybackurls")
    elif choice == "3":
        run_script("params_gau")
    elif choice == "0":
        return
    else:
        print(Fore.RED + "Invalid choice!")
    input(Fore.MAGENTA + "\nPress Enter to return..." + Style.RESET_ALL)


def submenu_content():
    print(Fore.YELLOW + """
    === Content Discovery & Takeover ===
    [1] httpx
    [2] subjack
    [3] eyewitness
    [0] Back
    """ + Style.RESET_ALL)
    choice = input(Fore.CYAN + "Select a tool: " + Style.RESET_ALL)

    if choice == "1":
        run_script("content_httpx")
    elif choice == "2":
        run_script("content_subjack")
    elif choice == "3":
        run_script("content_eyewitness")
    elif choice == "0":
        return
    else:
        print(Fore.RED + "Invalid choice!")
    input(Fore.MAGENTA + "\nPress Enter to return..." + Style.RESET_ALL)


def main():
    while True:
        banner()
        main_menu()
        choice = input(Fore.CYAN + "Select a category: " + Style.RESET_ALL)

        if choice == "1":
            submenu_subdomain()
        elif choice == "2":
            submenu_dns()
        elif choice == "3":
            submenu_portscan()
        elif choice == "4":
            submenu_dirbrute()
        elif choice == "5":
            submenu_params()
        elif choice == "6":
            submenu_content()
        elif choice == "0":
            print(Fore.CYAN + "\n[!] Thanks for using Recon Hub - k1dd0sz out!\n")
            sys.exit(0)
        else:
            print(Fore.RED + "Invalid option!")
            input("Press Enter...")


if __name__ == "__main__":
    main()

