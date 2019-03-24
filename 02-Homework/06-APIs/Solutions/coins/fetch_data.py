# -*- coding: utf-8 -*-
import os
import requests
import pandas as pd

import quandl

stock_news_api = os.getenv("stock_news_api")
news_api = os.getenv("news_api")

def get_stock_news(ticker="AAPL"):
    # stock_news_url = f"https://stocknewsapi.com/api/v1?tickers={ticker}&type=article&items=5&fallback=true&token={stock_news_api}"
    stock_news_url = f"https://newsapi.org/v2/top-headlines?sources=bloomberg&apiKey={news_api}"
    return requests.get(stock_news_url).json()

def get_stock(ticker="AAPL"):
    df = quandl.get(f"WIKI/{ticker}")
    return df.reset_index()
