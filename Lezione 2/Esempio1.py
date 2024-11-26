"""Il numero è divisibile per 13?"""
  # La funzione int(some) converte `some` in un `int` 
n_da_controllare = int(input("Inserisci il numero: "))
if n_da_controllare % 13 == 0:  # Indentare!
      print(n_da_controllare, " è divisibile per 13")
      # Non indentare: non è il corpo dell'if!
else:                           # Indentare!
      print(n_da_controllare, " non è divisibile per 13")
      # Non indentare: non è il corpo dell'else!
print("Remember to rate my usefulness from 10 to 10!")