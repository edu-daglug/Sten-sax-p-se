def spela():
    import random
    val = ["sten", "sax", "påse"]
    datorval = random.choice(val)
    spelarensval = input("Välj sten, sax eller påse ->")
    print(f"{spelarnamn} spelar: {spelarensval}")
    print(f"Pyhton311 spelar: {datorval}")
    if spelarensval == datorval:
        print(f"vinare i spelomgång {i}: Oavgjort!")
    elif (spelarensval == "sten" and datorval == "sax") or (spelarensval == "sax" and datorval == "påse") or (spelarensval == "påse" and datorval == "sten"):
        print(f"vinare i spelomgång {i}: {spelarnamn}!")
    else:
        print(f"vinare i spelomgång {i}: Pyhton311!")
    

print("Nu ska vi köra sten, sax eller påse!\nJag är Pyhton311\n")
spelarnamn=input("Ange ditt spelarnamn ->")
spelomgångar=int(input("Ange hur många omgångar vi ska spela? ->"))
i=1
while i <= spelomgångar:
    print(f"Spelomgång {i}\n-------------")
    spela()
    i+= 1