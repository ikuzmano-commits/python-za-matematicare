def prosjek(predmeti,ime):
    #prvo napravimo listu
    lista = predmeti.split(';')
    #zatim napravimo dictionary
    rj = {}
    for i in range(len(lista)):
        rj[lista[i].split('=')[0]] = float(lista[i].split('=')[1])
    suma = 0
    for key in rj:
        suma = suma + rj[key]
    rjesenje = suma/len(lista)
    print(f"Učenik {ime}  ima prosjek {rjesenje:.2f}.")

prosjek('matematika=3.5;povijest=4.2;tjelesni=5;fizika=4.6','Stipe')