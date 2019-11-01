import ccxt
import pandas as pd
import panel as pn
import os
import hvplot.pandas
import hvplot.streamz
import asyncio
import time
import sqlite3
from streamz import Stream
from streamz.dataframe import DataFrame
import numpy as np

def initialize(cash):
    """Initialize the dashboard, data storage, and account balances."""
    # Initialize Account
    account = {"balance": cash, "shares": 0}

    # Initialize Database
    db = sqlite3.connect("algo_trader_history.sqlite")

    # Initialize Streaming DataFrame for Signals
    signals_stream = Stream()
    columns = ["close", "sma10", "sma20"]
    data = {"close": [],  "sma10": [], "sma20": []}
    signals_example = pd.DataFrame(data=data, columns=columns, index=pd.DatetimeIndex([]))
    signals_stream_df = DataFrame(signals_stream, example=signals_example)

    # Initialize Streaming DataFrame for the signals
    dashboard = build_dashboard(signals_stream_df)
    return account, db, signals_stream, dashboard

def build_dashboard(signals):
    """Build the dashboard."""
    column = pn.Column(signals.hvplot.line())
    column_test = pn.Column()

    dashboard = pn.Tabs(("Summary", column), ("Tab 2", column_test))
    return dashboard

def fetch_data():
    """Fetches the latest prices."""
    kraken = ccxt.kraken(
        {"apiKey": os.getenv("KRAKEN_PUBLIC_KEY"), "secret": os.getenv("KRAKEN_SECRET_KEY")}
    )
    close = kraken.fetch_ticker("BTC/USD")['close']
    datetime = kraken.fetch_ticker("BTC/USD")['datetime']
    df = pd.DataFrame({'close': [close], 'date': [datetime]})
    df.index = pd.to_datetime([datetime])
    return df

def generate_signal(df):
    """Generates trading signals for a given dataset."""
    # Set window
    short_window = 10

    signals = df.copy()
    signals["index"] = pd.to_datetime(signals["index"])
    signals = signals.set_index('index', drop=True)
    signals["signal"] = 0.0

    # Generate the short and long moving averages
    signals["sma10"] = signals["close"].rolling(window=10).mean()
    signals["sma20"] = signals["close"].rolling(window=20).mean()

    # Generate the trading signal 0 or 1,
    signals["signal"][short_window:] = np.where(
        signals["sma10"][short_window:] > signals["sma20"][short_window:], 1.0, 0.0
    )

    # Calculate the points in time at which a position should be taken, 1 or -1
    signals["entry/exit"] = signals["signal"].diff()

    return signals


def execute_trade_strategy(signals, account):
    """Makes a buy/sell/hold decision."""

    if signals["entry/exit"][-1] == 1.0:
        print("buy")
        number_to_buy = round(account['balance'] / signals['close'][-1], 0) * .001
        account["balance"] -= (number_to_buy * signals['close'][-1])
        account["shares"] += number_to_buy
    elif signals["entry/exit"][-1] == -1.0:
        print("sell")
        account["balance"] += signals['close'][-1] * account['shares']
        account["shares"] = 0
    else:
        print("hold")

    return account

async def main():

    while True:
        global db
        global account
        global signals_stream

        # Fetch and save new data
        new_df = await loop.run_in_executor(None, fetch_data)
        new_df.to_sql('data', db, if_exists='append', index=True)

        # Generate Signals and execute the trading strategy
        min_window = 30
        max_window = 1000
        df = pd.read_sql(f"select * from data limit {max_window}", db)
        if df.shape[0] >= min_window:
            signals = generate_signal(df)
            signals_stream.emit(signals[['close', 'sma10', 'sma20']].tail(1))
            account = execute_trade_strategy(signals, account)
            print(f"Account Balance: {account['balance']}")
            print(f"Account Shares: {account['shares']}")

        # Update the Dashboard
        await asyncio.sleep(1)


account, db, signals_stream, dashboard = initialize(100000)
dashboard.servable()

# Python 3.7+
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
