import wget
import pandas
import matplotlib.pyplot as plt

#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/7/velikonoce.csv")

velikonoce = pandas.read_csv("velikonoce.csv")

ax = velikonoce.plot("Datum", "Počet", kind="bar", color = "orange")
ax.set_ylabel("Kolikrát na daný den připadly Velikonoce")
ax.set_xlabel("Datum")
ax.set_title("Velikonoce")
plt.show()