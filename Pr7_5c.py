try:
    f = open('podaci.txt')
except FileNotFoundError:
    print("Datoteka ne postoji.")