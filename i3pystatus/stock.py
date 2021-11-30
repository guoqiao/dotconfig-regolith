#!/usr/bin/env python3
from os import getenv
from binance.client import Client

API_KEY = getenv('BINANCE_API_KEY')
API_SECRET = getenv('BINANCE_API_SECRET')
CLIENT = Client(API_KEY, API_SECRET)


def get_current_price(symbol):
    resp = CLIENT.get_symbol_ticker(symbol=symbol)
    return resp.get('price')


def main():
    btc = get_current_price('BTCUSDT')
    eth = get_current_price('ETHUSDT')
    print('btc:{}|eth:{}'.format(btc, eth))


if __name__ == "__main__":
    main()

