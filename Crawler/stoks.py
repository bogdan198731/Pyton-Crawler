from cautare_in_pagina import *
import threading
from queue import Queue
from descarcare_pagina import *

TIP = "Actiune"


def cautare_actiuni(lista_prod):
#    vgm_url = 'https://finance.yahoo.com/most-active'
#    soup3 = str(descarcare_pag(vgm_url))
#    cauta_produs(soup3, lista_prod, TIP)
#    vgm_url = 'https://finance.yahoo.com/most-active?offset=0&count=100'
#    soup3 = str(descarcare_pag(vgm_url))
#    cauta_produs(soup3, lista_prod, TIP)
    vgm_url = 'https://finance.yahoo.com/quote/BNGO?p=BNGO&.tsrc=fin-srch'
    soup3 = str(descarcare_pag(vgm_url))
    cauta_produs(soup3, lista_prod, TIP)
    x = 0
    while x < 10:
        vgm_url = 'https://finance.yahoo.com/most-active?count=' + str(1 * 250) + '&offset=' + str(x * 250)
        x = x + 1
        soup3 = str(descarcare_pag(vgm_url))
        cauta_produs(soup3, lista_prod, TIP)
#    for produs in lista_prod:
#        if produs.tendinta == 1:
#            produs.afisare_produs()
