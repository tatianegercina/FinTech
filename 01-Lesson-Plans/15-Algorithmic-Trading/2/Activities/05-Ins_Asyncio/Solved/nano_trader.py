import os
import numpy as np
import pandas as pd
import ccxt
import asyncio
import sqlite3

import hvplot.streamz
from streamz import Stream
from streamz.dataframe import DataFrame
import panel as pn
import time

pn.extension()

def initialize(cash):
    """Initialize the dashboard, data storage, and account balances."""
    # Initialize Account
    account = {"balance": cash, "shares": 0}

    # Initialize DataFrame
    data_df = pd.DataFrame()

    # Initialize Streaming DataFrame for the signals
    dashboard = initialize_dashboard()
    return account, data_df, dashboard

def initialize_dashboard():
    """Build the dashboard."""
    loading_text = pn.widgets.StaticText(name="Trading Dashboard", value="Loading...")
    dashboard = pn.Column(loading_text)
    print("init dashboard")
    return dashboard

def fetch_data():
    """Fetches the latest prices."""
    kraken = ccxt.kraken(
        {"apiKey": os.getenv("kraken_key"), "secret": os.getenv("kraken_secret")}
    )
    close = kraken.fetch_ticker("BTC/USD")['close']
    datetime = kraken.fetch_ticker("BTC/USD")['datetime']
    df = pd.DataFrame({'close': [close], 'date': [datetime]})
    df.index = pd.to_datetime([datetime])
    return df

def generate_signal(data_df):
    """Generates trading signals for a given dataset."""
    # Set window
    short_window = 10
    long_window = 20

    # Set up the signals DataFrame
    signals = data_df.copy()
    signals["date"] = pd.to_datetime(signals["date"], infer_datetime_format=True)
    signals = signals.set_index("date", drop=True)
    signals["signal"] = 0.0

    # Generate the short and long moving averages
    signals["SMA10"] = signals["close"].rolling(window=short_window).mean()
    signals["SMA20"] = signals["close"].rolling(window=long_window).mean()

    # Generate the trading signal 0 or 1,
    signals["signal"][short_window:] = np.where(
        signals["SMA10"][short_window:] > signals["SMA20"][short_window:], 1.0, 0.0
    )

    # Calculate the points in time at which a position should be taken, 1 or -1
    signals["entry/exit"] = signals["signal"].diff()

    # Print the DataFrame
    print(signals)
    return signals

def update_dashboard(account, tested_signals_df):
    """Updates the dashboard with widgets, plots, and financial tables"""
    # Initialize static widgets
    account_balance = pn.widgets.StaticText(name="Cash Balance", value=tested_signals_df['Portfolio Cash'][-1])
    holding_value = pn.widgets.StaticText(name="Portfolio Holding", value=tested_signals_df['Portfolio Holdings'][-1])
    total_portfolio_value = pn.widgets.StaticText(name="Total Portfolio Value", value=tested_signals_df['Portfolio Total'][-1])

    # Create price plot of closing, SMA10, and SMA20
    price_plot = tested_signals_df.hvplot.line(x='date', y=['close', 'SMA10', 'SMA20'], value_label='Price', width=1000, height=400, rot=90)

    # Create rows
    row_one = pn.Row(account_balance, holding_value, total_portfolio_value)
    row_two = pn.Row(price_plot)

    # Create columns
    column = pn.Column(row_one, row_two)

    # Create tabs
    tabs = pn.Tabs(("Summary", column))

    # Assign tab to dashboard object
    dashboard[0] = tabs
    return

def main():

    while True:
        global account
        global data_df
        global dashboard

        # Fetch and save new data
        new_record_df = fetch_data()

        if data_df.empty:
            data_df = new_record_df.copy()
        else:
            data_df = data_df.append(new_record_df, ignore_index=True)

        # Generate Signals and execute the trading strategy
        min_window = 30
        if data_df.shape[0] >= min_window:
            signals = generate_signal(data_df)
            print(f"Account Balance: {account['balance']}")
            print(f"Account Shares: {account['shares']}")

        # Update the Dashboard
        update_dashboard(account, signals)
        time.sleep(1)

account, data_df, dashboard = initialize(10000)
dashboard.servable()

main()
