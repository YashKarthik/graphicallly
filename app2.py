import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import numpy as np
import pandas as pd

app = dash.Dash(__name__)
x = np.linspace(-50, 50, 5000)

app.layout = html.Div([
                    dcc.Dropdown(id = 'graph-type',
                                options = [
                                    {'label':'Polynomial','value':'poly'},
                                    {'label':'Trigonometric','value':'trig'},
                                    ],
                                multi = False,
                                value = 'poly'),

                    dcc.Input(id = 'equation', value = 'x', type = 'text'),
    html.Button(id='eq-submit', n_clicks = 0, children = 'plot !!!',
                style = {
                    'background-color':'lightblue', 'border-radius':'10px'}),
                    html.Div(id = 'output-graph')
])

@app.callback(
        Output(component_id = 'output-graph', component_property = 'children'),
        [Input(component_id = 'eq-submit', component_property = 'n_clicks')],

        [State('equation', 'value'),
         State('graph-type', 'value')]
)

def update(n__clicks, equation, graph_type):
    equation = equation.replace('^', '**')

    if graph_type == 'trig':
         eq = 'np.'+ equation

    else:
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
                         'title':equation
                     }
                 }
    )

if __name__ == '__main__':
    app.run_server(debug = True)
