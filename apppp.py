import numpy as np
import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html 
from dash.dependencies import Input, Output 

app = dash.Dash(__name__)
x = np.linspace(-10, 10, 100)       # synthesize the data

app.layout = html.Div([
        html.H1('Graphing claculator !!!', style = {'text-align':'centre'}),

        dcc.Dropdown(id = 'graph-type',
                    options = [
                        {'label':'Polynomial','value':'poly'},
                        {'label':'Trigonometric','value':'trig'},
                        {'label':'Logarithmic','value':'log'}],
                    multi = False, 
                    value = 'poly'),

        dcc.Input(id='input-container',
                value = 'x**2'),
        
        html.Br(),

        html.Button(id = 'submit', type = 'submit', children='ok'),

        dcc.Graph(id = 'output-graph', figure = {})
])

@app.callback(
        Output(component_id = 'output-graph', component_property = 'figure'),
         [Input(component_id = 'graph-type', component_property = 'value'),
          Input(component_id = 'input-container', component_property = 'value')]
)

def update_graph(graph_typ, equation):
    global x

    if graph_typ == 'poly':
        y = eval(equation)
    else:
        eq = 'np.' + equation
        y = eval(eq)

    df = pd.DataFrame({
                    'x':x,
                    'y':y})    

    fig = px.line(df, x = df['x'], y = df['y'], title='Your equation plotted!!!')
    fig.show()




if __name__ == '__main__':
    app.run_server(debug=True)
