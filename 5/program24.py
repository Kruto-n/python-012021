import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")
import pandas

temperature = pandas.read_csv('temperature.csv')
print(temperature.head())
praha = temperature.loc[(temperature["City"] == "Prague")]
print(praha)
osmdesat = temperature.loc[(temperature["AvgTemperature"] > 80)]
print(osmdesat)
sedesat_evropa = temperature.loc[(temperature["AvgTemperature"] > 60) & (temperature["Region"] == "Europe")]
print(sedesat_evropa)
malo = temperature.loc[(temperature["AvgTemperature"] < -20)]
print(malo)