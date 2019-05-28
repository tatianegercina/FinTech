#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os

try:
    os.chdir(os.path.join(os.getcwd(), "Solutions"))
    print(os.getcwd())
except:
    pass
#%% [markdown]
# # Visual Data Analysis of Fraudulent Transactions
#
# Remember to create your Plotly API account and set your credentias as follows on the Plotly configuration file:
# ```python
# import plotly
# plotly.tools.set_credentials_file(username='youUserName', api_key='key123456')
# ```
#
# Reference: [Getting Started with Plotly for Python](https://plot.ly/python/getting-started/#initialization-for-online-plotting)

#%%
# initial imports
import pandas as pd
import calendar
import plotly.plotly as py
import plotly.graph_objs as go
from sqlalchemy import create_engine

get_ipython().run_line_magic("matplotlib", "inline")


#%%
# create a connection to the database
engine = create_engine("postgresql://postgres:postgres@localhost:5432/fraud_detection")

#%% [markdown]
# ## Data Analysis Questions 1
#
# Create a line plot showing a time series from the transactions along all the year for each card holder. In order to contrast the patters of both card holders, create a line plot containing both lines. What difference do you observe between the consumption patterns? Does the difference could be a fraudulent transaction? Explain your rationale.

#%%
# loading data for card holder 18 and 19
query = """
        SELECT ch.id AS cardholder, t.date AS hour, t.amount
        FROM transaction AS t
        JOIN credit_card AS cc ON cc.card = t.card
        JOIN card_holder AS ch ON ch.id = cc.id_card_holder
        WHERE ch.id in (18, 2)
        ORDER BY hour
        """
data = pd.read_sql(query, engine)


#%%
# get data for each card holder
data_18 = data[data["cardholder"] == 18]
data_2 = data[data["cardholder"] == 2]


#%%
# define traces
trace_18 = go.Scatter(x=data_18["hour"], y=data_18["amount"], name="Card holder 18")

trace_2 = go.Scatter(x=data_2["hour"], y=data_2["amount"], name="Card holder 2")


#%%
# plot for cardholder 18
data = [trace_18]

layout = go.Layout(title=go.layout.Title(text="Analysis of Card Holder 18"))

fig = go.Figure(data=data, layout=layout)
py.iplot(fig)


#%%
# plot for cardholder 2
data = [trace_2]

layout = go.Layout(title=go.layout.Title(text="Analysis of Card Holder 2"))

fig = go.Figure(data=data, layout=layout)
py.iplot(fig)


#%%
# plot for card holders 18 and 2
data = [trace_18, trace_2]

layout = go.Layout(title=go.layout.Title(text="Analysis of Card Holders 18 and 2"))

fig = go.Figure(data=data, layout=layout)
py.iplot(fig)

#%% [markdown]
# ### Sample Conclusions for Question 1
#
# After reviewing both plots it can be concluded that there are some fraudulent transactionon the card holder 18 records, since there are some anomalous amounts along the year.
#%% [markdown]
# ## Data Analysis Question 2
#
# Create a series of six box plots, one for each month, in order to identify how many outliers could be per month for card holder id `25`. By observing the consumption patters, do you see any anomalies? Write your own conclusions about your insights.

#%%
# loading data of daily transactions from jan to jun 2018 for card holder 25
query = """
        SELECT date_part('month', t.date) AS month, date_part('day', t.date) as day, t.amount
        FROM transaction AS t
        JOIN credit_card AS cc ON cc.card = t.card
        JOIN card_holder AS ch ON ch.id = cc.id_card_holder
        WHERE ch.id = 25 AND date_part('month', t.date) <= 6
        ORDER BY month, day
        """
data = pd.read_sql(query, engine)


#%%
# creating box plots

# empty array to store all box plots traces
box_plots = []

# loop to create a box plot trace for every month
for i in range(1, 7):
    box_plots.append(
        go.Box(y=data[data["month"] == i]["amount"], name=calendar.month_name[i])
    )

layout = go.Layout(
    title=go.layout.Title(
        text="Transactions from January to June 2018 for Card Holder 25"
    )
)

fig = go.Figure(data=box_plots, layout=layout)

py.iplot(fig)

#%% [markdown]
# ### Sample Conclusions for Question 2
#
# It can be concluded that card holder 25 has been hacked along all the first semester of 2018, exept for february where there are not anomalous transactions.
