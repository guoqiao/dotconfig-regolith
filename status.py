#!/usr/bin/env python3
import requests
import yfinance as yf

def get_exchange_rates(base='NZD', currencies=['CNY', 'AUD', 'USD']):
    resp = requests.get(f'https://api.exchangeratesapi.io/latest?base={base}')
    result = f'1{base}'
    if resp.ok:
        rates = resp.json()['rates']
        for currency in currencies:
            result += '={:.2f}{}'.format(rates[currency], currency)
    return result

items = [get_exchange_rates()]

for ticker in yf.Tickers('AIR.NZ ANZ.NZ ^NZ50 BTC-USD').tickers:
    info = ticker.info
    price = info.get('bid') or info.get('ask') or info.get('open')
    items.append('{}={:.2f}'.format(info['symbol'], price))

print(*items)
