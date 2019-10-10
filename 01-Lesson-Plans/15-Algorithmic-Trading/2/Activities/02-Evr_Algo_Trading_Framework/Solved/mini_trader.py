# Import libraries and dependencies
import ccxt
import time
import pandas as pd
import pprint as pp
import datetime
import asyncio
import sqlite3
import panel as pn
import hvplot.pandas
import numpy as np
import math
import plotly_express as px
pn.extension()

# Suppress warnings
import warnings
warnings.simplefilter(action='ignore', category=UserWarning)
warnings.simplefilter(action='ignore', category=RuntimeWarning)
pd.set_option('mode.chained_assignment', None)

def initialize(cash):
    """Initialize the account balance, data storage, and dashboard.

    Args:
        cash (float): The original investment amount.

    Returns: A tuple with the account balances and a DataFrame for prices.
    """
    # Initialize account cash balance
    account = {
        "cash_balance": cash,
        "portfolio_holding": 0,
        "total_portfolio_value": 0,
        "buy_counter": 0,
        "sell_counter": 0
    }

    # Initialize DataFrames to hold data
    api_data_df = pd.DataFrame()
    signals_df = pd.DataFrame()
    trade_evaluation_df = pd.DataFrame()

    # Initialize dashboard
    dashboard = initialize_dashboard()

    print("Init account")
    return account, api_data_df, signals_df, trade_evaluation_df, dashboard

def initialize_dashboard():
    """Initialize the dashboard."""
    loading_text = pn.widgets.StaticText(name="Trading Dashboard", value="Loading...")
    dashboard = pn.Column(loading_text)
    print("init dashboard")
    return dashboard

def fetch_data():
    """Fetches the latest prices.

    This function uses a trading api to fetch the latest prices and then updates
    the input DataFrame with the latest data.

    Args:
        df (obj): A Pandas DataFrame with historical prices

    Returns: A Pandas DataFrame with historical + latest prices.
    """

    # Set the public and private keys for the API
    exchange = ccxt.kraken({
        'apiKey': 'mvCmUR7Ji9iLjLDhe8OZvdQ0nJPp7i+BCszr8ENlu1NxeEeduEzP99Co',
        'secret': 'bBFr4we3uc+nl/1d3OBvkoK3Zz2/c3QaGch7lBqe8hPYOynew3htWxrTSHEJALG/ej0EkzJ8at3zyoRIjHwaxA==',
    })

    # Connect to Kraken and load the available cyptocurrency datasets
    print(f"{datetime.datetime.now()} [INFO] ----Entering fetch_data() function")
    print(f"{datetime.datetime.now()} [INFO] Connecting to Cryptocurrency Exchange... {exchange.name}")
    currency_details = exchange.load_markets()

    # Print the list of available currencies
    print(f"{datetime.datetime.now()} [INFO] Generating available list of cryptocurrencies.")
    #print(currency_details.keys())

    # Grab the current price details for BTC/USD and convert to a DataFrame
    print(f"{datetime.datetime.now()} [INFO] Grabbing price details for... BTC/USD")
    current_price_details = kraken.fetch_ticker('BTC/USD')

    # Import current price details as Pandas DataFrame and print it
    print(f"{datetime.datetime.now()} [INFO] Displaying price details for BTC/USD as a Pandas DataFrame")
    crypto_df = pd.DataFrame(current_price_details)
    #print(crypto_df)

    # Drop extraneous `info` column
    print(f"{datetime.datetime.now()} [INFO] Filtering down content to a single record to be processed.")
    new_record_df = pd.DataFrame(crypto_df.loc[['c']]).drop(columns=['info'])

    # Set `datetime` column as datetime object
    new_record_df['datetime'] = pd.to_datetime(new_record_df['datetime'])
    #print(new_record_df)

    # Return the DataFrame object
    return new_record_df


def generate_signal(df):
    """Generates trading signals for a given dataset.

    This function calculates trading signals and appends them to the input
    DataFrame as additional columns.

    Args:
        df (obj): A Pandas DataFrame with historical and current prices.

    Returns: A Pandas DataFrame updated with generated trading signals.
    """
    database_connector = sqlite3.connect("mini_trader.sqlite")

    # Query data from sqlite to check if data exists
    print(f"{datetime.datetime.now()} [INFO] ----Entering generate_signal() function")
    print(f"{datetime.datetime.now()} [INFO] Querying data from sqlite")

    # Try to query the sqlite table, if it errors the table doesn't exist and the stacktrace is printed
    try:
        sqlite_data = pd.read_sql("select * from data", database_connector)
    except Exception as e:
        print(e)
        print(f"{datetime.datetime.now()} [WARNING] Data does not exist from sqlite")
        return

    # Set short and long window durations
    short_window = 10
    long_window = 20

    # If the sqlite data is empty, return early
    if sqlite_data.empty:
        print(f"{datetime.datetime.now()} [WARNING] Data does not exist from sqlite")
        return
    # Else if the sqlite data is less than the number of periods specified by the short window, return early
    elif len(sqlite_data) < short_window:
        print(f"{datetime.datetime.now()} [WARNING] Only {len(sqlite_data)} records returned, not enough data to generate a signal")
        return
    # Else sqlite data is returned and has sufficient data, generate signals
    else:
        print(f"{datetime.datetime.now()} [INFO] Displaying tail (most recent) of queried data from sqlite as Pandas DataFrame. Total records returned is {len(sqlite_data)}")
        print(sqlite_data.tail())

        # Grab just the `date` and `close` from the IEX dataset
        signals_df = sqlite_data.loc[:, ['datetime', 'close']]

        # Set the `date` column as the index and conver the date string to a datetime object
        signals_df.set_index(pd.to_datetime(signals_df['datetime']), inplace=True)

        # Drop the now extraneous `date` column
        signals_df.drop(columns=['datetime'], inplace=True)

        # Generate the short and long moving averages (50 and 100 days, respectively)
        signals_df['SMA10'] = signals_df['close'].rolling(window=10).mean()
        signals_df['SMA20'] = signals_df['close'].rolling(window=20).mean()
        signals_df['Signal'] = 0.0

        # Generate the trading signal 0 or 1,
        # where 0 is when the SMA50 is under the SMA100, and
        # where 1 is when the SMA50 is higher (or crosses over) the SMA100
        signals_df['Signal'][short_window:] = np.where(signals_df['SMA10'][short_window:] > signals_df['SMA20'][short_window:], 1.0, 0.0)

        # Calculate the points in time at which a position should be taken, 1 or -1
        signals_df['Entry/Exit'] = signals_df['Signal'].diff()

        # Display tail of signals DataFrame
        # print(signals_df.tail())

        return signals_df

def execute_backtest(signals_df):
    """Executes a backtest of a trading strategy.

    This function contains all of the logic required for performing a backtest.

    Args:
        signals_df (obj): A Pandas DataFrame of prices and trading signals.

    Returns: An updated Pandas DataFrame with backtested results.
    """
    print(f"{datetime.datetime.now()} [INFO] ----Entering execute_backtest() function")

    # Set initial capital
    initial_capital = 100000

    # Initialize share size variable
    share_size = 0

    # Calculate the possible share size
    # If backtesting for the first time, calculate the max possible share size as the initial 100000 divided by the current price, rounded down to the nearest integer
    # Else, backtesting has already been done, therefore calculate the max possible share size as the current portfolio cash divided by the current price, rounded down to the nearest integer
    if 'Portfolio Cash' not in signals_df.columns:
        print(f"{datetime.datetime.now()} [INFO] Backtesting has never been performed before, setting share size as 100000 divided by latest share price.")
        share_size = math.floor(initial_capital / signals_df['close'][-1])
    else:
        share_size = math.floor(signals_df['Portfolio Cash'][-1] / signals_df['close'][-1])

    # Take a share position where the dual moving average crossover is 1 (SMA50 is greater than SMA100)
    signals_df['Position'] = share_size * signals_df['Signal']

    # Find the points in time where a share position is bought or sold
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
    # print(signals_df)

    return signals_df

def execute_trade_strategy(signals_df, account):
    """Makes a buy/sell/hold decision.

    This function contains all of the logic required for a trading strategy. A
    final buy/sell/hold decision will be added as a column to the input df.

    Note: ML models will need to be initialized in this function and all
    preprocessing steps handled here.

    Args:
        df (obj): A Pandas DataFrame of prices and trading signals.

    Returns: An updated Pandas DataFrame with a buy/sell/hold decision.
    """
    print(f"{datetime.datetime.now()} [INFO] ----Entering execute_trade_strategy() function")

    # Print the latest 20 records of signal data
    print(f"{datetime.datetime.now()} [INFO] Printing latest 20 records of signal data")
    print(signals_df.tail(20))

    # If the value of the `Entry/Exit` column of the signal data is 0, then HOLD
    # Else if the value of the `Entry/Exit` column of the signal data is 1, then BUY
    # Else if the value of the `Entry/Exit` column of the signal data is -1, then SELL
    if signals_df['Entry/Exit'][-1] == 0.0:
        print(f"{datetime.datetime.now()} [INFO] Signal metrics indicate a HOLD")
        return account
    elif signals_df['Entry/Exit'][-1] == 1.0:
        print(f"{datetime.datetime.now()} [INFO] Signal metrics indicate a BUY")

        # Calculate number of shares that can be bought
        num_shares_can_buy = round(account['cash_balance'] / signals_df['close'][-1], 0)
        print(f"{datetime.datetime.now()} [INFO] Purchasing {num_shares_can_buy} shares at a current market price of {signals_df['close'][-1]}")

        # Set new account values after placing a BUY
        account['cash_balance'] = signals_df['Portfolio Cash'][-1]
        account['portfolio_holding'] = signals_df['Portfolio Holdings'][-1]
        account['total_portfolio_value'] = signals_df['Portfolio Total'][-1]
        account['buy_counter'] += 1

        return account
    elif signals_df['Entry/Exit'][-1] == -1.0:
        print(f"{datetime.datetime.now()} [INFO] Signal metrics indicate a SELL")

        # Set new account values after placing a SELL
        account['cash_balance'] = signals_df['Portfolio Cash'][-1]
        account['portfolio_holding'] = signals_df['Portfolio Holdings'][-1]
        account['total_portfolio_value'] = signals_df['Portfolio Total'][-1]
        account['sell_counter'] += 1

        return account

def save_data(account, data, signals):
    """Save the data to a database."""

    # Create a connection to sqlite
    database_connector = sqlite3.connect("mini_trader.sqlite")

    # Set variables from account dictionary
    cash_balance = account.get("cash_balance")
    portfolio_holding = account.get("portfolio_holding")
    total_portfolio_value = account.get("total_portfolio_value")
    buy_counter = account.get("buy_counter")
    sell_counter = account.get("sell_counter")

    # Set DataFrame from variables of account dictionary
    account_df = pd.DataFrame({
        "cash_balance": [cash_balance],
        "portfolio_holding": [portfolio_holding],
        "total_portfolio_value": [total_portfolio_value],
        "buy_counter": [buy_counter],
        "sell_counter": [sell_counter]
        })

    # Use the `to_sql` function to export data from DataFrame to sqlite connection
    account_df.to_sql("account", database_connector, if_exists='replace', index=False)
    data.to_sql("data", database_connector, if_exists='replace', index=True)

    # If signals_df is None, then just return the database connector after exporting the prior datasets
    # Else, signals_df contains data, therefore export the signal data to sqlite as well
    if signals is None:
        return database_connector
    else:
        signals.to_sql("signals", database_connector, if_exists='replace', index=False)
        return database_connector

def evaluate_metrics(signals_df):
    """Evaluates the up-to-date signal data to produce evaluation metrics.

    Args:
        signals_df (obj): A DataFrame containing signal data

    Returns: None
    """
    print(f"{datetime.datetime.now()} [INFO] ----Entering evaluate_metrics() function")

    # If there is so signal data, return early
    # Else, evaluate the metrics from the signal data and
    # create and return a DataFrame containing per trade metrics
    if signals_df is None:
        return
    else:
        # Create empty DataFrame and set the column names
        trade_evaluation_df = pd.DataFrame(columns=['Stock',
                                                'Entry Date',
                                                'Exit Date',
                                                'Shares',
                                                'Entry Share Price',
                                                'Exit Share Price',
                                                'Entry Portfolio Holding',
                                                'Exit Portfolio Holding',
                                                'Profit/Loss'])

        # Initialize variables
        entry_date = ''
        exit_date = ''
        entry_portfolio_holding = 0
        exit_portfolio_holding = 0
        share_size = 0
        entry_share_price = 0
        exit_share_price = 0

        # Loop through the rows of the signals_df
        # If the `Entry/Exit` column indicates 1, pull the relevant data from the row for entry trade metrics
        # Else if `Entry/Exit` column indicates -1, pull the relevant data from the row for exit trade metrics
        for index, row in signals_df.iterrows():
            if row['Entry/Exit'] == 1:
                # Set variables from entry trade row data
                entry_date = index
                entry_portfolio_holding = row['Portfolio Holdings']
                share_size = row['Entry/Exit Position']
                entry_share_price = row['close']

            elif row['Entry/Exit'] == -1:
                # Set variables from exit trade row data
                exit_date = index
                exit_portfolio_holding = abs(row['close'] * row['Entry/Exit Position'])
                exit_share_price = row['close']

                # Calculate profit/loss from difference in entry vs. exit portfolio holding
                profit_loss = exit_portfolio_holding - entry_portfolio_holding

                # Append the variables as a new entry-exit pair row in the trade_evaluation_df
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

        return trade_evaluation_df


def calculate_portfolio_evaluation_metrics(signals_df):
    # Initialize index and columns
    metrics= ['Annual Return', 'Cumulative Returns', 'Annual Volatility', 'Sharpe Ratio', 'Sortino Ratio']
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

    return portfolio_evaluation_df

def update_dashboard(database_connector, dashboard, signals_df, trade_evaluation_df):
    """Updates the dashboard with the latest data and account balances.

    Args:
        database_connector (obj): A database connector
        dashboard (obj): A Panel Dashboard
        signals_df (obj): A DataFrame containing tested signal data
        trade_evaluation_df (obj): A DataFrame containing per trade metrics

    Returns: None
    """
    print(f"{datetime.datetime.now()} [INFO] ----Entering update_dashboard() function")

    # Read the data for the dashboard
    account = pd.read_sql("select * from account", database_connector)
    #df = pd.read_sql("select * from data", database_connector)
    #signals = pd.read_sql("select * from signals", database_connector)

    # Return early if the DataFrames are empty
    if account.empty:
        return

    # Update the account balance
    cash_balance = account.cash_balance.iloc[-1]
    portfolio_holding = account.portfolio_holding.iloc[-1]
    total_portfolio_value = account.total_portfolio_value.iloc[-1]
    buy_counter = account.buy_counter.iloc[-1]
    sell_counter = account.sell_counter.iloc[-1]

    # Set the account information widgets
    account_balance = pn.widgets.StaticText(name="Cash Balance", value=cash_balance)
    holding_value = pn.widgets.StaticText(name="Portfolio Holding", value=portfolio_holding)
    total_portfolio_value = pn.widgets.StaticText(name="Total Portfolio Value", value=total_portfolio_value)
    num_entry_trades = pn.widgets.StaticText(name="Number of Entry Trades", value=buy_counter)
    num_exit_trades = pn.widgets.StaticText(name="Number of Exit Trades", value=sell_counter)

    # Initialize the dashboard columns
    summary_column = pn.Column()

    # Build the plots
    if signals_df is None:
        return
    else:
        #################SUMMARY TAB#######################
        # Not a very elegant filtering solution, may look into this later
        filtered_df = signals_df[['close', 'SMA10', 'SMA20']]

        # Set datetime index as a separate column
        filtered_df['datetime'] = signals_df.index
        filtered_df['datetime'] = pd.to_datetime(filtered_df['datetime'])

        ## DEPRECATED
        # Set formatted datetime string
        filtered_df['formatted_datetime'] = filtered_df['datetime'].dt.strftime('%d/%m/%y %H:%M:%S')

        # Create hvplot price chart of BTC/USD
        price_chart = filtered_df.hvplot.line(x='datetime', y=['close', 'SMA10', 'SMA20'], value_label='Price', width=1000, height=400, rot=90)

        # Create rows for each account information widget
        account_balance_row = account_balance
        holding_value_row = holding_value
        total_portfolio_value_row = total_portfolio_value
        #combined_row = price_chart
        num_entry_trades_row = num_entry_trades
        num_exit_trades_row = num_exit_trades

        # Create trade evaluation table
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

        # Create filtered cumulative returns DataFrame
        cumulative_ret_df = signals_df[['Portfolio Cumulative Returns']]

        # Set datetime index as a separate column
        cumulative_ret_df['datetime'] = signals_df.index
        cumulative_ret_df['datetime'] = pd.to_datetime(filtered_df['datetime'])

        # Create cumulative returns plot
        cumulative_ret_plot = cumulative_ret_df.hvplot.line(x='datetime', y=['Portfolio Cumulative Returns'], value_label='Total Portfolio Value', width=600, height=250, rot=90)

        # Set the last row
        #last_row = pn.Row(trade_evaluation_table, cumulative_ret_plot)

        # Create portfolio summary table
        portfolio_evaluation_df = calculate_portfolio_evaluation_metrics(signals_df)
        portfolio_evaluation_df.reset_index()

        # Create the hvplot table
        portfolio_evaluation_table = portfolio_evaluation_df.hvplot.table(columns=['index', 'Backtest'], width=300, height=400)

        ###########TRANSACTION TAB#################
        entry = signals_df[signals_df['Entry/Exit'] == -1.0]['Portfolio Total'].hvplot.scatter(line_color='green')
        exit = signals_df[signals_df['Entry/Exit'] == 1.0]['Portfolio Total'].hvplot.scatter(line_color='red')
        port_value = signals_df[['Portfolio Total']].hvplot.line(line_color='lightgray')

        entry_exit_plot = port_value * entry * exit

        # Set the combined row and last row
        combined_row = pn.Row(price_chart, entry_exit_plot)
        last_row = pn.Row(trade_evaluation_table, cumulative_ret_plot, portfolio_evaluation_table)

         # Set the row to the summary column
        summary_column = pn.Column(
            account_balance_row,
            holding_value_row,
            total_portfolio_value_row,
            combined_row,
            num_entry_trades_row,
            num_exit_trades_row,
            last_row
        )

    tabs = pn.Tabs(
            ("Summary", summary_column)
        )

    dashboard[0] = tabs
    return

async def main(account, api_data_df, signals_df, trade_evaluation_df, dashboard):

    # Create an event loop
    loop = asyncio.get_event_loop()

    # Set a continuous loop (never ending)
    while True:

        # Fetch data from API and wait asyncronously for the new record
        new_record_df = await loop.run_in_executor(None, fetch_data)

        # If the DataFrame containing API data is empty, then perform a `copy` function of the new record DataFrame to copy the structure (columns)
        # Else, the DataFrame already contains API data, therefore append the new record data
        if api_data_df.empty:
            api_data_df = new_record_df.copy()
        else:
            api_data_df = api_data_df.append(new_record_df, ignore_index=True)

        # Generate signals and entry/exit trading point in time from the API data
        signals_df = generate_signal(api_data_df)

        # If the signals_df is null, then skip the trade execution as there was no data/not enough signal data to make a decision
        # Else, the signals_df contains enough signal data and thus proceeds to running backtest calculation and executing the trading strategy
        if signals_df is None:
            print(f"{datetime.datetime.now()} [WARNING] Not enough signal data to make a decision, skipping backtesting and execution of trade strategy.")
        else:
            print(f"{datetime.datetime.now()} [INFO] There is enough signal data to make a decision, running backtesting and executing trade strategy.")

            # Run the backtest and append the calculated columns to the signals_df and return the DataFrame
            signals_df = execute_backtest(signals_df)

            # Execute the trade strategy and update the account dictionary
            account = await loop.run_in_executor(None, execute_trade_strategy, signals_df, account)

            # Evaluate metrics from signals_df and return a DataFrame containing per trade metrics
            trade_evaluation_df = evaluate_metrics(signals_df)

        # Save the current data
        database_connector = save_data(account, api_data_df, signals_df)

        # Update the Panel dashboard
        update_dashboard(database_connector, dashboard, signals_df, trade_evaluation_df)

        # Sleep for 1 second and begin the next loop
        await asyncio.sleep(1)

# Kraken API credentials
kraken = ccxt.kraken({
    'apiKey': 'mvCmUR7Ji9iLjLDhe8OZvdQ0nJPp7i+BCszr8ENlu1NxeEeduEzP99Co',
    'secret': 'bBFr4we3uc+nl/1d3OBvkoK3Zz2/c3QaGch7lBqe8hPYOynew3htWxrTSHEJALG/ej0EkzJ8at3zyoRIjHwaxA==',
})

# Initialize global variables to contain data and spin up the dashboard
account, api_data_df, signals_df, trade_evaluation_df, dashboard = initialize(100000)
dashboard.servable()

# Create an event loop and run it until completion (in this case we have it in a constant loop)
loop = asyncio.get_event_loop()
loop.run_until_complete(main(account, api_data_df, signals_df, trade_evaluation_df, dashboard))
