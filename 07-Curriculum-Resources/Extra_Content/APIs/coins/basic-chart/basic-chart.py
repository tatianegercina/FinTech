# -*- coding: utf-8 -*-
import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html

import plotly_express as px

app = dash.Dash(__name__)

df = pd.read_csv('data.csv')
df = df.dropna()
df = df.iloc[:100, :]

fig1 = px.scatter(df, x='')

app.layout = html.Div(children=[
    dcc.Graph(figure=px.scatter(
        df,
        x='date',
        y='country',
        size='Mobile Cell Usage Per 100 People',
        title='This is a test'
    ))
])

if __name__ == '__main__':
    app.run_server(debug=True)
