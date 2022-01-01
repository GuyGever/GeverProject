import subprocess
import nmap #pythom-nmap

# import socket
# print(socket.gethostbyname(socket.gethostname()))

l = [20,21,22,23,25,26,53,80,110,119,123,143,161,194,443,995]
ls = str(l)[1:-1]

print("Port Scanner\n\nTool For Scanning The Most Used Ports")
print("Most Used Ports\n"+ls)
print("\nDo You have The IP?\nThe Default IP Is Your Own IP\n")
print("Scanning Ports Outside Your LAN Will Be Slower To Make Sure You Are Not Detected \n")

c = input("(Y/N)\n")
ip = None

if c.lower() == "n":
    r = subprocess.run(["ifconfig","eth0"],stdout=subprocess.PIPE,text=True)
    lines = r.stdout.splitlines()
    for i,l in enumerate(lines):
        if ("eth0" in l):
            ip = lines[i+1].split()[1]
            print("\nFound IP:" + ip +"\n")
            break
        else:
            print("Could Not Find IP. Enter Manually.")

elif c.lower() == "y":
    ip = input("Enter IP\n")
    
else:
    print("Error")
    quit()

print("\nIf You See Ports That Are Open, But They're Supposed To Be Close.\nIt May Be A Security Breach.")

nmScan = nmap.PortScanner()

nmScan.scan(ip, ls)

for host in nmScan.all_hosts():
     print("Host : {0} ({1})".format(host, nmScan[host].hostname()))
     print("State : {0}".format(nmScan[host].state()))
     for proto in nmScan[host].all_protocols():
         print('----------')
         print("Protocol : {0}".format(proto))
 
         lport = nmScan[host][proto].keys()
         for port in lport:
             print("port : {0}\tstate : {1}".format(port, nmScan[host][proto][port]['state']))