import random

def spela():
    val = ["sten", "sax", "påse"]
    datorval = random.choice(val)
    while True:
        spelarensval = input("Välj sten, sax eller påse ->").lower()
        if spelarensval in val:
            break  
    print(f"{spelarnamn} spelar: {spelarensval}")
    print(f"Pyhton311 spelar: {datorval}")
    if spelarensval == datorval:
        print(f"\nvinnare i spelomgång {i}: Oavgjort!")
    elif (spelarensval == "sten" and datorval == "sax") or (spelarensval == "sax" and datorval == "påse") or (spelarensval == "påse" and datorval == "sten"):
        print(f"\nvinnare i spelomgång {i}: {spelarnamn}!")
        return "spelare"
    else:
        print(f"\nvinnare i spelomgång {i}: Pyhton311!")
        return "dator"

print("Nu ska vi köra sten, sax eller påse!\nJag är Pyhton311\n")
spelarnamn=input("Ange ditt spelarnamn ->")
spelomgångar=int(input("Ange hur många omgångar vi ska spela? ->"))

spelare_p = 0
dator_p = 0
i=1

while i <= spelomgångar:
    print(f"\n\nSpelomgång {i}\n-------------")
    result = spela()
    if result == "spelare":
        spelare_p += 1
    elif result == "dator":
        dator_p += 1
    i+= 1
print("\n\nRESULTAT\n=============")
if spelare_p > dator_p:
    print(f"{spelarnamn}: {spelare_p}p\nPyhton311: {dator_p}p\n\nVinnare: {spelarnamn}")
elif spelare_p < dator_p:
    print(f"{spelarnamn}: {spelare_p}p\nPyhton311: {dator_p}p\n\nVinnare: Pyhton311")
else:
    print(f"{spelarnamn}: {spelare_p}p\nPyhton311: {dator_p}p\n\nVinnare: Oavgjort!")
print("programmet avslutades normalt")