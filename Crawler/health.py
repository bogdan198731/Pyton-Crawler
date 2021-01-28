from cautare_in_pagina import *
from descarcare_pagina import *

TIP = "health"


def cautare_health(lista_prod):
    x = 0
    while x < 5:
        vgm_url = 'https://finance.yahoo.com/screener/predefined/ms_healthcare?offset='+str(1 * 250) + 'offset=' + str(x * 250)
        x = x + 1
        soup3 = str(descarcare_pag(vgm_url))
        cauta_produs(soup3, lista_prod, TIP)

#    for produs in lista_prod:
#        if produs.tendinta == 1:
#            produs.afisare_produs()