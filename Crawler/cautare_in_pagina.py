from produs import *
from gestionare_produse import *
from general import  *

def cauta_produs(sursa, listaProd,tip):
    gasit = True
    poz2 = 0
    i=0
    while gasit:
        poz = sursa.find('title=', poz2)
        if poz == -1:
            break
        poz1 = sursa.find('>', poz)
        poz2 = sursa.find('<', poz)
        nume = sursa[poz1+1: poz2]
        poz = sursa.find('span class=', poz2)
        poz1 = sursa.find('>', poz)
        poz2 = sursa.find('<', poz)
        pret = sursa[poz1+1: poz2]
        prod = Produs(nume, pret, False, tip)
        if len(nume) > 0 and len(pret) > 0:
            produs=cautare_produs(listaProd, prod, pret)
            if not produs:
                listaProd.append(prod)
                i += 1
            else:
                if are_potential(produs):
                    data = "poti incerca sa investesti in " + str(produs.nume) + " pret initiai " + str(produs.pret_initial + "pret acctual " + str(produs.pret[0]))
                    append_to_file('Crawler/cumpar.txt', data)
                    print("PRODUS ADAUGAT IN DE CUMPARAT")
                if interesant(produs):
                    data = "poti incerca sa investesti in " + str(produs.nume) + " pret initiai " + str(produs.pret_initial) + "pret acctual " + str(produs.pret[0])
                    append_to_file('Crawler/de-vazut.txt', data)
                    print("PRODUS ADAUGAT IN DE-VAZUT")
#                prod.afisare_produs()
#    print('au fost gasite ' + str(i) + ' companii')


def afis_lista(listaProd):
    for prod in listaProd:
        prod.afisare_produs()

