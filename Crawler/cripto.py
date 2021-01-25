from cautare_in_pagina import *
import threading
from queue import Queue
from descarcare_pagina import *

TIP = "Criptomoneda"
def cautare_cripto(lista_prod):
    vgm_url = 'https://finance.yahoo.com/cryptocurrencies'
    soup3 = str(descarcare_pag(vgm_url))
    cauta_produs(soup3, lista_prod, TIP)
    x = 1
    while x < 10:
        vgm_url = 'https://finance.yahoo.com/cryptocurrencies?offset=25&count=' + str(x*25)
        x = x + 1
        soup3 = str(descarcare_pag(vgm_url))
        cauta_produs(soup3, lista_prod, TIP)
    for produs in lista_prod:
        if produs.tendinta == 1:
            produs.afisare_produs()

