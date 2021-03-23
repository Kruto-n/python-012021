#Vytvoř třídu Uchazec, která bude dědit od třídy Kontakt a která reprezentuje uchazeče o práci.
# Uchazeč o práci bude mít navíc atribut datum_pohovoru a zapis_z_pohovoru.
# Datum pohovoru objekt získá z parametru a zápis z pohovoru je na začátku prázdný řetězec "".
# Dále přidej funkci uloz_zapis(), která bude mít jako parametr textový zápis pohovoru.
# Tato funkce ohlídá, zda uživatel omylem nezadává zápis k pohovoru, který ještě neproběhl.
# Na začátku funkce porovnej aktuální datum a datum pohovoru. Pokud podle data pohovor ještě neproběhl, vrať chybový text,
# který informuje uživatele o chybě. Pokud již podle data pohovor proběhl, ulož zápis a vrať text s informací, že zápis byl uložen.

from datetime import datetime, timedelta

class Kontakt:
  def __init__(self, jmeno, email):
    self.jmeno = jmeno
    self.email = email

class Uchazec(Kontakt):
    def __init__(self, jmeno, email, datum_pohovoru):
        super().__init__(jmeno, email)
        self.datum_pohovoru = datetime.strptime(datum_pohovoru, "%d. %m. %Y")
    def uloz_zapis(self, zapis_z_pohovoru):
        zapis_z_pohovoru = 0
        if datetime.now() < self.datum_pohovoru:
            return f"Pohovor jeste neprobehl."
        else:
            self.zapis_z_pohovoru = zapis_z_pohovoru
            return f"Zapis je v poradku."
    def get_info(self):
        return f"Zapis je: {self.zapis_z_pohovoru}."

nedele = Uchazec("Alena Alenova", "alenalena@alena.cz", "20. 3. 2021")
streda = Uchazec("Klara Klarova", "klarovaklara@klara.com", "24. 3. 2021")

#print(nedele.uloz_zapis("uchazec vhodny"))
#print(nedele.get_info())
#print(nedele.get_info())
#print(streda.get_info())