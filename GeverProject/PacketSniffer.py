import subprocess

print("Packet Sniffer\n\nTool For Finding Out Who Send Data To A Network And Saves To A File\n")

print("Make Sure Your WiFi Adapter Can Be Set To Monitor Mode (wlan0)")
c = input("Is Your WiFi Adapter Already Set To Monitor Mode? (Y/N)\n")

command1 = "ifconfig wlan0 down"
command2 = "iwconfig wlan0 mode monitor"
command3 = "ifconfig wlan0 up"

if c.lower() == "n":
    subprocess.run(command1.split(" "))
    subprocess.run(command2.split(" "))
    subprocess.run(command3.split(" "))
elif c.lower() == "y":
    pass
else:
    print("Error")
    quit()

bssid = input("\nEnter The BSSID Of The Network (With Colons)\n")

sec = input("\nInsert The Amount Of Time Before Stopping The Scan (In Seconds)\n")

lines = subprocess.run(["timeout",sec,"airodump-ng","wlan0"],stdout=subprocess.PIPE,text=True).stdout.splitlines()
