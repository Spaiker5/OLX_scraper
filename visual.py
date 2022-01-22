import plotly.express as px

from config import *


def wizualizacja(data):
    fig = px.scatter(
        data,
        x=data.index,
        y="Cena",
        size="Size",
        hover_name="Tytuł",

        size_max=30,
        hover_data=("Linki", "Data", data.index),
        labels={
            "index": "Data"
        },
        title=f"Ilość stron {STRONY[-1]}",

    )

    fig.show()
