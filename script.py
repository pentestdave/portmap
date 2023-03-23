import nmap
import re

from time import perf_counter
from pyfiglet import Figlet
from colorama import Fore, Style, init

# Reset colorama
init(autoreset=True)

# Print ASCII banner
ascii_font = Figlet(font='big')
print(f"{Fore.RED + Style.BRIGHT} {ascii_font.renderText('PORTMAP')}")

# Check if suplied IPv4 address is valid through regex
ip_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")

# Port range pattern
port_pattern = re.compile("([0-9]+)-([0-9]+)")

port_min = 0
port_max = 65535

# Ask user to input the ip address they want to scan.
while True:
    ip_entered = input("Please enter the IP address that you want to scan: ")
    if ip_pattern.search(ip_entered):
        print(f"{Fore.GREEN + Style.BRIGHT}[+] {ip_entered} is a valid IP address")
        print("\n")
        break

# Ask user to enter port range to scan
while True:
    print("Please enter the range of ports you want to scan in format: <int>-<int> (ex would be 60-120)")
    port_range = input("Enter port range: ")
    print("\n")
    port_range_valid = port_pattern.search(port_range.replace(" ",""))
    if port_range_valid:
        port_min = int(port_range_valid.group(1))
        port_max = int(port_range_valid.group(2))
        break

portmap = nmap.PortScanner()

t1 = perf_counter()

def task():
    # Loop through the port from min to max while checking their status
    for port in range(port_min, port_max + 1):
        try:
            result = portmap.scan(ip_entered, str(port))
            port_status = (result['scan'][ip_entered]['tcp'][port]['state'])
            print(f"Port => {port} :: Status => {port_status}")
        except:
            print(f"{Fore.RED + Style.BRIGHT}[!] Unable to scan port => {port}.")

task()

t2 = perf_counter()

print("\n")
print(f"{Fore.GREEN + Style.BRIGHT}[+] Process done in {t2-t1} seconds")