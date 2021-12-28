import subprocess

all_secure = True

print("User Scanner\n\nTool For Scanning Users And Their Security\n")

lusers = subprocess.run(["users"],stdout=subprocess.PIPE,text=True).stdout.splitlines()

print("Users: (If You See An Unfamiliar User, That May Be A Security Breach)")
for u in lusers:
    print(u)

lines = subprocess.run(["cat", "/etc/shadow"],stdout=subprocess.PIPE,text=True).stdout.splitlines()

print("\n")

for line in lines:
    l = line.split(":")
    if l[0] in lusers:
        print(l[0] + " : " + l[1])
        if l[1] == "":
            all_secure = False
            print("User Does Not Have A Password!!\n")

print("\n")

if all_secure:
    print("All Users Are Secure And Have Passwords")
else:
    print("Some Users Do Not Have Passwords!!")