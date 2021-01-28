import re
from cautare_in_pagina import *
import threading
from queue import Queue
from descarcare_pagina import *
import threading
import time
from general import *
from acces_mail import *
from produs import *
from basicMaterials import *
from health import *
from cripto import *
from stoks import *
from techno import *
from financial import *
from energy import cautare_Energie



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


INTERVAL = 300
ITERATII = 10
go = 1
i = int(1)
lista_prod = []

if os.path.isfile('test.xlsx'):
    readFromExcel('test.xlsx', lista_prod)
#else:
#    create_data_files('Crawler/BD.txt', 0)


create_project_dir('Crawler')
create_data_files('Crawler/cumpar.txt', 0)
create_data_files('Crawler/de-vazut.txt', 0)

k = 0
while go != 0:
    k += 1
    print(f'Iteratia : {k} ')
#    cautare_cripto(lista_prod)
    x = threading.Thread(target=cautare_cripto, args=(lista_prod,))
    x.start()
    y = threading.Thread(target=cautare_actiuni, args=(lista_prod,))
#    y.start()
#    cautare_actiuni(lista_prod)
    bm = threading.Thread(target=cautare_BasicMaterials, args=(lista_prod,))
    bm.start()
    he = threading.Thread(target=cautare_health, args=(lista_prod,))
    he.start()
    te = threading.Thread(target=cautare_techno, args=(lista_prod,))
    te.start()
    fi = threading.Thread(target=cautare_financiar, args=(lista_prod,))
    fi.start()
    en = threading.Thread(target=cautare_Energie, args=(lista_prod,))
    en.start()

    x.join()
#    y.join()
    bm.join()
    he.join()
    te.join()
    fi.join()
    en.join()

    if i >= ITERATII:
        break
    if go == 0:
        break
    else:
        time.sleep(INTERVAL)
    i += 1



#print("afisare lista")
#afis_lista(lista_prod)
produs_to_excel(lista_prod, "test.xlsx")