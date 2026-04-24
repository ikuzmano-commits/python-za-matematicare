try:
    x = int(input("Unesite cijeli broj: "))
except ValueError:
    print("Nije unesena dobra vrijednost.")
else:
    print("Broj je:", x)