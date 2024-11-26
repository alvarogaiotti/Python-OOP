primo_lato = int(input("Inserisci il primo lato:"))
secondo_lato = int(input("Inserisci il secondo lato:"))
terzo_lato = int(input("Inserisci il terzo lato:"))

lato1_ok = primo_lato > 0 and primo_lato < secondo_lato + terzo_lato

lato2_ok = secondo_lato > 0 and secondo_lato < primo_lato + terzo_lato

lato3_ok = terzo_lato > 0 and terzo_lato < primo_lato + secondo_lato

if lato1_ok and lato2_ok and lato3_ok:
  print("Triangolo!")
else:
  print("Non è un triangolo!")