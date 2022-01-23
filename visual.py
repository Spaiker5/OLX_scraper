import plotly.graph_objects as go
from dash import dash, dcc, no_update, html, Input, Output
from dash.exceptions import PreventUpdate
from scraby_wyszukania import *

data = data_farming(OLX)
app = dash.Dash()

app.layout = html.Div([
    html.A(children='Po zaznaczeniu ogłoszenia, kliknij w link.', id='link',
           href='https://dash.plot.ly', target='_blank', ),
    dcc.Graph(
        id="figure",
        figure=go.Figure(
            go.Scatter(y=data["Cena"], x=data.index, mode="markers", customdata=data["Link"]),
            layout=go.Layout(clickmode='event+select')),
            clear_on_unhover=True,
    ),
    dcc.Tooltip(id="graph-tooltip"),
    ])
@app.callback(
    Output('link', 'href'),
    [Input('figure', 'hoverData')])


def display_hover_data(hoverData):
    if hoverData:
        target = hoverData['points'][0]['customdata']
        return target
    else:
        raise PreventUpdate


@app.callback(
    Output("graph-tooltip", "show"),
    Output("graph-tooltip", "bbox"),
    Output("graph-tooltip", "children"),
    [Input('figure', 'hoverData')])
def display_hover(hoverData):
    if hoverData is None:
        return False, no_update, no_update

    # demo only shows the first point, but other points may also be available
    pt = hoverData["points"][0]
    bbox = pt["bbox"]
    num = pt["pointNumber"]

    df_row = data.iloc[num]
    img_src = df_row["Obraz"]
    name = df_row["Tytuł"]
    form = df_row["Data"]
    desc = df_row["Cena"]

    children = [
        html.Div([
            html.Img(src=img_src, style={"width": "100%"}),
            html.H2(f"{name}", style={"color": "darkblue"}),
            html.P(f"{form}"),
            html.P(f"{desc}"),
        ], style={'width': '200px', 'white-space': 'normal'})
    ]

    return True, bbox, children


app.run_server(debug=False, use_reloader=False)
