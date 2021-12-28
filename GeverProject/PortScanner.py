import subprocess

l = [20,21,22,23,25,26,53,80,110,119,123,143,161,194,443,995]
ls = str(l)[1:-1]

def scan(ip):
    r = subprocess.run(["nmap", "-p", ls, ip],stdout=subprocess.PIPE,text=True)
    lines = r.stdout.splitlines()
    return lines

print("Port Scanner\n\nTool For Scanning The Most Used Ports")
print("Most Used Ports\n"+ls)
print("\nDo You have The IP?\nThe Default IP Is Your Own IP\n")


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

lines = scan(ip)
slines = []
for i,l in enumerate(lines):
    if("PORT" in l) and ("STATE" in l):
        slines = lines[i:-1]
        break

for l in slines:
    print(l)