#Pokračuj ve své práci pro streamovací službu. Služba nyní eviduje uživatele, kteří službu využívají.
# Vytvoř třídu Uzivatel, která bude mít atributy uzivatelske_jmeno a delka_sledovani, který udává celkovou délku pořadů,
# které uživatel zhlédl. Uživatelské jméno získej jako parametr a délka sledování je na začátku 0.
#Třídám Serial a Film přidej funkce get_celkova_delka(), která vrátí celkovou délku filmu/seriálu (u seriálu je to počet episod násobený délkou jedné episody).
#Třídě Uzivatel přidej funkci pripocti_zhlednuti(), která bude mít jeden parametr. Funkce zvýší atribut udávající celkovou délku sledávní o zadaný parametr.
#Vytvoř objekt, který reprezentuje nějakého uživatele. Následně zkus uvažovat situaci,
# že uživatel zhlédne film a seriál, které jsi vytvořil(a) jako objekty. Uživateli připočti délky děl k délce sledování,
# využij k tomu funkci get_celkova_delka() u objektu a seriálu, abys zjistil(a), kolik minut (nebo hodin) videa celkem uživatel zhlédl.
#Nejjednodušší řešení je, pokud si u filmu/seriálu uložíš celkovou délku do pomocné proměnné a tuto
# pomocnou proměnnou potom předáš jako parametr funkci pripocti_zhlednuti().

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
    def get_celkova_delka(self):
        return delka

class Serial(Polozka):
    def __init__(self, name, zanr, epizody, delkaepizody):
        super().__init__(name, zanr)
        self.epizody = epizody
        self.delkaepizody = delkaepizody
    def get_info(self):
        return f"Nazev polozky je {self.name}, zanr {self.zanr}, pocet epizod {self.epizody}, delka epizody {self.delkaepizody} minut."
    def get_celkova_delka(self):
        delka = self.delkaepizody * self.epizody
        return delka

class Uzivatel:
    def __init__(self, uzivatelske_jmeno, delka_sledovani = 0):
        self.uzivatelske_jmeno = uzivatelske_jmeno
        self.delka_sledovani = delka_sledovani
    def pripocti_zhlednuti(self):
        self.delka_sledovani += delka
        return f"Celkem sledovano {self.delka_sledovani} minut."

ratatouille = Film("Ratatouille", "komedie", 120)
pratele = Serial("Pratele", "komedie", 236, 20)
hubert = Uzivatel("Hubert")

print(ratatouille.get_celkova_delka())
print(pratele.get_celkova_delka())
print(hubert.pripocti_zhlednuti())
