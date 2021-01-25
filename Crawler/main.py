import re
from cautare_in_pagina import *
import threading
from queue import Queue
from descarcare_pagina import *
import time
from general import *
from acces_mail import *
from cripto import *
from stoks import *



#PROJECT_NAME = 'thenewboston3'
#HOMEPAGE = 'https://www.etoro.com/ro/discover/markets/stocks'
#NUME_FISIER = '/date.txt'
#DOMAIN = get_domain_name(HOMEPAGE)
#QUEUE_FILE = PROJECT_NAME + NUME_FISIER
#NUMBER_OF_THREADS = 8
#queue = Queue()
#Spider(PROJECT_NAME, HOMEPAGE, DOMAIN)

#vgm_url = 'https://www.etoro.com/ro/markets/aapl'
#vgm_url = 'https://cdn.etorostatic.com/285.0.2/sem-etoro-ng/runtime.7d9d4678f9511567f211.js'
#vgm_url = 'https://www.google.com/finance/#wptab=s:H4sIAAAAAAAAAOPQeMSozC3w8sc9YSmpSWtOXmMU4RJyy8xLzEtO9UnMS8nMSw9ITE_l2cXEHekfGhQfHOLv7B28iJU9DaIGAAUYQO1AAAAA'
#vgm_url = 'https://www.tradeville.eu/actiuni/cotatii-bursa'


INTERVAL = 60
ITERATII = 50
go = 1
i = int(1)
lista_prod = []

create_project_dir('Crawler')
create_data_files('Crawler/cumpar.txt', 0)
create_data_files('Crawler/de-vazut.txt', 0)

#if os.path.isfile('Crawler/BD.txt'):
#    lista_prod = file_to_set('Crawler/BD.txt')
#else:
#    create_data_files('Crawler/BD.txt', 0)


k = 0
my_instance = Produs
prod = Produs("a", 0, 0, 0)
prod.modif_pret(10)
lista_prod.append(prod)

#go = 0
while go != 0:
    k += 1
    print(f'Iteratia : {k} ')
    cautare_cripto(lista_prod)
    cautare_actiuni(lista_prod)

#    go = int(input("mai incercam > "))
#    print("go este " + str(go))
    if go == 0:
        break
    else:
        time.sleep(INTERVAL)
    i += 1
    if i > ITERATII:
        break

#for produs in lista_prod:
#    afis_lista(lista_prod)


#set_to_file(lista_prod, 'Crawler/BD.txt')



