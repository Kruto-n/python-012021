import wget
import pandas

#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_praha.csv")
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_plzeň.csv")
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/zam_liberec.csv")
#wget.download("https://raw.githubusercontent.com/pesikj/python-012021/master/zadani/6/platy_2021_02.csv")

liberec = pandas.read_csv("zam_liberec.csv")
plzen = pandas.read_csv("zam_plzeň.csv")
praha = pandas.read_csv("zam_praha.csv")
platy = pandas.read_csv("platy_2021_02.csv")
print(plzen.head)

liberec['mesto'] = 'Liberec'
plzen['mesto'] = 'Plzen'
praha['mesto'] = 'Praha'

