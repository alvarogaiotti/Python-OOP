primo_numero = int(input("Inserisci il primo numero:"))
secondo_numero = int(input("Inserisci il secondo numero:"))
terzo_numero = int(input("Inserisci il terzo numero:"))

if primo_numero > secondo_numero:
  if primo_numero > terzo_numero:
    print(primo_numero)
  else:
    print(terzo_numero)
elif secondo_numero > terzo_numero:
  print(secondo_numero)
else:
  print(terzo_numero)

# print(max(primo_numero, secondo_numero, terzo_numero))