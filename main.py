import requests
from bs4 import BeautifulSoup
import pandas as pd
from scrab import *

olx = "https://www.olx.pl/sport-hobby/q-rolki/"  # input("Podaj link do wyników wyszukiwania na OLX: ")
i = 1


def parse(i, olx):
    response = requests.get(olx + f"?page={i}")
    strona = response.text
    # print(response)
    # print(strona)

    sup = BeautifulSoup(strona, "html.parser")

    # ilość_stron(sup)

    while i <= 3:  # ilość_stron(sup)
        scrab_obrazów(sup)
        scrab_linków(sup)
        scrab_tytułów(sup)
        scrab_cen(sup)
        scrab_daty(sup)

        df = pd.DataFrame({
            "Tytuł": TYTUŁY,
            "Ceny": Ceny,

        })
        print()
        i += 1


parse(i, olx)
