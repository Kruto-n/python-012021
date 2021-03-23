from forex_python.converter import CurrencyRates
prevodnik = CurrencyRates()
pozadovano_v_cilove_mene = int(input("Pozadovano v cilove mene:"))
puvodni_mena = input("Zadejte puvodni menu:")
cilova_mena = input("Zadejte cilovou menu:")
cena = prevodnik.convert(puvodni_mena, cilova_mena, pozadovano_v_cilove_mene)
print(cena)
