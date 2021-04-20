import wget
import pandas as pd

wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/staty.json")
wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/gdp.csv")

staty = pd.read_json("staty.json")

evropa = staty.loc[(staty["region"] == "Europe")]
print(evropa.groupby("subregion").count())
print(evropa.groupby("subregion").sum())