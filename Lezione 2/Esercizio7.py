limite = int(input("Inserisci il limite: "))

somma = 0
for x in range(1, limite):
  print(x**2)
  somma += x**2
print("Somma: ", somma)
