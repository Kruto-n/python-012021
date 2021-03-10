vysledky = [
    {"Jméno": "Mirek Dušín", "Český jazyk": 1, "Anglický jazyk": 2, "Matematika": 1, "Biologie": 1, "Zeměpis": 1},
    {"Jméno": "Jarka Metelka", "Český jazyk": 3, "Anglický jazyk": 1, "Matematika": 3, "Dějepis": 2, "Ekonomika": 5},
    {"Jméno": "Jindra Hojer", "Český jazyk": 2, "Anglický jazyk": 2, "Matematika": 1, "Biologie": 3, "Chemie": 3},
    {"Jméno": "Červenáček", "Český jazyk": 1, "Anglický jazyk": 1, "Matematika": 1, "Fyzika": 2, "Informatika": 4},
    {"Jméno": "Rychlonožka", "Český jazyk": 4, "Anglický jazyk": 3, "Matematika": 2, "Chemie": 1, "Biologie": 4},
]
def spocitej_prumer(student):
    suma = 0
    for znamka in student.values():
        if type(znamka) == int:
            suma += znamka
    prumer = suma / (len(student) - 1)
    return prumer

def ohodnot_studenta(student):
    prumer = spocitej_prumer(student)
    if prumer < 1.5 and not 3 in student.values() and not 5 in student.values():
        print(student["Jméno"], " vyznamenání")
    elif not 5 in student.values():
        print(student["Jméno"], " prospěl")
    else:
        print(student["Jméno"], " neprospěl")

for student in vysledky:
    ohodnot_studenta(student)

