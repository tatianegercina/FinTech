import pandas as pd
from pathlib import Path
import numpy as np
import hvplot.pandas
import panel as pn

def initialize():
    """Initialize the dashboard, data storage, and account balances."""
    return

def build_dashboard(signals_df, portfolio_evaluation_df, trade_evaluation_df):
    """Build the dashboard."""
    # Create hvplot visualizations
    price_plot = signals_df.hvplot.line(x='date', y=['close', 'sma10', 'sma20'], value_label='Price', width=1000, height=400, rot=90)
    portfolio_evaluation_table = portfolio_evaluation_df.hvplot.table(columns=['index', 'Backtest'], width=300, height=400)
    trade_evaluation_table = trade_evaluation_df.hvplot.table()

    # Create rows, columns, and tabs
    row_one = pn.Row(price_plot)
    row_two = pn.Row(portfolio_evaluation_table, trade_evaluation_table)
    column = pn.Column(row_one, row_two)
    tabs = pn.Tabs(("Summary", column))

    # Assign dashboard
    dashboard = tabs
    return dashboard

def fetch_data():
    """Fetches the latest prices."""
    # Set the file path and read CSV into a Pandas DataFrame
    filepath = Path("../Resources/aapl.csv")
    data_df = pd.read_csv(filepath)

    # Print the DataFrame
    print(data_df.head())
    return data_df

def generate_signals(data_df):
    """Generates trading signals for a given dataset."""
    # Set window
    short_window = 10
    long_window = 20

    # Set up the signals DataFrame
    signals_df = data_df.copy()
    signals_df["date"] = pd.to_datetime(signals_df["date"], infer_datetime_format=True)
    signals_df = signals_df.set_index("date", drop=True)
    signals_df["signal"] = 0.0

    # Generate the short and long moving averages
    signals_df["sma10"] = signals_df["close"].rolling(window=short_window).mean()
    signals_df["sma20"] = signals_df["close"].rolling(window=long_window).mean()

    # Generate the trading signal 0 or 1,
    signals_df["signal"][short_window:] = np.where(
        signals_df["sma10"][short_window:] > signals_df["sma20"][short_window:], 1.0, 0.0
    )

    # Calculate the points in time at which a position should be taken, 1 or -1
    signals_df["entry/exit"] = signals_df["signal"].diff()

    # Print the DataFrame
    print(signals_df.head())
    return signals_df

def execute_backtest(signals_df):
    """Backtests signal data."""
    # Set initial capital
    initial_capital = float(100000)

    # Set the share size
    share_size = 500

    # Calculate backtest metrics
    signals_df['Position'] = share_size * signals_df['signal']
    signals_df['Entry/Exit Position'] = signals_df['Position'].diff()
    signals_df['Portfolio Holdings'] = signals_df['close'] * signals_df['Entry/Exit Position'].cumsum()
    signals_df['Portfolio Cash'] = initial_capital - (signals_df['close'] * signals_df['Entry/Exit Position']).cumsum()
    signals_df['Portfolio Total'] = signals_df['Portfolio Cash'] + signals_df['Portfolio Holdings']
    signals_df['Portfolio Daily Returns'] = signals_df['Portfolio Total'].pct_change()
    signals_df['Portfolio Cumulative Returns'] = (1 + signals_df['Portfolio Daily Returns']).cumprod() - 1

    # Print the DataFrame
    print(signals_df.head())
    return signals_df

def execute_trade_strategy():
    """Makes a buy/sell/hold decision."""
    return

def evaluate_metrics(signals_df):
    """Generates evaluation metrics from backtested signal data."""
    #### CALCULATE PORTFOLIO METRICS ####
    # Initialize index and columns
    metrics= ['Annual Return', 'Cumulative Returns', 'Annual Volatility', 'Sharpe Ratio', 'Sortino Ratio']
    columns = ['Backtest']

    # Initialize the DataFrame with index set to evaluation metrics and column as `Backtest` (just like PyFolio)
    portfolio_evaluation_df = pd.DataFrame(index=metrics, columns=columns)

    # Assign portfolio evaluation metrics for each index
    portfolio_evaluation_df.loc['Cumulative Returns'] = signals_df['Portfolio Cumulative Returns'][-1]
    portfolio_evaluation_df.loc['Annual Return'] = ((1 + signals_df['Portfolio Daily Returns'].mean())**252 - 1)
    portfolio_evaluation_df.loc['Annual Volatility'] = ((1 + signals_df['Portfolio Daily Returns'].std())** 252 - 1)
    portfolio_evaluation_df.loc['Sharpe Ratio'] = (signals_df['Portfolio Daily Returns'].mean() * 252) / (signals_df['Portfolio Daily Returns'].std() * np.sqrt(252))

    # Calculate sortino ratio
    sortino_ratio_df = signals_df[['Portfolio Daily Returns']]
    sortino_ratio_df['Downside Returns'] = 0
    target = 0
    sortino_ratio_df.loc[sortino_ratio_df['Portfolio Daily Returns'] < target, 'Downside Returns'] = sortino_ratio_df['Portfolio Daily Returns']**2
    down_stdev = np.sqrt(sortino_ratio_df['Downside Returns'].mean())
    expected_return = sortino_ratio_df['Portfolio Daily Returns'].mean()
    sortino_ratio = expected_return/down_stdev
    portfolio_evaluation_df.loc['Sortino Ratio'] = sortino_ratio

    # Print the DataFrame
    print(portfolio_evaluation_df.head())

    #### CALCULATE TRADE METRICS ####
    trade_evaluation_df = pd.DataFrame(
        columns=['Stock', 'Entry Date', 'Exit Date', 'Shares', 'Entry Share Price', 'Exit Share Price', 'Entry Portfolio Holding', 'Exit Portfolio Holding', 'Profit/Loss']
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
                {'Stock': 'AAPL', 'Entry Date': entry_date, 'Exit Date': exit_date, 'Shares': share_size, 'Entry Share Price': entry_share_price, 'Exit Share Price': exit_share_price, 'Entry Portfolio Holding': entry_portfolio_holding, 'Exit Portfolio Holding': exit_portfolio_holding, 'Profit/Loss': profit_loss},
                ignore_index=True)

    # Print the DataFrame
    print(trade_evaluation_df.head())
    return portfolio_evaluation_df, trade_evaluation_df

def main():
    """Main Event Loop."""
    data_df = fetch_data()
    signals_df = generate_signals(data_df)
    tested_signals_df = execute_backtest(signals_df)
    portfolio_evaluation_df, trade_evaluation_df = evaluate_metrics(tested_signals_df)
    dashboard = build_dashboard(tested_signals_df, portfolio_evaluation_df, trade_evaluation_df)
    dashboard.servable()
    return

main()
