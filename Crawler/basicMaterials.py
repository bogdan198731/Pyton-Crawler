from cautare_in_pagina import *
from descarcare_pagina import *

TIP = "BasicMaterials"


def cautare_BasicMaterials(lista_prod):
    vgm_url = 'https://finance.yahoo.com/screener/predefined/ms_basic_materials?offset=0&count=250'
    soup3 = str(descarcare_pag(vgm_url))
    cauta_produs(soup3, lista_prod, TIP)

#    for produs in lista_prod:
#        if produs.tendinta == 1:
#            produs.afisare_produs()
