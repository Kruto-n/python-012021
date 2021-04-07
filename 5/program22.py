import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/character-deaths.csv")
import pandas

deaths = pandas.read_csv("character-deaths.csv")
deaths = deaths.set_index("Name")
print(deaths.columns)
print(deaths.loc["Hali"])
print(deaths.loc["Gevin Harlaw" : "Gillam"])
print(deaths.loc["Gevin Harlaw" : "Gillam" , 'Death Year'])
print(deaths.loc["Gevin Harlaw" : "Gillam" , 'GoT' : 'DwD'])