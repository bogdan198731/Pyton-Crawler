from produs import *



def cautare_produs(listaProduse, prod, pret):
    for produs in listaProduse:
#        print(f' produs 1 {prod.nume} == produs 2 {produs.nume}')
        if prod.nume == produs.nume:
            produs.modif_pret(pret)
            return produs
    return False

def are_potential(produs):
    try:
        zero_virgula5_la_suta = float(produs.pret_initial)/200
        if float(produs.pret[0]) - float(produs.pret_initial) > zero_virgula5_la_suta:
             return True
    except ValueError:
#        print(" Eroare de calcul -- zero_virgula5_la_suta")
        return False
    return False


def interesant(produs):
    try:
        cinci_la_suta = float(produs.pret_initial)/20
        if float(produs.pret_initial) - float(produs.pret[0]) > cinci_la_suta:
            return True
        return False
    except ValueError:
#        print(" Eroare de calcul -- cinci_la_suta")
        return False
    return False



