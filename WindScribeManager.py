import windscribe #pip install python-windscribe
windscribe.login('<user>', '<password>')

print("Locations:")
loc = windscribe.locations()
for l in loc:
    print(l)
i = input("Choose Location, ")

if i in loc:
    print("inside")
else:
    print("no such location")