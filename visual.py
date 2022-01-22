import plotly.express as px


def wizualizacja(data):
    fig = px.scatter(
        data, y="Data",
        x="Cena",
        size="Size",
        hover_name="Tytuł",
        log_x=True,
        size_max=60,

    )

    fig.show()
