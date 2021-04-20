import wget
import pandas as pd

#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/vykazy.csv")

vykazy = pd.read_csv("vykazy.csv")
print(vykazy.head())

print(vykazy.groupby('project').sum('hours'))