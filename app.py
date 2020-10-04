import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
import numpy as np
import pandas as pd

app = dash.Dash(external_stylesheets = [dbc.themes.SUPERHERO])
server = app.server

colors = {
    'background': '#1b2e41',
    'text': 'lightblue'
}

app.layout = html.Div([
                    html.Br(),
                    dcc.Input(id = 'eq', value = 'x', type = 'text'),
                    html.Button(id='eq-submit', n_clicks = 0, children = 'Plot !!!'),

                    html.Br(),
                    html.Br(),

                    html.Div(id = 'output-graph'),

                    html.Br(),
                    html.P('Double click to switch between scales')
], id = 'fallback')

@app.callback(
        Output(component_id = 'output-graph', component_property = 'children'),
        [Input(component_id = 'eq-submit', component_property = 'n_clicks')],

        [State('eq', 'value')]
)

def update(n__clicks, eq):
    equation = eq[:]
    eq = eq.replace('^', '**')
    y_range =  dict(range = [-5, 5])
    x_range =  dict(range = [-5, 5])


    if 'tan' in eq:
        eq = eq[:eq.find('tan'):] + 'np.' + eq[eq.find('tan'):]
        x = np.linspace(-4*np.pi, 4*np.pi, 99999)

    if 'sin' in eq:
        eq = eq[:eq.find('sin'):] + 'np.' + eq[eq.find('sin'):]
        x = np.linspace(-4*np.pi, 4*np.pi, 2200)

    if 'cos' in eq:
        eq = eq[:eq.find('cos'):] + 'np.' + eq[eq.find('cos'):]
        x = np.linspace(-4*np.pi, 4*np.pi, 2200)

    else:
        x = np.linspace(-50, 50, 5000)

    y = eval(eq)
    df = pd.DataFrame({
                     'x':x,
                     'y':y})

    fig = go.Figure(
                data = [go.Line(
                            x = df['x'], y = df['y']
                        )],
                layout = {
                    'title':eq,
                    'yaxis':y_range,
                    'xaxis':x_range,
                    'plot_bgcolor':colors['background'],
                    'paper_bgcolor': colors['background'],
                    'font_color':colors['text']
                    } 
                )
    
                layout=)
    
    fig.update_xaxes(showline=True, linewidth=2, linecolor='lightblue')
    fig.update_yaxes(showline=True, linewidth=2, linecolor='lightblue')


    return dcc.Graph(
                 id = 'graph',
                 figure=fig
            )

if __name__ == '__main__':
    app.run_server()
