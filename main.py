import random

def spela():
    val = ["sten", "sax", "påse"]
    datorval = random.choice(val)
    spelarensval = input("Välj sten, sax eller påse ->")
    print(f"{spelarnamn} spelar: {spelarensval}")
    print(f"Pyhton311 spelar: {datorval}")
    if spelarensval == datorval:
        print(f"vinare i spelomgång {i}: Oavgjort!")
    elif (spelarensval == "sten" and datorval == "sax") or (spelarensval == "sax" and datorval == "påse") or (spelarensval == "påse" and datorval == "sten"):
        print(f"vinare i spelomgång {i}: {spelarnamn}!")
        return "spelare"
    else:
        print(f"vinare i spelomgång {i}: Pyhton311!")
        return "dator"

print("Nu ska vi köra sten, sax eller påse!\nJag är Pyhton311\n")
spelarnamn=input("Ange ditt spelarnamn ->")
spelomgångar=int(input("Ange hur många omgångar vi ska spela? ->"))

spelare_p = 0
dator_p = 0
i=1

while i <= spelomgångar:
    print(f"Spelomgång {i}\n-------------")
    result = spela()
    if result == "spelare":
        spelare_p += 1
    elif result == "dator":
        dator_p += 1
    i+= 1
print(f"{dator_p} {spelare_p}")