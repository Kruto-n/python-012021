prodeje2019 = {
   "Zkus mě chytit": 4165,
   "Vrah zavolá v deset": 5681,
   "Zločinný steh": 2565,
}

prodeje2020 = {
   "Zkus mě chytit": 3157,
   "Vrah zavolá v deset": 3541,
   "Vražda podle knihy": 2510,
   "Past": 2364,
   "Zločinný steh": 5412,
   "Zkus mě chytit": 6671,
}
nazev = input("Jaky je nazev knihy?")
sales1 = 0
sales2 = 0
total = 0
if nazev in prodeje2019:
    sales1 = prodeje2019[nazev]
if nazev in prodeje2020:
    sales2 = prodeje2020[nazev]
total = sales2 + sales1
print(total)