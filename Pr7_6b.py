try:
    x = int(input("Unesi broj: "))
    rezultat = 10 / x
    print("Rezultat je:", rezultat)
except ZeroDivisionError:
    print("Ne možeš dijeliti s nulom.")
finally:
    print("Ovaj blok se uvijek izvršava.")