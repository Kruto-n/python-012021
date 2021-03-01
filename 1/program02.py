sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}
kod = 0
pocet = 0
kod = input("Jaky je kod soucastky?")
if kod in sklad:
  pocet = int(input("Kolik jich potrebujete?"))
  if pocet > sklad[kod]:
    print(f"Mame pouze {sklad[kod]}.")
    sklad.pop(kod)
  else:
    print(f"Poptavku lze uspokojit v plne vysi.")
    for kod in sklad:
      sklad[kod] = sklad[kod] - pocet
else:
  print("Soucastku nemame na skladu.")