"""Calcolo della velocità in km/h e m/s"""
# Dati iniziali
minuti = 21
secondi = 34
km = 4.1
# Elaborazione
secondi_totali = minuti * 60 + secondi

# Velocità in m/s
metri = km * 1000
m_s = metri / secondi_totali
# Velocità in km/h
ore_totali = secondi_totali / 3600
km_h = km / ore_totali
# Output
print("Velocità:", round(m_s, 2), "m/s")
print("Velocità:", round(km_h, 2), "km/h")