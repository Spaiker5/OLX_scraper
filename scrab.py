from config import *


def ilość_stron(sup):
    pages = sup.find_all(name="a", class_="block br3 brc8 large tdnone lheight24")
    for page in pages:
        strona = int(page.getText())
        STRONY.append(strona)

    return STRONY[-1]


def scrab_cen(sup):
    tagi = sup.find_all(name="p", class_="price")

    for tag in tagi:
        cena = tag.getText().split()
        CENY.append(cena)


def scrab_tytułów(sup):
    tagi = sup.find_all(name="a", class_="marginright5 link linkWithHash detailsLink")

    for tag in tagi:
        tytuł = tag.getText().strip()
        TYTUŁY.append(tytuł)


def scrab_daty(sup):
    tagi = sup.find_all(name="i", attrs={'data-icon': 'clock'})

    for tag in tagi:
        data = tag.parent.getText()
        DATY.append(data)


def scrab_linków(sup):
    tagi = sup.find_all(name="a", class_="marginright5 link linkWithHash detailsLink")
    for tag in tagi:
        link = tag.get("href")
        LINKI.append(link)


def scrab_obrazów(sup):
    tagi = sup.find_all(name="img", class_="fleft")
    for tag in tagi:
        obraz = tag.get("src")
        OBRAZY.append(obraz)
