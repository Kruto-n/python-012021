import wget
import pandas
import matplotlib.pyplot as plt

#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")

temperature = pandas.read_csv('temperature.csv')
cities = temperature[temperature["City"].isin(["Miami Beach", "Helsinki", "Tokyo"])]
cities.plot(kind='box', by="City")
plt.show()