import math

dat = "vrijednosti.txt"

try:
    f = open(dat, "r")
except FileNotFoundError:
    raise FileNotFoundError("Datoteka 'vrijednosti.txt' ne postoji.")

for linija in f:
    linija = linija.strip()

    try:
        # provjera praznog retka
        if linija == "":
            raise ValueError("Prazan redak u datoteci.")

        # pokušaj pretvorbe u broj
        x = float(linija)

        # provjera negativnog broja
        if x < 0:
            raise ValueError(f"Negativan broj nije dopušten: {x}")

        rezultat = math.sqrt(x)
        print(f"f(x) = sqrt({x}) = {rezultat}")

    except ValueError as e:
        print(f"Greška: {e}")

f.close()