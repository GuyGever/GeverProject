from scapy.all import *
import time
i = int(input("Enter How Much Time Do You Want To Sniff For? "))
a = AsyncSniffer(iface=["eth0","wlan0"])
a.start()
time.sleep(i)
a.stop()
print("Captured {0} Packets".format(len(a.results)))
print(a.results)