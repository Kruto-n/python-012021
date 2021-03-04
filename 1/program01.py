baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}
kod = input("Jaky je kod vaseho baliku?")
if kod in baliky:
  if baliky[kod]:
    print("Balík byl předán kurýrovi")
  else:
    print("Balík zatím nebyl předán kurýrovi")