import wget
import pandas
import matplotlib.pyplot as plt

#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/5/twlo.csv")
twilio = pandas.read_csv("twlo.csv")

twilio["Date"] = pandas.to_datetime(twilio["Date"])
twilio.plot("Date", "Close")
plt.show()