import numpy as np

def read_matrices(filename):
    matrice = []
    current = []

    try:
        f = open(filename, "r")
    except FileNotFoundError:
        print("Greška: datoteka 'matrice.txt' ne postoji.")
        return []

    for line in f:
        line = line.strip()

        if line == "":
            if current != []:
                matrice.append(np.array(current))
                current = []
        else:
            try:
                row = []
                for x in line.split():
                    row.append(float(x))
                current.append(row)
            except ValueError:
                print("Greška: neispravan unos u matrici – preskačem matricu.")
                current = []
                # preskače trenutnu matricu do praznog retka
                continue

    if current != []:
        matrice.append(np.array(current))

    f.close()
    return matrice


def simetricna(matrix):
    return np.array_equal(matrix, matrix.T)


def antisimetricna(matrix):
    return np.array_equal(matrix, -matrix.T)


# glavni dio
matrice = read_matrices("matrice.txt")
sim_matr = []

for mat in matrice:
    # provjera kvadratne matrice
    try:
        if mat.shape[0] != mat.shape[1]:
            print("Greška: matrica nije kvadratna – preskačem.")
            continue
    except Exception:
        print("Greška pri obradi matrice – preskačem.")
        continue

    if simetricna(mat):
        sim_matr.append(mat)


# zapis simetričnih matrica u datoteku
f = open("simetricne.txt", "w")
for mat in sim_matr:
    for row in mat:
        f.write(" ".join(str(int(x)) if float(x).is_integer() else str(x) for x in row) + "\n")
    f.write("\n")
f.close()