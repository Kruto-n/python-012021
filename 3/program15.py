from datetime import datetime, timedelta
neprevedenedatum = input("Na jaky den chcete vstupenky zakoupit?")
datum = datetime.strptime(neprevedenedatum, "%d. %m. %Y")
pocet = int(input("Kolik vstupenek chcete?"))

t1_zacatek = datetime(2021, 7, 1)
t1_konec = datetime(2021, 8, 10)
t2_zacatek = datetime(2021, 8, 11)
t2_konec = datetime(2021, 8, 31)

if t1_zacatek <= datum <= t1_konec:
    cena = 250 * pocet
    print(f"Cena vstupenek je {cena} Kc.")
elif t2_zacatek <= datum <= t2_konec:
    cena = 180 * pocet
    print(f"Cena vstupenek je {cena} Kc.")
else:
    print("Letni kino je bohuzel uzavrene.")
