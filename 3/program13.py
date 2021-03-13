class Auto:
    def __init__(self, registracniznacka, typ, kilometry, dostupnost = True):
        self.registracniznacka = registracniznacka
        self.typ = typ
        self.kilometry = kilometry
        self.dostupnost = dostupnost
    def getInfo(self):
        return f"Auto ma registracni znacku {self.registracniznacka}, typ {self.typ}, najeto {self.kilometry}."
    def pujc_auto(self):
        if self.dostupnost == True:
            self.dostupnost = False
            print("Potvrzuji zapůjčení vozidla.")
        else:
            print("Vozidlo není k dispozici.")
    def vrat_auto(self, tachometr, dny):
        self.tachometr = tachometr
        self.dny = dny
        self.dostupnost = True
        if dny < 7:
            cena = 400 * dny
        else:
            cena = 300 * dny
        return f"Cena pujcovneho je {cena}"



peugeot = Auto("4A2 3020", "Peugeot 403 Cabrio", "47534" )
skoda = Auto("1P3 4747", "Škoda Octavia", "41253")

pujcit = input("Jakou znacku auta si prejete pujcit - skoda nebo peugeot?")
if pujcit == "peugeot":
    print(peugeot.getInfo())
    print(peugeot.pujc_auto())
if pujcit == "skoda" or "škoda":
    print(skoda.getInfo())
    print(skoda.pujc_auto())

tachometr = int(input("Kolik kilometru jste s autem ujel?"))
dny = int(input("Jak dlouho jste mel auto pujcene?"))
if pujcit == "peugeot":
    print(peugeot.vrat_auto(tachometr, dny))
if pujcit == "skoda" or "škoda":
    print(skoda.vrat_auto(tachometr, dny))