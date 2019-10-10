import pandas as pd
from pathlib import Path

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
    # Set the file path
    filepath = Path("../Resources/aapl.csv")

    # Read the CSV located at the file path into a Pandas DataFrame
    data_df = pd.read_csv(filepath)

    return data_df

def generate_signal(data_df):
    """Generates trading signals for a given dataset."""

    # Set window
    short_window = 10
    long_window = 20

    # Set up the signals DataFrame
    signals = df.copy()
    signals["index"] = pd.to_datetime(signals["index"])
    signals = signals.set_index("index", drop=True)
    signals["signal"] = 0.0

    # Generate the short and long moving averages
    signals["SMA10"] = signals["close"].rolling(window=short_window).mean()
    signals["SMA20"] = signals["close"].rolling(window=long_window).mean()

    # Generate the trading signal 0 or 1,
    signals["signal"][short_window:] = np.where(
        signals["SMA10"][short_window:] > signals["SMA20"][long_window:], 1.0, 0.0
    )

    # Calculate the points in time at which a position should be taken, 1 or -1
    signals["entry/exit"] = signals["signal"].diff()

    return signals

def execute_backtest(signals_df):
    # Set initial capital
    initial_capital = float(100000)

    # Set the share size
    share_size = 500

    # Take a 500 share position where the dual moving average crossover is 1 (SMA50 is greater than SMA100)
    signals_df['Position'] = share_size * signals_df['Signal']

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
    signals_df

    return signals_df

def place_order():
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

def evaluate_metrics(signals_df):
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

    #### CALCULATE TRADE METRICS ####

    trade_evaluation_df = pd.DataFrame(columns=['Stock',
                                            'Entry Date',
                                            'Exit Date',
                                            'Shares',
                                            'Entry Share Price',
                                            'Exit Share Price',
                                            'Entry Portfolio Holding',
                                            'Exit Portfolio Holding',
                                            'Profit/Loss'])

    entry_date = ''
    exit_date = ''
    entry_portfolio_holding = 0
    exit_portfolio_holding = 0
    share_size = 0
    entry_share_price = 0
    exit_share_price = 0

    for index, row in signals_df.iterrows():
        if row['Entry/Exit'] == 1:
            #record = [index, row['Entry/Exit'], row['Portfolio Holdings']]
            print(index, row['Entry/Exit'], row['Portfolio Holdings'])

            entry_date = index
            entry_portfolio_holding = row['Portfolio Holdings']
            share_size = row['Entry/Exit Position']
            entry_share_price = row['close']

            print(f"  Entry Portfolio Holding {entry_portfolio_holding}")
            #trade_evaluation_df = trade_evaluation_df.append(record)
        elif row['Entry/Exit'] == -1:
            print(index, row['Entry/Exit'], signals_df.loc[index].shift(-1)['Portfolio Holdings'])

            exit_date = index
            exit_portfolio_holding = signals_df.loc[index].shift(-1)['Portfolio Holdings']
            exit_share_price = signals_df.loc[index].shift(-1)['close']

            print(f"  Exit Portfolio Holding {exit_portfolio_holding}")

            profit_loss = exit_portfolio_holding - entry_portfolio_holding
            print(f"  Per Trade Profit Loss: {profit_loss}")

            trade_evaluation_df = trade_evaluation_df.append({'Stock': 'AAPL',
                                                            'Entry Date': entry_date,
                                                            'Exit Date': exit_date,
                                                            'Shares': share_size,
                                                            'Entry Share Price': entry_share_price,
                                                            'Exit Share Price': exit_share_price,
                                                            'Entry Portfolio Holding': entry_portfolio_holding,
                                                            'Exit Portfolio Holding': exit_portfolio_holding,
                                                            'Profit/Loss': profit_loss},
                                                            ignore_index=True)

    trade_evaluation_df

    return portfolio_evaluation_df, trade_evaluation_df

def update_dashboard():
    return

def save_data():


    return


account, dashboard = initialize(100000)

# data_df = fetch_data()
# signals_df = generate_signal(data_df)

# signals_df = execute_backtest(signals_df)

# portfolio_evaluation_df, trade_evaluation_df = evaluate_metrics(signals_df)

# update_dashboard(account, signals_df, portfolio_evaluation_df, trade_evaluation_df)

# save_data()
