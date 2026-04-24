try:
    rezultat = 1 / 0
except ZeroDivisionError:
    print("Ne možete dijeliti s nulom.")
    rezultat = None  # ili neki default vrijednost
    
print("Rezultat:", rezultat)
