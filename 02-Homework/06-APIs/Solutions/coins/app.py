# -*- coding: utf-8 -*-
import pandas as pd

from fetch_data import get_stocks, get_coin_prices

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

import plotly_express as px
import plotly.graph_objs as go
import plotly.figure_factory as ff
from plotly.offline import download_plotlyjs, plot, iplot

app = dash.Dash(__name__)

stocks = get_stocks()

trace_high = go.Scatter(x=stocks.Date, y=stocks.High, name="AAPL High")

trace_low = go.Scatter(x=stocks.Date, y=stocks.Low, name="AAPL Low")

layout = dict(
    title="Historical Coin Prices",
    xaxis=dict(
        rangeselector=dict(
            buttons=list(
                [
                    dict(count=1, label="1m", step="month", stepmode="backward"),
                    dict(count=6, label="6m", step="month", stepmode="backward"),
                    dict(step="all"),
                ]
            )
        ),
        rangeslider=dict(visible=True),
        type="date",
    ),
)

data = [trace_high, trace_low]

table_figure = ff.create_table(stocks.iloc[:10, :])

# fig1 = px.scatter(df, x='')

app.layout = html.Div(
    children=[
        dcc.Input(id="input-1-state", type="text", value="United States"),
        dcc.Input(id="input-2-state", type="text", value="Canada"),
        html.Button(id="submit-button", n_clicks=0, children="Submit"),
        html.Div(id="output-state"),
        dcc.Graph(figure={"data": data, "layout": layout}),
        dcc.Graph(id="stocks-table", figure=table_figure),
    ]
)


@app.callback(
    Output("output-state", "children"),
    [Input("submit-button", "n_clicks")],
    [State("input-1-state", "value"), State("input-2-state", "value")],
)
def update_output(n_clicks, input1, input2):
    return u"""
        The Button has been pressed {} times,
        Input 1 is "{}",
        and Input 2 is "{}"
    """.format(
        n_clicks, input1, input2
    )


if __name__ == "__main__":
    app.run_server(debug=True)
