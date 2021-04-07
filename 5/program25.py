import wget
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/temperature.csv")
import pandas

temperature = pandas.read_csv('temperature.csv')
print(temperature.head())
den = temperature.loc[(temperature["Day"] == 13)]
print(den)
den_US = temperature.loc[(temperature["Day"] == 13) & (temperature["Country"] == "US")]
print(den_US)