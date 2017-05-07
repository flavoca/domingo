print('Hello, Django girls!')
nummer = 8
if nummer > 3 :
    print ("it works")
elif nummer > 5:
    print ("ok")
else:
    print ("sai!")
def oi (name):
    print ("oi " + name + ", tudo?")

    if name == "flavia" :
        print ("oi Flavia, tudo?")
    elif name == "bo" :
        print ("oi bo!")
oi("maria")
oi("alex")
meninas = ["maria", "monica", "luana", "aline"]
for name in meninas:
    oi(name)
    print("Next meninas")
    mysite/settings.py
