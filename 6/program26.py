import wget
import pandas as pd

#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_praha.csv")
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_plzeň.csv")
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_liberec.csv")
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/platy_2021_02.csv")

liberec = pd.read_csv("zam_liberec.csv")
plzen = pd.read_csv("zam_plzeň.csv")
praha = pd.read_csv("zam_praha.csv")
platy = pd.read_csv("platy_2021_02.csv")
print(plzen.head())

liberec['mesto'] = 'Liberec'
plzen['mesto'] = 'Plzen'
praha['mesto'] = 'Praha'

zamestnanci = pd.concat([liberec, plzen, praha], ignore_index=True)
zamestnanci.to_csv('zamestnanci.csv', index=False)

zamestnanci_platy = pd.DataFrame.merge(zamestnanci, platy, on="cislo_zamestnance", how="outer")

print(zamestnanci.shape) #(56, 5)
print(platy.shape) #(43, 2)
print(zamestnanci_platy.shape) #(56, 6)

print(zamestnanci_platy.groupby('mesto')['plat'].mean())

