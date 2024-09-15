import requests
from bs4 import BeautifulSoup

volume = 0
valore_iniziale = 0
valore_finale = 0

diz2 = {}

links = ["https://it.wikipedia.org/wiki/Capitoli_di_One_Piece_(volumi_1_-_60)",
         "https://it.wikipedia.org/wiki/Capitoli_di_One_Piece_(volumi_61_-_in_corso)"]


def recupera_da_link(link):
    global volume
    global valore_iniziale
    global valore_finale
    text = requests.get(link).text
    soup = BeautifulSoup(text, "html.parser")
    a = soup.find_all(class_='wikitable')
    diz = {}
    for tabella in a:
        z = tabella.tbody
        z = z.find_all("div")
        for element in z:
            b = element.find_all('li')
            numero_capitoli = 0
            for ele in b:
                numero_capitoli += 1
            if numero_capitoli > 0:
                volume = volume + 1
                diz[volume] = numero_capitoli
    for key, value in diz.items():
        valore_finale = valore_iniziale + value
        diz2[key] = [valore_iniziale + 1, valore_finale]
        valore_iniziale = valore_finale


def ottieni_volumi() -> dict:
    for link in links:
        recupera_da_link(link)
    return diz2
