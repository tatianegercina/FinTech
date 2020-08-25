import os
import numpy as np
import pandas as pd

# @TODO: Import ccxt
import time
from dotenv import load_dotenv


def initialize(cash=None):
    """Initialize the dashboard, data storage, and account balances."""
    print("Intializing Account and DataFrame")

    # @TODO: initialize account and DataFrame


def build_dashboard(data, signals):
    """Build the dashboard."""

    # @TODO: We will complete this later!


def fetch_data():
    """Fetches the latest prices."""
    print("Fetching data...")
    # @TODO: Update to fetch data from kraken


def generate_signals(df):
    """Generates trading signals for a given dataset."""
    print("Generating Signals")
    # Set window
    short_window = 10

    signals = df.copy()
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

    print("Executing Trading Strategy!")

    # @TODO: Update to execute a trade with the new data


print("Initializing account and DataFrame")
account, df = initialize(10000)
print(df)


def main():

    while True:
        global account
        global df

        # Fetch and save new data
        new_df = fetch_data()
        df = df.append(new_df, ignore_index=True)
        min_window = 22
        if df.shape[0] >= min_window:
            signals = generate_signals(df)
            print(signals)
            account = execute_trade_strategy(signals, account)
        time.sleep(1)


main()
