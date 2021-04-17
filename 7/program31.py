import wget
import pandas

#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")
temperature = pandas.read_csv("temperature.csv")

temperature13 = temperature[temperature["Day"] == 13]

temperature13 = temperature13.loc[temperature13["AvgTemperature"] != -99]

temperature13 = temperature13.sort_values(["AvgTemperature"], ascending = False)

print(temperature13.sort_values(by="AvgTemperature").tail())
print(temperature13.sort_values(by="AvgTemperature").head())