import random
from tqdm import tqdm
import time

sterrenbeelden = (
    "ram", "stier", "tweeling", "kreeft", "leeuw", "maagd", "weegschaal",
    "schorpioen", "boogschutter", "steenbok", "waterman", "vis", "adelaar",
    "dolfijn", "goudvis", "draak", "wolf", "lynx", "phoenix", "pegasus",
    "zwaan", "hercules", "waterslang", "hagedis", "eenhoorn", "orion"
)

def spel():
    spel = 0
    print('1) Cycles voor kansberekeningen.')
    while spel != 1:
        try:
            spel = int(input("Kies uit 1 van de menu's door het getal in te geven.  "))
        except:
            spel = 0
        if spel != 1:
            spel = 0
            print('Dit is geen keuze')
    if spel == 1:
        ticket()
        cyclefunction()
          
def cyclefunction():
    cycles = int(input("Geef het aantal cycles.  "))
    start = time.perf_counter()
    Prijs0 = 0
    Prijs1 = 0
    Prijs2 = 0
    Prijs3 = 0
    Prijs4 = 0
    Prijs5 = 0
    Prijs6 = 0
    Prijs7 = 0
    Prijs8 = 0
    Prijs9 = 0
    for i in tqdm(range(cycles)):
        win()
        TijdelijkPrijzen = check()
        if TijdelijkPrijzen[0] == 1:
            Prijs0 += 1
        if TijdelijkPrijzen[1] == 1:
            Prijs1 += 1
        if TijdelijkPrijzen[2] == 1:
            Prijs2 += 1
        if TijdelijkPrijzen[3] == 1:
            Prijs3 += 1
        if TijdelijkPrijzen[4] == 1:
            Prijs4 += 1
        if TijdelijkPrijzen[5] == 1:
            Prijs5 += 1
        if TijdelijkPrijzen[6] == 1:
            Prijs6 += 1
        if TijdelijkPrijzen[7] == 1:
            Prijs7 += 1
        if TijdelijkPrijzen[8] == 1:
            Prijs8 += 1
        if TijdelijkPrijzen[9] == 1:
            Prijs9 += 1

    print()
    print("Uitgedeelde prijzen:")
    print("Geen prijs:", Prijs0, "/", (Prijs0 / cycles) * 100, "%")
    print("2€ prijs:", Prijs1, "/", (Prijs1 / cycles) * 100, "%")
    print("3€ prijs:", Prijs2, "/", (Prijs2 / cycles) * 100, "%")
    print("5€ prijs:", Prijs3, "/", (Prijs3 / cycles) * 100, "%")
    print("5€ prijs:", Prijs4, "/", (Prijs4 / cycles) * 100, "%")
    print("50€ prijs:", Prijs5, "/", (Prijs5 / cycles) * 100, "%")
    print("50€ prijs:", Prijs6, "/", (Prijs6 / cycles) * 100, "%")
    print("5000€ prijs:", Prijs7, "/", (Prijs7 / cycles) * 100, "%")
    print("50000€ prijs:", Prijs8, "/", (Prijs8 / cycles) * 100, "%")
    print("1000000 prijs:", Prijs9, "/", (Prijs9 / cycles) * 100, "%")
    finish = time.perf_counter()
    print("Finished in ",round(finish-start, 2),"second(s)")

def check():
    rood = 0
    wit = 0

    if getrokkenticket[0] in winningticket:
        rood += 1
    if getrokkenticket[1] in winningticket:
        rood += 1
    if getrokkenticket[2] in winningticket:
        rood += 1
    if getrokkenticket[3] in winningticket:
        rood += 1
    if getrokkenticket[4] in winningticket:
        rood += 1
    if getrokkenticket[5] in winningticket:
        wit += 1

    prijs0 = 0
    prijs1 = 0
    prijs2 = 0
    prijs3 = 0
    prijs4 = 0
    prijs5 = 0
    prijs6 = 0
    prijs7 = 0
    prijs8 = 0
    prijs9 = 0

    if wit == 1 and rood == 0:
        prijs1 += 1
    elif wit == 1 and rood == 1:
        prijs2 += 1
    elif wit == 1 and rood == 2:
        prijs3 += 1
    elif wit == 0 and rood == 3:
        prijs4 += 1
    elif wit == 1 and rood == 3:
        prijs5 += 1
    elif wit == 0 and rood == 4:
        prijs6 += 1
    elif wit == 1 and rood == 4:
        prijs7 += 1
    elif wit == 0 and rood == 5:
        prijs8 += 1
    elif wit == 1 and rood == 5:
        prijs9 += 1
    else:
        prijs0 += 1
    TijdelijkPrijzen = [
        prijs0, prijs1, prijs2, prijs3, prijs4, prijs5, prijs6, prijs7, prijs8,
        prijs9
    ]
    return TijdelijkPrijzen

def win():
    global winningticket

    winningticket = ["", "", "", "", ""]

    for i in range(0, 5):
        winningticket[i - 1] = random.randrange(1, 55, 1)
        while winningticket.count(winningticket[i - 1]) > 1:
            winningticket[i - 1] = random.randrange(1, 55, 1)
    winningticket.sort()

    winsterrenbeeld = random.choice(sterrenbeelden)
    winningticket.append(winsterrenbeeld)

def ticket():
    global getrokkenticket
    getrokkenticket = ["", "", "", "", ""]

    print("Geef 5 getallen tussen 1 en 55.")

    for i in range(0, 5):
        getrokkenticket[i - 1] = int(input("Geef een getal.  "))

        while getrokkenticket[i - 1] > 55 or getrokkenticket[i - 1] < 1:
            print("Het gebruikte getal zit niet tussen 1 en 55")
            getrokkenticket[i - 1] = int(
                input("Geef een getal tussen 1 en 55.  "))
        while getrokkenticket.count(getrokkenticket[i - 1]) > 1:
            print("Je hebt dit getal al eens gebruikt, probeer opnieuw.")
            getrokkenticket[i - 1] = int(
                input("Geef een getal tussen 1 en 55.  "))
    getrokkenticket.sort()

    print("Kies uit deze sterrenbeelden", sterrenbeelden)
    getrokkensterrenbeeld = input("Geef een sterrenbeeld.  ")
    while sterrenbeelden.count(getrokkensterrenbeeld) != 1:
        print("Het sterrenbeeld staat niet in de lijst.")
        getrokkensterrenbeeld = input("Geef een sterrenbeeld.  ")
    getrokkenticket.append(getrokkensterrenbeeld)
    print("Dit is je ticket", getrokkenticket)

spel()
input()
