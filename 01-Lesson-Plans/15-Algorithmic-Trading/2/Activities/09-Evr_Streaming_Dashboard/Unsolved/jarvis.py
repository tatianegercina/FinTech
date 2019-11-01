import os
import numpy as np
import pandas as pd
import ccxt
import asyncio
import sqlite3

# @TODO: Add Streamz libraries!
import panel as pn

pn.extension()


def initialize(cash=None):
    """Initialize the dashboard, data storage, and account balances."""
    print("Intializing account, database, and DataFrame")

    # Initialize Database
    db = sqlite3.connect("algo_trader_history.sqlite")
    with db:
        cur = db.cursor()
        cur.execute("DROP TABLE IF EXISTS data")

    # Initialize Account
    account = {"balance": cash, "shares": 0}

    # @TODO: Add Streamz DataFrames!

    # Initialize the dashboard
    dashboard = build_dashboard()

    # @TODO: We will complete the rest of this later!
    return db, account, df, dashboard


def build_dashboard():
    """Build the dashboard."""
    # @TODO Build a new dashboard using streamz!


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
    print("Generating Signals")
    # Set window
    short_window = 10

    signals = df.copy()
    # @TODO fix the index for the DataFrame!
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


#  @TODO: Initialize everything!
dashboard.servable()


async def main():
    loop = asyncio.get_event_loop()

    while True:
        # @TODO: Use streamz dataframes!

        await asyncio.sleep(1)


# Python 3.7+
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
