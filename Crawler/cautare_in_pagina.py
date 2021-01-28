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
        full_name = sursa[poz+7: sursa.find('"', poz+7)]
        poz1 = sursa.find('>', poz)
        poz2 = sursa.find('<', poz)
        nume = sursa[poz1+1: poz2]
        poz = sursa.find('span class=', poz2)
        poz1 = sursa.find('>', poz)
        poz2 = sursa.find('<', poz)
        prett = str(sursa[poz1+1: poz2].replace(',', ''))
        try:
            pret = float(prett)
        except ValueError:
            pret = 0
#           prod.afisare_produs()
        if len(nume) > 0 and pret > 0:
            prod = Produs(full_name, nume, pret, False, tip)
            produs=cautare_produs(listaProd, prod, pret)
            if not produs:
                listaProd.append(prod)
                i += 1
            else:
                if are_potential(produs):
                    data = str("poti incerca sa investesti in " + str(produs.nume) + " pret initial " + str(produs.pret_initial) + "pret acctual " + str(produs.pret[0]))
                    append_to_file('Crawler/cumpar.txt', data)
    #                    print("PRODUS ADAUGAT IN DE CUMPARAT")
                if interesant(produs):
                    data = str("poti incerca sa investesti in " + str(produs.nume) + " pret initial " + str(produs.pret_initial) + "pret acctual " + str(produs.pret[0]))
                    append_to_file('Crawler/de-vazut.txt', data)
    #                    print("PRODUS ADAUGAT IN DE-VAZUT")
    #                prod.afisare_produs()
     #   except:
      #      continue
    if i > 0:
        print("au fost gasite " + str(i) + ' noi produse de tipul ' + tip)

#    print('au fost gasite ' + str(i) + ' companii')


def afis_lista(listaProd):
    for prod in listaProd:
        prod.afisare_produs()

