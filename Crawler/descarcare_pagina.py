from bs4 import BeautifulSoup
import requests


def descarcare_pag(url):
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'html.parser')
    return soup