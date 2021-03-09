number = input("Na jake cislo chcete zpravu odeslat?")
number = number.replace(" ", " ")
def validate(number):
    if len(number) == 9:
        print("V poradku.")
    elif len(number) == 13:
        if number.startswith("+420"):
            print("V poradku.")
    else:
        print("Cislo neni v poradku.")
validate(number)
message = input("Jaky je text zpravy?")
def price(message):
    lengthofmessage = len(message)
    coefficient = lengthofmessage // 180
    priceofmessage = coefficient * 3
    if priceofmessage == 0:
        print(f"Cena vasi zpravy je 3 Kc.")
    else:
        print(f"Cena vasi zpravy je {priceofmessage} Kc.")
price(message)