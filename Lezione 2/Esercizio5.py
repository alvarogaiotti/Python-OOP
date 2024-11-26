numero = int(input("Fino a quale numero vuoi controllare i divisori?"))

for x in range(1, numero):
  if x % 3 == 0 and x % 5 == 0:
    print(x)