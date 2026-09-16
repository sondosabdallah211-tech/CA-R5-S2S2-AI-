from dash import Dash, html, dcc, Input
from dash.dependencies import Input, Output

app = Dash(__name__)

app.layout = html.Div([
    html.Button("Submit", id = "number"),
    dcc.Input(placeholder = "Enter a valid number", id = "Data", type = "number" ),
    html.H1(id= "Result")
])

@app.callback(Output("Result", "children" ),
              Input("number", "n_clicks"))


def play_data(n, data):
    if n:
        return f"your enter:{data}"
    return ""
    
app.run(debug=True)

