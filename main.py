import pandas as pd

from scraby_wyszukania import *
from visual import *

start = datetime.datetime.now()

data_framing(OLX)

df_sklad = [TYTUL, CENY, DATY, LINKI, SIZE]
for lista in df_sklad:
    lista = powtorki(lista)

try:
    df = pd.DataFrame({
        "Tytuł": TYTUL,
        "Cena": CENY,
        "Data": DATY,
        "Link": LINKI,
        "Obraz": OBRAZY,
        "Size": SIZE,
    })
except ValueError:
    zipp = list(zip(TYTUL, CENY, DATY, LINKI, OBRAZY, SIZE))
    df = pd.DataFrame(zipp, columns={
        "Tytuł", "Cena", "Data", "Link", "Obraz", "Size"
    })
df = df.drop_duplicates()
df = df.sort_values(by="Data", ignore_index=True)

wizualizacja(df)
print(datetime.datetime.now() - start)
