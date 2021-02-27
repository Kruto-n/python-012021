baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}
kod = 0
kod = input("Jaky je kod vaseho baliku?")
if kod in baliky:
    if baliky[kod] == True:
        print("Balík byl předán kurýrovi")
    else:
        print("Balík zatím nebyl předán kurýrovi")

#Ráda bych se zeptala, proč v řádce 10 musí být if a ne for