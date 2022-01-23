import datetime
from datetime import date

import pandas as pd
import requests
from bs4 import BeautifulSoup

OLX = input("Podaj link do listy wyszukania na OLX: ")


def ilosc_stron(start_sup):
    tagi = start_sup.find_all(name="a", class_="block br3 brc8 large tdnone lheight24")
    for tag in tagi:
        strona = int(tag.getText())
        STRONY.append(strona)
    return STRONY[-1]


def powtorki(x):
    return list(dict.fromkeys(x))


CENY = []
TYTUL = []
DATY = []
LINKI = []
OBRAZY = []
ROZMIARY = []
SIZE = []
STRONY = []


def scraby_wyszukania(sup):
    scrab_cen(sup)
    scrab_tytulow(sup)
    scrab_daty(sup)
    scrab_linkow(sup)
    scrab_obrazow(sup)


def data_farming(OLX):
    response = requests.get(OLX)
    pierwsza_strona = response.text

    start_sup = BeautifulSoup(pierwsza_strona, "html.parser")
    strony = ilosc_stron(start_sup)
    i = 0
    while i <= strony:
        response = requests.get(OLX + "?page=" + str(i))
        strona = response.text

        sup = BeautifulSoup(strona, "html.parser")
        scraby_wyszukania(sup)
        i += 1
    zipp = list(zip(TYTUL, CENY, DATY, LINKI, OBRAZY, SIZE))
    df = pd.DataFrame(zipp, columns=[
        "Tytuł", "Cena", "Data", "Link", "Obraz", "Size"
    ])


    df = df.sort_values(by="Data", ignore_index=True)

    return df


def scrab_cen(sup):
    tagi = sup.find_all(name="p", class_="price")

    for tag in tagi:
        cena = tag.getText().strip().replace(",", ".")
        cena = cena.replace("zł", "")
        cena = cena.replace(" ", "")
        try:
            CENY.append(float(cena))
        except ValueError:
            CENY.append(0)


def scrab_tytulow(sup):
    tagi = sup.find_all("h3", class_="lheight22 margintop5")

    for tag in tagi:
        tytuł = tag.getText().strip()
        SIZE.append(int(len(tytuł)))
        TYTUL.append(tytuł)


def scrab_daty(sup):
    tagi = sup.find_all(name="i", attrs={'data-icon': 'clock'})

    def validate(date_text):
        try:
            datetime.datetime.strptime(date_text, '%Y-%m-%d')
        except ValueError:
            return False
        return True

    for tag in tagi:
        data = tag.parent.getText()
        if "dzisiaj" in data:
            data = date.today().isoformat()
        elif "wczoraj" in data:
            data = datetime.date.today() - datetime.timedelta(days=1)
            data = data.isoformat()
        elif not validate(data):
            data = data.split()
            today = date.today()
            data = date(today.year, today.month, int(data[0]))
            # TODO: Ustawić miesiąc z danych nie na pałe.
            data = data.isoformat()
        DATY.append(data)


def scrab_linkow(sup):
    tagi = sup.find_all("h3", class_="lheight22 margintop5")
    for tag in tagi:
        tag = tag.find("a")
        link = tag.get("href")
        LINKI.append(link)


def scrab_obrazow(sup):
    tagi = sup.find_all(name="img", class_="fleft")
    for tag in tagi:
        obraz = tag.get("src")
        OBRAZY.append(obraz)
