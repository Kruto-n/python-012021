class Auto:
    def __init__(self, registracniznacka, typ, kilometry, dostupnost = True):
        self.registracniznacka = registracniznacka
        self.typ = typ
        self.kilometry = kilometry
        self.dostupnost = dostupnost

peugeot = Auto("4A2 3020", "Peugeot 403 Cabrio", "47534" )
skoda = Auto("1P3 4747", "Škoda Octavia", "41253")
