imedat = input("Unesite naziv datoteke: ")

dat = None  # inicijalizacija varijable kako bi bila dostupna u finally bloku

try:
    dat = open(imedat, "r")
    numbers = []

    for line in dat:
        numbers.append(float(line.strip()))

    average = sum(numbers) / len(numbers)
    print("Prosjek je:", average)

except FileNotFoundError:
    print("Greška: Datoteka ne postoji.")

except ValueError:
    print("Greška: Datoteka sadrži neispravne podatke (nisu brojevi).")

except ZeroDivisionError:
    print("Greška: Datoteka je prazna.")

finally:
    if dat:
        dat.close()
        print("Datoteka je zatvorena.")