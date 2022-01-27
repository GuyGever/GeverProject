#!/usr/bin/env python3
#Use these commands in Kali to install required software:
#  sudo apt install python3-pip
#  pip install python-nmap

import requests
from bs4 import BeautifulSoup

# Import nmap so we can use it for the scan
import nmap
# We import the ipaddress module. We want to use the ipaddress.ip_address(address)
# method to see if we can instantiate a valid ip address to test.
import ipaddress
# We need to create regular expressions to ensure that the input is correctly formatted.
import re

# Regular Expression Pattern to extract the number of ports you want to scan. 
# You have to specify <lowest_port_number>-<highest_port_number> (ex 10-100)
port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
# Initialising the port numbers, will be using the variables later on.
port_min = 0
port_max = 65535

scan_types = {1:"auth",2:"broadcast",3:"brute",4:"vuln",5:"discovery",6:"dos",7:"exploit",8:"external",9:"fuzzer",10:"intrusive",11:"malware",12:"safe",13:"version"}

script = "--script "

# This port scanner uses the Python nmap module.
# You'll need to install the following to get it work on Linux:
# Step 1: sudo apt install python3-pip
# Step 2: pip install python-nmap


# Basic user interface header
print(r"""   _____ ________      ________ _____                  _____  _____   ____       _ ______ _____ _______ 
  / ____|  ____\ \    / /  ____|  __ \                |  __ \|  __ \ / __ \     | |  ____/ ____|__   __|
 | |  __| |__   \ \  / /| |__  | |__) |               | |__) | |__) | |  | |    | | |__ | |       | |   
 | | |_ |  __|   \ \/ / |  __| |  _  /                |  ___/|  _  /| |  | |_   | |  __|| |       | |   
 | |__| | |____   \  /  | |____| | \ \                | |    | | \ \| |__| | |__| | |___| |____   | |   
  \_____|______|   \/   |______|_|  \_\               |_|    |_|  \_\\____/ \____/|______\_____|  |_|   
                                                                                                        """)
print("\n****************************************************************")

# Ask user to input the ip address they want to scan.
while True:
    ip_add_entered = input("\nPlease enter the ip address that you want to scan: ")
    # If we enter an invalid ip address the try except block will go to the except block and say you entered an invalid ip address.
    try:
        ip_address_obj = ipaddress.ip_address(ip_add_entered)
        # The following line will only execute if the ip is valid.
        print("You entered a valid ip address.")
        break
    except:
        ip_address_obj = ip_add_entered
        print("You entered an invalid ip address")
        break


while True:
    # You can scan 0-65535 ports. This scanner is basic and doesn't use multithreading so scanning all the ports is not advised.
    print("Please enter the range of ports you want to scan in format: <int>-<int> (ex would be 60-120)")
    port_range = input("Enter port range: ")
    # We pass the port numbers in by removing extra spaces that people sometimes enter. So if you enter 80 - 90 instead of 80-90 the program will still work.
    port_range_valid = port_range_pattern.search(port_range.replace(" ",""))
    if port_range_valid:
        # We're extracting the low end of the port scanner range the user want to scan.
        port_min = int(port_range_valid.group(1))
        # We're extracting the upper end of the port scanner range the user want to scan.
        port_max = int(port_range_valid.group(2))
        break

while True:
	# print("Please enter the number of the type of scan you wish to run\n1. auth\n2. broadcast\n3. brute\n4. vuln\n5. discovery\n6. dos\n7. exploit\n8. external\n9. fuzzer\n10. intrusive\n11. malware\n12. safe\n13. version\n(go to https://nmap.org/book/nse-usage.html to see what does each type do)")
	# scan_type_number = int(input())
	
	script = "--script " + "discovery" # scan_types[scan_type_number]
	print("")
	break


nm = nmap.PortScanner()
# We're looping over all of the ports in the specified range.
for port in range(port_min, port_max + 1):
    try:
        # The result is quite interesting to look at. You may want to inspect the dictionary it returns. 
        # It contains what was sent to the command line in addition to the port status we're after. 
        # For in nmap for port 80 and ip 10.0.0.2 you'd run: nmap -oX - -p 89 -sV 10.0.0.2
        result = nm.scan(ip_add_entered, str(port))
        
        # print(nm.command_line())
        ip_address_obj = (list(result['scan'].keys())[0])
        
        port_status = (result['scan'][ip_address_obj]['tcp'][port]['state'])
        port_service = (result['scan'][ip_address_obj]['tcp'][port]['name'])
        print(f"Port {port} is {port_status}. The service that runs on this port is {port_service}.")
        print()
        print(f"https://www.exploit-db.com/search?port={port}&verified=true")
        print("-------------------------")
    except:
        # We cannot scan some ports and this ensures the program doesn't crash when we try to scan them.
        print(f"Cannot scan port {port}.")
        print("\n")

# HEADERS = {
#     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
# }
# URL = "https://www.exploit-db.com/search?port=80"
# page = requests.get(URL,headers=HEADERS)
# # soup = BeautifulSoup(page.content, "html.parser")

# # table = soup.find('tbody',id="exploits-table")

# print(page)
