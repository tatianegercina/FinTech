#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'Solutions'))
	print(os.getcwd())
except:
	pass
#%% [markdown]
#  # Challenge
#
#  ## Identifying Outliers using Standard Deviation

#%%
# initial imports
import pandas as pd
import numpy as np
import random
import plotly.plotly as py
import plotly.graph_objs as go
from sqlalchemy import create_engine


#%%
# create a connection to the database
engine = create_engine("postgresql://postgres:postgres@localhost:5432/fraud_detection")


#%%
def find_outliers_sd(card_holder=1):
    query = (
        "SELECT t.date, t.amount, t.card "
        + "FROM transaction AS t "
        + "JOIN credit_card AS cc ON cc.card = t.card "
        + "JOIN card_holder AS ch ON ch.id = cc.id_card_holder "
        + "WHERE ch.id = "
        + str(card_holder)
        + " ORDER BY date"
    )
    data = pd.read_sql(query, engine)
    elements = data["amount"]
    mean = np.mean(elements, axis=0)
    sd = np.std(elements, axis=0)
    # 2 standard deviations are taken for analysis purposes
    low_transactions = [x for x in elements if (x < mean - 2 * sd)]
    high_transaction = [x for x in elements if (x > mean + 2 * sd)]
    final_list = low_transactions + high_transaction
    if len(final_list) > 0:
        query = (
            "SELECT t.date, t.amount, t.card "
            + "FROM transaction AS t "
            + "JOIN credit_card AS cc ON cc.card = t.card "
            + "JOIN card_holder AS ch ON ch.id = cc.id_card_holder "
            + "WHERE ch.id = "
            + str(card_holder)
            + " AND t.amount IN ("
            + str(final_list)[1:-1]
            + ") "
            + "ORDER BY date"
        )
        data = pd.read_sql(query, engine)
        return data
    else:
        return "There are no fraudulent transactions identified for this card holder"


#%%
# find anomalous transactions for 3 random card holders
for i in range(1, 4):
    card_holder = random.randint(1, 25)
    print("*" * 60)
    print(f"Looking for fraudulent transactions for card holder id {card_holder}")
    print(find_outliers_sd(card_holder))

#%% [markdown]
#  ## Identifying Outliers Using Interquartile Range

#%%
def find_outliers_iqr(card_holder=1):
    query = (
        "SELECT t.date, t.amount, t.card "
        + "FROM transaction AS t "
        + "JOIN credit_card AS cc ON cc.card = t.card "
        + "JOIN card_holder AS ch ON ch.id = cc.id_card_holder "
        + "WHERE ch.id = "
        + str(card_holder)
        + " ORDER BY date"
    )
    data = pd.read_sql(query, engine)
    # calculate interquartile range
    q25, q75 = np.percentile(data["amount"], 25), np.percentile(data["amount"], 75)
    iqr = q75 - q25
    # calculate the outlier cutoff
    cut_off = iqr * 1.5
    lower, upper = q25 - cut_off, q75 + cut_off
    # identify outliers
    outliers = [x for x in data["amount"] if x < lower or x > upper]
    if len(outliers) > 0:
        query = (
            "SELECT t.date, t.amount, t.card "
            + "FROM transaction AS t "
            + "JOIN credit_card AS cc ON cc.card = t.card "
            + "JOIN card_holder AS ch ON ch.id = cc.id_card_holder "
            + "WHERE ch.id = "
            + str(card_holder)
            + " AND t.amount IN ("
            + str(outliers)[1:-1]
            + ") "
            + "ORDER BY date"
        )
        data = pd.read_sql(query, engine)
        return data
    else:
        return "There are no fraudulent transactions identified for this card holder"


#%%
# find anomalous transactions for 3 random card holders
for i in range(1, 4):
    card_holder = random.randint(1, 25)
    print("*" * 60)
    print(f"Looking for fraudulent transactions for card holder id {card_holder}")
    print(find_outliers_iqr(card_holder))
