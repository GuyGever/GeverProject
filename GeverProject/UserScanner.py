import pwd, grp
import subprocess
from sys import stdout
from typing import Text

print("Would You Rather The Full User Scan")
c = input("Y/N ? ")

if (c.lower() == 'y'): 
    for p in pwd.getpwall():
        print (p[0], grp.getgrgid(p[3])[0])
elif (c.lower() == 'n'):
    l = subprocess.run(["users"],stdout=subprocess.PIPE,text=True).stdout.split()
    for u in l:
        print(u)

print("\nUsers Log: (since two days ago)\n")
logs = subprocess.run(["last","--since","-2days"],stdout=subprocess.PIPE,text=True).stdout.split("\n")
for log in logs:
    print(log)

print("\nBad Login Attempts: (since two days ago)\n")
logs = subprocess.run(["lastb","--since","-2days"],stdout=subprocess.PIPE,text=True).stdout.split("\n")
for log in logs:
    print(log)