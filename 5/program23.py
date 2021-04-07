import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/country_vaccinations.csv")
import pandas

countries = pandas.read_csv("country_vaccinations.csv")
print(countries.columns)
naockovano = countries.loc[(countries["date"] == "2021-03-10"), ["country", "total_vaccinations"]]
print(naockovano)
milion = countries.loc[(countries["date"] == "2021-03-10") & (countries["total_vaccinations"] > 1000000), ["country", "total_vaccinations"]]
print(milion)
hodne = countries.loc[(countries["date"] == "2021-03-10") & (countries["daily_vaccinations"] > 100000), ["country", "daily_vaccinations"]]
malo = countries.loc[(countries["date"] == "2021-03-10") & (countries["daily_vaccinations"] < 100), ["country", "daily_vaccinations"]]
print(hodne)
print(malo)