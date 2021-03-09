number = input("Na jake cislo chcete zpravu odeslat?")
number = number.replace(" ", "")
def validate(number):
    if len(number) == 9:
        print("V poradku.")
        return True
    elif len(number) == 13:
        if number.startswith("+420"):
            print("V poradku.")
            return True
    else:
        print("Cislo neni v poradku.")
        return False
vporadku = validate(number)
message = 0
if vporadku:
    def price(message):
        message = input("Jaky je text zpravy?")
        lengthofmessage = len(message)
        coefficient = lengthofmessage // 180 + 1
        priceofmessage = coefficient * 3
        print(f"Cena vasi zpravy je {priceofmessage} Kc.")
price(message)