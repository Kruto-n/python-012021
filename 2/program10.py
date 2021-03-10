def uspech(odvetvi, obrat, zeme, konference = False, newsletter = False):
    body = 0
    if odvetvi == "Automotive":
        body += 3
    elif odvetvi == "Retail":
        body += 2
    else:
        body += 0
    if obrat == "10 mil. euro - 1000 mil. euro":
        body += 3
    elif obrat == "< 10 mil. euro":
        body += 0
    else:
        body += 0
    if zeme == "Ceska republika" or zeme == "Slovensko":
        body += 2
    elif zeme == "Francie" or zeme == "Nemecko":
        body += 1
    else:
        body += 0
    if konference == "ano":
        body += 1
    if newsletter == "ano":
        body += 1
    if body <= 5:
        print("Sance na zakazku je mala.")
    elif 6 <= body >= 8:
        print("Sance na zakazku je stredni.")
    else:
        print("Sance na zakazku je vysoka.")
odvetvi = input("Zadejte prosim odvetvi firmy. Moznosti jsou: Automotive, Retail, jine.")
obrat = input("Zadejte prosim obrat firmy. Moznosti jsou: < 10 mil. euro, 10 mil. euro - 1000 mil. euro, jine.")
zeme = input("Zadejte prosim zemi firmy.")
konference = input("Byli jste na konferenci? ano/ne.")
newsletter = input("Odebirate newsletter? ano/ne")
uspech(odvetvi, obrat, zeme, konference, newsletter)