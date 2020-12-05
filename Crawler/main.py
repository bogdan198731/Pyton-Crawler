import re
from bs4 import BeautifulSoup
import requests

#vgm_url = 'https://www.etoro.com/ro/markets/aapl'
#vgm_url = 'https://cdn.etorostatic.com/285.0.2/sem-etoro-ng/runtime.7d9d4678f9511567f211.js'
vgm_url = 'https://www.google.com/finance/#wptab=s:H4sIAAAAAAAAAOPQeMSozC3w8sc9YSmpSWtOXmMU4RJyy8xLzEtO9UnMS8nMSw9ITE_l2cXEHekfGhQfHOLv7B28iJU9DaIGAAUYQO1AAAAA'
html_text = requests.get(vgm_url).text
soup = BeautifulSoup(html_text, 'html.parser')
print(soup)
for link in soup.find_all('a'):
    print(link.get('href'))
    print(link.get('script'))

print("test")

for link in soup.find_all('ui-layout'):
    print(link.get('class'))

print('test2')

for link in soup.find_all('script'):
#    print(link.get('href'))
    print(link.get('data-assets-version'))






#import threading
#from queue import Queue
#from spider import Spider
#from domain import *
#from general import *
#from bs4 import BeautifulSoup

#PROJECT_NAME = 'thenewboston3'
#HOMEPAGE = 'https://www.etoro.com/ro/discover/markets/stocks'
#DOMAIN = get_domain_name(HOMEPAGE)
#QUEUE_FILE = PROJECT_NAME + '/queue.txt'
#CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
#NUMBER_OF_THREADS = 8
#queue = Queue()
#Spider(PROJECT_NAME, HOMEPAGE, DOMAIN)
