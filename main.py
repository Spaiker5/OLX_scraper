import pandas as pd
import requests
from bs4 import BeautifulSoup

from scraby_wyszukania import *
from visual import *

olx = input("Podaj link do wyników wyszukiwania na OLX: ")


def data_framing(olx):
    start = datetime.datetime.now()
    response = requests.get(olx)
    strona = response.text

    start_sup = BeautifulSoup(strona, "html.parser")

    strony = ilosc_stron(start_sup)
    print(strony)
    i = 0
    while i <= strony:
        response = requests.get(olx + "?page=" + str(i))
        strona = response.text

        sup = BeautifulSoup(strona, "html.parser")
        scraby_wyszukania(sup)
        i += 1
        print(i)
    try:
        df = pd.DataFrame({
            "Tytuł": TYTUŁY,
            "Cena": CENY,
            "Data": DATY,
            "Linki": LINKI,
            "Size": SIZE,
        })
    except ValueError:
        print("Ojojoj")
        scraby_wyszukania(sup)
        df = pd.DataFrame({
            "Tytuł": TYTUŁY,
            "Cena": CENY,
            "Data": DATY,
            "Linki": LINKI,
            "Size": SIZE,
        })
    df = df.drop_duplicates()
    df = df.sort_values(by="Data", ignore_index=True)

    print(datetime.datetime.now() - start)

    return df


wizualizacja(data_framing(olx))
