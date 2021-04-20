import wget
import pandas as pd

#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/vykazy.csv")

vykazy = pd.read_csv("vykazy.csv")

hours = vykazy.groupby('project').sum('hours')
hours.to_excel("hours.xlsx")
reverse = pd.read_excel("hours.xlsx")
print(reverse)
