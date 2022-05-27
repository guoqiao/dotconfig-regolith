#!/usr/bin/env python3
import requests
from os import getenv
from binance.client import Client

from dotenv import load_dotenv
load_dotenv()

API_KEY = getenv('BINANCE_API_KEY')
API_SECRET = getenv('BINANCE_API_SECRET')
CLIENT = Client(API_KEY, API_SECRET)


def get_price(coin, base='USDT'):
    symbol = coin.upper() + base
    resp = CLIENT.get_symbol_ticker(symbol=symbol)
    return resp.get('price', '0.0').split('.', maxsplit=1)[0]


def get_prices(coins):
    return {coin: get_price(coin) for coin in coins}


def get_exchange_rate(q="NZD_CNY"):
    url = f"https://free.currconv.com/api/v7/convert?q={q}&compact=ultra&apiKey=10ad16149788c3c11c6b"
    resp = requests.get(url)
    data = resp.json()  # {"NZD_CNY":4.340477}
    rate_str = data.get(q, '0')
    rate = float(rate_str)
    return round(rate, 2)


def main():
    prices = get_prices(['BTC', 'ETH'])
    print('|'.join([f'{coin}:{price}' for coin, price in prices.items()]))


if __name__ == "__main__":
    main()
