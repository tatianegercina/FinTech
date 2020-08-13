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

pn.extension()


def initialize(cash=None):
    """Initialize the dashboard, data storage, and account balances."""

    # Initialize Database
    db = sqlite3.connect("algo_trader_history.sqlite")
    with db:
        cur = db.cursor()
        cur.execute("DROP TABLE IF EXISTS data")

    # Initialize Account
    account = {"balance": cash, "shares": 0}

    # Initialize Streaming DataFrame for Raw Data
    data_stream = Stream()
    data_example = pd.DataFrame(
        data={"close": []}, columns=["close"], index=pd.DatetimeIndex([])
    )
    data_stream_df = DataFrame(data_stream, example=data_example)

    # Initialize Streaming DataFrame for Signals
    signals_stream = Stream()
    columns = ["close", "signal", "sma10", "sma20", "entry/exit"]
    data = {"close": [], "signal": [], "sma10": [], "sma20": [], "entry/exit": []}
    signals_example = pd.DataFrame(
        data=data, columns=columns, index=pd.DatetimeIndex([])
    )
    signals_stream_df = DataFrame(signals_stream, example=signals_example)

    # Initialize Streaming DataFrame for the signals
    dashboard = build_dashboard(data_stream_df, signals_stream_df)
    return db, account, data_stream, signals_stream, dashboard


def build_dashboard(data, signals):
    """Build the dashboard."""

    signals_plot = (
        signals[signals["entry/exit"] == 1.0].hvplot.scatter(
            y="sma10", marker="^", size=200, c="g", label="buy", padding=0.1
        )
        * signals[signals["entry/exit"] == -1.0].hvplot.scatter(
            y="sma10", marker="v", size=200, c="r", label="sell", padding=0.1
        )
        * signals.hvplot.line(y="sma10", label="sma10")
        * signals.hvplot.line(y="sma20", label="sma20")
    )
    dashboard = pn.Column(
        "# JARVIS Algorithmic Trading Dashboard",
        data.hvplot(title="prices"),
        signals_plot.opts(title="signals plot", show_legend=False),
        "### Signals Table",
        signals.hvplot.table(
            title="signals table",
            columns=["close", "entry/exit", "sma10", "sma20"],
            backlog=10,
        ),
    )
    return dashboard


def fetch_data():
    """Fetches the latest prices."""
    kraken_public_key = os.getenv("KRAKEN_PUBLIC_KEY")
    kraken_secret_key = os.getenv("KRAKEN_SECRET_KEY")
    kraken = ccxt.kraken({"apiKey": kraken_public_key, "secret": kraken_secret_key})

    close = kraken.fetch_ticker("BTC/USD")["close"]
    datetime = kraken.fetch_ticker("BTC/USD")["datetime"]
    df = pd.DataFrame({"close": [close]})
    df.index = pd.to_datetime([datetime])
    return df


def generate_signals(df):
    """Generates trading signals for a given dataset."""
    # Set window
    short_window = 10

    signals = df.copy()
    signals["index"] = pd.to_datetime(signals["index"])
    signals = signals.set_index("index", drop=True)
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
        number_to_buy = round(account["balance"] / signals["close"][-1], 0) * 0.001
        account["balance"] -= number_to_buy * signals["close"][-1]
        account["shares"] += number_to_buy
    elif signals["entry/exit"][-1] == -1.0:
        print("sell")
        account["balance"] += signals["close"][-1] * account["shares"]
        account["shares"] = 0
    else:
        print("hold")

    return account


db, account, data_stream, signals_stream, dashboard = initialize(10000)
dashboard.servable()


async def main():
    loop = asyncio.get_event_loop()

    while True:
        global db
        global account
        global data_stream
        global signals_stream

        # Fetch and save new data
        new_df = await loop.run_in_executor(None, fetch_data)
        new_df.to_sql("data", db, if_exists="append", index=True)

        # Generate Signals and execute the trading strategy
        min_window = 21
        max_window = 1000
        df = pd.read_sql(f"select * from data limit {max_window}", db)
        if df.shape[0] >= min_window:
            signals = generate_signals(df)
            signals_stream.emit(signals)
            account = execute_trade_strategy(signals, account)
            print(f"Account Balance: {account['balance']}")
            print(f"Account Shares: {account['shares']}")

        # Update the Dashboard
        data_stream.emit(new_df)
        await asyncio.sleep(1)


# Python 3.7+
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
