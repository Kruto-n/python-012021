class Auto:
    def __init__(self, registracniznacka, typ, kilometry, dostupnost = True):
        self.registracniznacka = registracniznacka
        self.typ = typ
        self.kilometry = kilometry
        self.dostupnost = dostupnost
    def getInfo(self):
        return f"Auto ma registracni znacku {self.registracniznacka}, typ {self.typ}, najeto {self.kilometry} a dostupnost je {self.dostupnost}."
peugeot = Auto("4A2 3020", "Peugeot 403 Cabrio", "47534" )
skoda = Auto("1P3 4747", "Škoda Octavia", "41253")
print(peugeot.getInfo())