from cautare_in_pagina import *
import threading
from queue import Queue
from descarcare_pagina import *

TIP = "Criptomoneda"
def cautare_cripto(lista_prod):
#    vgm_url = 'https://finance.yahoo.com/cryptocurrencies'
#    soup3 = str(descarcare_pag(vgm_url))
#    cauta_produs(soup3, lista_prod, TIP)
    x = 0
    while x < 5:
        vgm_url = 'https://finance.yahoo.com/cryptocurrencies?offset=' + str(x*250) + '&count=' + str(1*250)
        x = x + 1
        soup3 = str(descarcare_pag(vgm_url))
        cauta_produs(soup3, lista_prod, TIP)
#    for produs in lista_prod:
#        if produs.tendinta == 1:
#            produs.afisare_produs()

