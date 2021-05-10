from produs import *


def cautareOportunitate(lista_produse):
    for prod in lista_produse:
        try:
            if (prod.pret_initial < prod.pret[0] * 0.95) or (prod.pret[0] < prod.pret[1] * 0.97):
                print("+ " + prod.full_name + " pret initial " + str(prod.pret_initial) +" -> " + str(prod.pret[0]) +
                      " -> " + str(prod.pret[1]))
            if (prod.pret_initial > prod.pret[0] * 1.05) or (prod.pret[0] > prod.pret[1] * 1.03):
                print("- " + prod.full_name + " pret initial " + str(prod.pret_initial) +" -> " + str(prod.pret[0]) +
                      " -> " + str(prod.pret[1]))
        except:
            if (prod.pret_initial < prod.pret[0] * 0.95):
                print("+ " + prod.full_name + " pret initial " + str(prod.pret_initial) +" -> " + str(prod.pret[0]))
            if (prod.pret_initial > prod.pret[0] * 1.05):
                print("- " + prod.full_name + " pret initial " + str(prod.pret_initial) +" -> " + str(prod.pret[0]))