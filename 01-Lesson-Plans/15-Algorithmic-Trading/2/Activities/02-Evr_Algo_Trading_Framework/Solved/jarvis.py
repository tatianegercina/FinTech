import numpy as np
import pandas as pd
from pathlib import Path
import hvplot.pandas
import panel as pn


def initialize():
    """Initialize the dashboard, data storage, and account balances."""
    # @TODO: We will complete this later!
    pass


def build_dashboard(signals_df, portfolio_evaluation_df):
    """Build the dashboard."""
    # Create hvplot visualizations
    price_df = signals_df[["close", "SMA50", "SMA100"]]
    price_chart = price_df.hvplot.line().opts(xaxis=None)
    portfolio_evaluation_table = portfolio_evaluation_df.hvplot.table(
        columns=["index", "Backtest"]
    )

    # Build the dashboard
    dashboard = pn.Column(
        "# Trading Dashboard", price_chart, portfolio_evaluation_table
    )
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
    # Grab just the `date` and `close` from the dataset
    signals_df = data_df.loc[:, ["date", "close"]].copy()

    # Set the `date` column as the index
    signals_df = signals_df.set_index("date", drop=True)

    # Set the short window and long windows
    short_window = 50
    long_window = 100

    # Generate the short and long moving averages (50 and 100 days, respectively)
    signals_df["SMA50"] = signals_df["close"].rolling(window=short_window).mean()
    signals_df["SMA100"] = signals_df["close"].rolling(window=long_window).mean()
    signals_df["Signal"] = 0.0

    # Generate the trading signal 0 or 1,
    # where 0 is when the SMA50 is under the SMA100, and
    # where 1 is when the SMA50 is higher (or crosses over) the SMA100
    signals_df["Signal"][short_window:] = np.where(
        signals_df["SMA50"][short_window:] > signals_df["SMA100"][short_window:],
        1.0,
        0.0,
    )

    # Calculate the points in time at which a position should be taken, 1 or -1
    signals_df["Entry/Exit"] = signals_df["Signal"].diff()

    return signals_df


def execute_backtest(signals_df):
    """Backtests signal data."""
    # Set initial capital
    initial_capital = float(100000)

    # Set the share size
    share_size = 500

    # Take a 500 share position where the dual moving average crossover is 1 (SMA50 is greater than SMA100)
    signals_df["Position"] = share_size * signals_df["Signal"]

    # Find the points in time where a 500 share position is bought or sold
    signals_df["Entry/Exit Position"] = signals_df["Position"].diff()

    # Multiply share price by entry/exit positions and get the cumulatively sum
    signals_df["Portfolio Holdings"] = (
        signals_df["close"] * signals_df["Entry/Exit Position"].cumsum()
    )

    # Subtract the initial capital by the portfolio holdings to get the amount of liquid cash in the portfolio
    signals_df["Portfolio Cash"] = (
        initial_capital
        - (signals_df["close"] * signals_df["Entry/Exit Position"]).cumsum()
    )

    # Get the total portfolio value by adding the cash amount by the portfolio holdings (or investments)
    signals_df["Portfolio Total"] = (
        signals_df["Portfolio Cash"] + signals_df["Portfolio Holdings"]
    )

    # Calculate the portfolio daily returns
    signals_df["Portfolio Daily Returns"] = signals_df["Portfolio Total"].pct_change()

    # Calculate the cumulative returns
    signals_df["Portfolio Cumulative Returns"] = (
        1 + signals_df["Portfolio Daily Returns"]
    ).cumprod() - 1

    return signals_df


def execute_trade_strategy():
    """Makes a buy/sell/hold decision."""
    # @TODO: We will complete this later!
    pass


def evaluate_metrics(signals_df):
    """Generates evaluation metrics from backtested signal data."""
    # Prepare DataFrame for metrics
    metrics = [
        "Annual Return",
        "Cumulative Returns",
        "Annual Volatility",
        "Sharpe Ratio",
        "Sortino Ratio",
    ]

    columns = ["Backtest"]

    # Initialize the DataFrame with index set to evaluation metrics and column as `Backtest` (just like PyFolio)
    portfolio_evaluation_df = pd.DataFrame(index=metrics, columns=columns)

    # Calculate cumulative return
    portfolio_evaluation_df.loc["Cumulative Returns"] = signals_df[
        "Portfolio Cumulative Returns"
    ][-1]

    # Calculate annualized return
    portfolio_evaluation_df.loc["Annual Return"] = (
        signals_df["Portfolio Daily Returns"].mean() * 252
    )

    # Calculate annual volatility
    portfolio_evaluation_df.loc["Annual Volatility"] = (
        1 + signals_df["Portfolio Daily Returns"].std() * np.sqrt(252)
    )

    # Calculate Sharpe Ratio
    portfolio_evaluation_df.loc["Sharpe Ratio"] = (
        signals_df["Portfolio Daily Returns"].mean() * 252
    ) / (signals_df["Portfolio Daily Returns"].std() * np.sqrt(252))

    # Calculate Downside Return
    sortino_ratio_df = signals_df[["Portfolio Daily Returns"]].copy()
    sortino_ratio_df.loc[:, "Downside Returns"] = 0

    target = 0
    mask = sortino_ratio_df["Portfolio Daily Returns"] < target
    sortino_ratio_df.loc[mask, "Downside Returns"] = (
        sortino_ratio_df["Portfolio Daily Returns"] ** 2
    )
    portfolio_evaluation_df

    # Calculate Sortino Ratio
    down_stdev = np.sqrt(sortino_ratio_df["Downside Returns"].mean()) * np.sqrt(252)
    expected_return = sortino_ratio_df["Portfolio Daily Returns"].mean() * 252
    sortino_ratio = expected_return / down_stdev

    portfolio_evaluation_df.loc["Sortino Ratio"] = sortino_ratio

    return portfolio_evaluation_df


def main():
    """Main Event Loop."""
    data_df = fetch_data()
    signals_df = generate_signals(data_df)
    tested_signals_df = execute_backtest(signals_df)
    portfolio_evaluation_df = evaluate_metrics(tested_signals_df)
    dashboard = build_dashboard(tested_signals_df, portfolio_evaluation_df)
    dashboard.servable()
    return


main()
