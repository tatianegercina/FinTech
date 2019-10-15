import ccxt
import pandas as pd
import panel as pn
import os
import hvplot.pandas
import asyncio
import time

def initialize(cash):
    """Initialize the dashboard, data storage, and account balances."""
    # Initialize Account
    account = {"balance": cash, "shares": 0}

    # Initialize DataFrame


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

    return

def update_dashboard(account, data, dashboard):
    """Updates the dashboard with widgets, plots, and financial tables"""
    # Reset DataFrame index
    data.reset_index

    # Create price plot of closing, SMA10, and SMA20
    price_plot = data.hvplot.line(x='index', y=['close'], value_label='Price', width=1000, height=400, rot=90)

    # Create rows, columns, and tabs
    row_two = pn.Row(price_plot)
    column = pn.Column(row_two)
    tabs = pn.Tabs(("Summary", column))

    # Assign tab to dashboard object
    dashboard[0] = tabs
    return

async def main():

    while True:
        global account
        global data_df
        global dashboard

        # Fetch latest pricing data


        # Save latest pricing data to a global DataFrame


        # Update the dashboard


account, data_df, dashboard = initialize(100000)
dashboard.servable()

# Python 3.7+
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
