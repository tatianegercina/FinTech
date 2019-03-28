# -*- coding: utf-8 -*-
import os
import requests
import pandas as pd

import quandl

def get_coin_prices():
    currency_base = "EUR"
    coin = "BTC"
    fixer_url = 'http://data.fixer.io/api/latest'
    coinbase_url = f'https://api.coinbase.com/v2/prices/spot?currency={currency_base}'

    fixer_params = {
        "access_key": os.getenv("fixer_api"),
        "symbols": ",".join(["USD", "AUD", "CAD", "GBP", "CHF"])
    }
    r = requests.get(fixer_url, params=fixer_params)
    exchange_rates = r.json()


    coin_params = {
        "symbols": f"{currency_base}"
    }
    r = requests.get(coinbase_url, params=coin_params)
    coin_rates = r.json()
    coin_per_eur = float(coin_rates["data"]["amount"])


    # buy_url = f"https://api.coinbase.com/v2/prices/{coin}-{currency_base}/buy"
    # buy_prices = requests.get(buy_url).json()

    # sell_url = f"https://api.coinbase.com/v2/prices/{coin}-{currency_base}/sell"
    # sell_prices = requests.get(sell_url).json()

    currency_countries = {
        "USD": "United States",
        "AUD": "Australia",
        "CAD": "Canada",
        "JPY": "Japan",
        "GBP": "United Kingdom",
        "CHF": "Switzerland",
    }
    def calc_coin_exchange():
        prices = []
        countries = []
        for currency, rate in forex["rates"].items():
            countries.append(currency_countries[currency])
            prices.append(rate * coin_per_eur)
        return pd.DataFrame({
            "country": countries,
            "price": prices
        })
    return calc_coin_exchange()

def get_stocks():
    df = quandl.get("BITFINEX/BTCUSD")
    return df.reset_index()
