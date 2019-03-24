# -*- coding: utf-8 -*-
import pandas as pd

from fetch_data import get_stock, get_stock_news

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

import plotly_express as px
import plotly.graph_objs as go
import plotly.figure_factory as ff
from plotly.offline import download_plotlyjs, plot, iplot

app = dash.Dash(__name__)


def build_line_chart(stocks, ticker):

    trace_high = go.Scatter(x=stocks.Date, y=stocks.High, name=f"{ticker} High")

    trace_low = go.Scatter(x=stocks.Date, y=stocks.Low, name=f"{ticker} Low")

    layout = dict(
        title="Historical Stock Prices",
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
    line_figure = {"data": data, "layout": layout}

    return line_figure

def build_table(stocks, ticker):
    table_figure = ff.create_table(stocks.iloc[:10, :])
    return table_figure

default_ticker = "AAPL"
stocks = get_stock(default_ticker)
line_figure = build_line_chart(stocks, ticker=default_ticker)
table_figure = build_table(stocks, ticker=default_ticker)

app.layout = html.Div(className='grid-container',
    children=[
        html.Div(className="News"),
        html.Div(children=[
            dcc.Input(id="stock-ticker", type="text", value="AAPL"),
            html.Button(id="submit-button", n_clicks=0, children="Submit")], className="Search"),
        html.Div(dcc.Graph(id="stock-line", figure=line_figure), className="stocks-line"),
        html.Div(dcc.Graph(id="stock-table", figure=table_figure), className="stocks-table"),
    ]
)


@app.callback(
    Output("stock-line", "figure"),
    [Input("submit-button", "n_clicks")],
    [State("stock-ticker", "value")],
)
def update_output(n_clicks, input1):
    stocks = get_stock(input1)
    return build_line_chart(stocks, input1)

@app.callback(
    Output("stock-table", "figure"),
    [Input("submit-button", "n_clicks")],
    [State("stock-ticker", "value")],
)
def update_output(n_clicks, input1):
    stocks = get_stock(input1)
    return build_table(stocks, input1)

if __name__ == "__main__":
    app.run_server(debug=True)
