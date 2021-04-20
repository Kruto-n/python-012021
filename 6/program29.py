import wget
import pandas as pd

#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")
temperature = pd.read_csv("temperature.csv")
nov13 = temperature.loc[(temperature["Day"] == 13)]
nov13 = nov13[nov13["AvgTemperature"] != -99]
print(nov13.groupby("Region").count())
print(nov13.groupby("Region")["AvgTemperature"].mean())
print(nov13.groupby("Region")["AvgTemperature"].min())
print(nov13.groupby("Region")["AvgTemperature"].max())