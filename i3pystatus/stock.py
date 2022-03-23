#!/usr/bin/env python3
import requests
from os import getenv
from binance.client import Client

API_KEY = getenv('BINANCE_API_KEY')
API_SECRET = getenv('BINANCE_API_SECRET')
CLIENT = Client(API_KEY, API_SECRET)


def get_current_price(symbol):
    resp = CLIENT.get_symbol_ticker(symbol=symbol)
    return resp.get('price', '0.0').split('.', maxsplit=1)[0]


def get_exchange_rate(q="NZD_CNY"):
    url = f"https://free.currconv.com/api/v7/convert?q={q}&compact=ultra&apiKey=10ad16149788c3c11c6b"
    resp = requests.get(url)
    data = resp.json()  # {"NZD_CNY":4.340477}
    rate_str = data.get(q, '0')
    rate = float(rate_str)
    return round(rate, 2)


def main():
    kv = {
        'btc': get_current_price('BTCUSDT'),
        'eth': get_current_price('ETHUSDT'),
        #  'nzd': get_exchange_rate(),
    }
    print('|'.join([f'{k}:{v}' for k, v in kv.items()]))


if __name__ == "__main__":
    main()

