import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import numpy as np
import pandas as pd

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([
                    html.Br(),
                    dcc.Input(id = 'equation', value = 'x', type = 'text'),
                    html.Button(id='eq-submit', n_clicks = 0, children = 'Plot !!!',
                                style = {
                                    'background-color':'lightblue', 'border-radius':'10px'}),

                    html.Div(id = 'output-graph',
                             style = {
                                'overflow':'allow'},
                    ),
                    html.P('Double click to switch between scales',
                          style = {
                                'color':'#91b1bf',
                                'font-family':'Avenir'})
])

@app.callback(
        Output(component_id = 'output-graph', component_property = 'children'),
        [Input(component_id = 'eq-submit', component_property = 'n_clicks')],

        [State('equation', 'value')]
)

def update(n__clicks, equation):
    equation = equation.replace('^', '**')
    y_range =  dict(range = [-5, 5])
    x_range =  dict(range = [-5, 5])

    if 'sin' in equation or 'cos' in equation or 'tan' in equation:









        if 'tan' in eq:
            x = np.linspace(-4*np.pi, 4*np.pi, 99999)

        else:
            x = np.linspace(-4*np.pi, 4*np.pi, 2200)

    else:
        x = np.linspace(-50, 50, 5000)
        eq = equation

    y = eval(eq)
    df = pd.DataFrame({
                     'x':x,
                     'y':y})

    return dcc.Graph(
                 id = 'graph',
                 figure={
                     'data': [{
                         'x':df['x'], 'y':df['y'],
                         'type':'line', 'name':equation},
                     ],
                     'layout':{
                         'title':equation,
                         'yaxis':y_range,
                         'xaxis':x_range
                     }
                 }
            )

if __name__ == '__main__':
    app.run_server()
