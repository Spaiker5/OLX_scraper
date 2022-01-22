import plotly.express as px
from config import *

def wizualizacja(data):
    fig = px.scatter(
        data,
        x=data.index,
        y="Cena",
        size="Size",
        hover_name="Tytuł",
        log_y=True,
        size_max=30,
        hover_data=("Linki", "Data"),
        labels={
            "index": "Data"
        },
        title=f"Ilość stron {STRONY[-1]}",

    )



    fig.show()
