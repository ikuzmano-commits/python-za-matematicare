def izracunaj(datoteka):
    rez = []

    try:
        with open(datoteka, 'r') as dat:
            for i, linija in enumerate(dat, start=1):
                try:
                    x = float(linija.strip())
                    vrijednost = 100 / x
                    rez.append(vrijednost)

                except ValueError:
                    print(f"Redak {i}: neispravan unos ('{linija.strip()}').")

                except ZeroDivisionError:
                    print(f'Redak {i}: dijeljenje s nulom nije dozvoljeno.')

    except FileNotFoundError:
        print(f"Greška: datoteka '{datoteka}' ne postoji.")
        return []

    return rez


# poziv funkcije
rez = izracunaj('vrijednosti.txt')
print('Uspješno izračunati rezultati:', rez)