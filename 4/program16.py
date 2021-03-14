class Polozka:
    def __init__(self, name, zanr):
        self.name = name
        self.zanr = zanr
    def get_info(self):
        return f"Nazev polozky je {self.name} a zanr je {self.zanr}."

class Film(Polozka):
    def __init__(self, name, zanr, delka):
        super().__init__(name, zanr)
        self.delka = delka
    def get_info(self):
        return f"Nazev polozky je {self.name}, zanr {self.zanr}, delka {self.delka} minut"

class Serial(Polozka):
    def __init__(self, name, zanr, epizody, delkaepizody):
        super().__init__(name, zanr)
        self.epizody = epizody
        self.delkaepizody = delkaepizody
    def get_info(self):
        return f"Nazev polozky je {self.name}, zanr {self.zanr}, pocet epizod {self.epizody}, delka epizody {self.delkaepizody} minut."

ratatouille = Film("Ratatouille", "komedie", 120)
pratele = Serial("Pratele", "komedie", 236, 20)

print(ratatouille.get_info())
print(pratele.get_info())