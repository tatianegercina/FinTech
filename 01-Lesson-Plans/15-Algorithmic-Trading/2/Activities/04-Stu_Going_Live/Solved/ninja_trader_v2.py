import pandas as pd
import numpy as np
from pathlib import Path
import panel as pn
import hvplot.pandas
import ccxt
import os

pn.extension()

def initialize(cash):
    """Initialize the dashboard, data storage, and account balances."""
    # Initialize account
    account = {"balance": cash, "shares": 0}

    # Initialize dashboard
    dashboard = initialize_dashboard()

    return account, dashboard

def initialize_dashboard():
    """Build the dashboard."""
    loading_text = pn.widgets.StaticText(name="Trading Dashboard", value="Loading...")
    dashboard = pn.Column(loading_text)
    print("init dashboard")

    return dashboard

def fetch_data():
    """Fetches the latest prices."""
    # Import Kraken environment variables
    exchange = ccxt.kraken(
        {"apiKey": os.getenv("KRAKEN_PUBLIC_KEY"), "secret": os.getenv("KRAKEN_SECRET_KEY")}
    )
    # Fetch daily candlestick bar data from `BTC/USD`
    historical_prices = exchange.fetch_ohlcv('BTC/USD', '1d')

    # Import the data as a Pandas DataFrame and set the columns
    historical_prices_df = pd.DataFrame(historical_prices, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    historical_prices_df

    # Convert epoch timestamp to date using the `to_datetime` function and `unit` parameter
    historical_prices_df['date'] = pd.to_datetime(historical_prices_df['timestamp'], unit='ms')
    historical_prices_df

    return historical_prices_df

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

def execute_backtest(signals_df):
    """Executes a backtest on trading signal data."""
    # Set initial capital
    initial_capital = float(100000)

    # Set the share size
    share_size = 500
    #print(initial_capital, signals_df['close'][0])
    #share_size = int(initial_capital / signals_df['close'][0])


    # Take a 500 share position where the dual moving average crossover is 1 (SMA50 is greater than SMA100)
    signals_df['Position'] = share_size * signals_df['signal']

    # Find the points in time where a 500 share position is bought or sold
    signals_df['Entry/Exit Position'] = signals_df['Position'].diff()

    # Multiply share price by entry/exit positions and get the cumulatively sum
    signals_df['Portfolio Holdings'] = signals_df['close'] * signals_df['Entry/Exit Position'].cumsum()

    # Subtract the initial capital by the portfolio holdings to get the amount of liquid cash in the portfolio
    signals_df['Portfolio Cash'] = initial_capital - (signals_df['close'] * signals_df['Entry/Exit Position']).cumsum()

    # Get the total portfolio value by adding the cash amount by the portfolio holdings (or investments)
    signals_df['Portfolio Total'] = signals_df['Portfolio Cash'] + signals_df['Portfolio Holdings']

    # Calculate the portfolio daily returns
    signals_df['Portfolio Daily Returns'] = signals_df['Portfolio Total'].pct_change()

    # Calculate the cumulative returns
    signals_df['Portfolio Cumulative Returns'] = (1 + signals_df['Portfolio Daily Returns']).cumprod() - 1

    # Print the DataFrame
    print(signals_df)

    return signals_df

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

def evaluate_metrics(signals_df):
    """Evaluates metrics from backtested signal data"""
    #### CALCULATE PORTFOLIO METRICS ####
    # Initialize index and columns
    metrics= ['Annual Return', 'Cumulative Returns', 'Annual Volatility', 'Sharpe Ratio', 'Sortino Ratio', 'Alpha', 'Beta']
    columns = ['Backtest']

    # Initialize the DataFrame with index set to evaluation metrics and column as `Backtest` (just like PyFolio)
    portfolio_evaluation_df = pd.DataFrame(index=metrics, columns=columns)

    # Assign evaluation metric values from backtest results
    portfolio_evaluation_df.loc['Cumulative Returns'] = signals_df['Portfolio Cumulative Returns'][-1]

    # Calculate annualized return
    portfolio_evaluation_df.loc['Annual Return'] = ((1 + signals_df['Portfolio Daily Returns'].mean())**252 - 1)

    # Calculate annual volatility
    portfolio_evaluation_df.loc['Annual Volatility'] = ((1 + signals_df['Portfolio Daily Returns'].std())** 252 - 1)

    # Calculate Sharpe Ratio
    portfolio_evaluation_df.loc['Sharpe Ratio'] = (signals_df['Portfolio Daily Returns'].mean() * 252) / (signals_df['Portfolio Daily Returns'].std() * np.sqrt(252))

    # Calculate Sortino Ratio
    sortino_ratio_df = signals_df[['Portfolio Daily Returns']]
    sortino_ratio_df['Downside Returns'] = 0
    target = 0
    sortino_ratio_df.loc[sortino_ratio_df['Portfolio Daily Returns'] < target, 'Downside Returns'] = sortino_ratio_df['Portfolio Daily Returns']**2
    down_stdev = np.sqrt(sortino_ratio_df['Downside Returns'].mean())
    expected_return = sortino_ratio_df['Portfolio Daily Returns'].mean()
    sortino_ratio = expected_return/down_stdev
    portfolio_evaluation_df.loc['Sortino Ratio'] = sortino_ratio

    # Print the DataFrame
    print(portfolio_evaluation_df)

    #### CALCULATE TRADE METRICS ####
    trade_evaluation_df = pd.DataFrame(
        columns=[
            'Stock',
            'Entry Date',
            'Exit Date',
            'Shares',
            'Entry Share Price',
            'Exit Share Price',
            'Entry Portfolio Holding',
            'Exit Portfolio Holding',
            'Profit/Loss'
        ]
    )

    entry_date = ''
    exit_date = ''
    entry_portfolio_holding = 0
    exit_portfolio_holding = 0
    share_size = 0
    entry_share_price = 0
    exit_share_price = 0

    for index, row in signals_df.iterrows():
        if row['entry/exit'] == 1:
            entry_date = index
            entry_portfolio_holding = row['Portfolio Holdings']
            share_size = row['Entry/Exit Position']
            entry_share_price = row['close']

        elif row['entry/exit'] == -1:
            exit_date = index
            exit_portfolio_holding = abs(row['close'] * row['Entry/Exit Position'])
            exit_share_price = row['close']

            profit_loss = exit_portfolio_holding - entry_portfolio_holding

            trade_evaluation_df = trade_evaluation_df.append(
                {
                    'Stock': 'AAPL',
                    'Entry Date': entry_date,
                    'Exit Date': exit_date,
                    'Shares': share_size,
                    'Entry Share Price': entry_share_price,
                    'Exit Share Price': exit_share_price,
                    'Entry Portfolio Holding': entry_portfolio_holding,
                    'Exit Portfolio Holding': exit_portfolio_holding,
                    'Profit/Loss': profit_loss
                },
                ignore_index=True)

    # Print the DataFrame
    print(trade_evaluation_df)

    return portfolio_evaluation_df, trade_evaluation_df

def update_dashboard(account, tested_signals_df, portfolio_evaluation_df, trade_evaluation_df):
    """Updates the dashboard with widgets, plots, and financial tables"""
    # Initialize static widgets
    account_balance = pn.widgets.StaticText(name="Cash Balance", value=tested_signals_df['Portfolio Cash'][-1])
    holding_value = pn.widgets.StaticText(name="Portfolio Holding", value=tested_signals_df['Portfolio Holdings'][-1])
    total_portfolio_value = pn.widgets.StaticText(name="Total Portfolio Value", value=tested_signals_df['Portfolio Total'][-1])

    # Create price plot of closing, SMA10, and SMA20
    price_plot = tested_signals_df.hvplot.line(x='date', y=['close', 'SMA10', 'SMA20'], value_label='Price', width=1000, height=400, rot=90)

    # Create portfolio metrics table
    portfolio_evaluation_table = portfolio_evaluation_df.hvplot.table(columns=['index', 'Backtest'], width=300, height=400)

    # Create trade metrics table
    trade_evaluation_table = trade_evaluation_df.hvplot.table(
        columns=[
            'Stock',
            'Entry Date',
            'Exit Date',
            'Shares',
            'Entry Share Price',
            'Exit Share Price',
            'Entry Portfolio Holding',
            'Exit Portfolio Holding',
            'Profit/Loss'
        ]
    )

    # Create rows
    row_one = pn.Row(account_balance, holding_value, total_portfolio_value)
    row_two = pn.Row(price_plot)
    row_three = pn.Row(portfolio_evaluation_table, trade_evaluation_table)

    # Create columns
    column = pn.Column(row_one,
                       row_two,
                       row_three)

    # Create tabs
    tabs = pn.Tabs(("Summary", column))

    # Assign tab to dashboard object
    dashboard[0] = tabs

    return

# Initialize account and dashboard objects
account, dashboard = initialize(100000)
dashboard.servable()

# Fetch data and generate signals
data_df = fetch_data()
signals_df = generate_signal(data_df)

# Backtest signal data, execute trade strategy, and evaluate metrics from backtested results
tested_signals_df = execute_backtest(signals_df)
account  = execute_trade_strategy(tested_signals_df, account)
portfolio_evaluation_df, trade_evaluation_df = evaluate_metrics(tested_signals_df)

# Update the dashboard with all metrics
update_dashboard(account, tested_signals_df, portfolio_evaluation_df, trade_evaluation_df)
