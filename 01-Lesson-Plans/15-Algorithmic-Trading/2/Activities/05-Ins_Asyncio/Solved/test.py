import ccxt
import pandas as pd
import panel as pn
import os
import hvplot.pandas
import asyncio

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

def update_dashboard(account, data, dashboard):
    """Updates the dashboard with widgets, plots, and financial tables"""
    # Reset DataFrame index
    data.reset_index

    # Create price plot of closing, SMA10, and SMA20
    price_plot = data.hvplot.line(x='index', y=['close'], value_label='Price', width=1000, height=400, rot=90)

    # Create rows
    row_two = pn.Row(price_plot)

    # Create columns
    column = pn.Column(row_two)

    # Create tabs
    tabs = pn.Tabs(("Summary", column))

    # Assign tab to dashboard object
    dashboard[0] = tabs
    return

async def main():

    while True:
        global account
        global data_df
        global dashboard

        # Fetch and save new data
        new_record_df = fetch_data()

        if data_df.empty:
            data_df = new_record_df.copy()
        else:
            data_df = data_df.append(new_record_df, ignore_index=False)

        update_dashboard(account, data_df, dashboard)
        await asyncio.sleep(1)

account, data_df, dashboard = initialize(100000)
dashboard.servable()

# Python 3.7+
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
