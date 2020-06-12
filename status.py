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


def get_yfinance_tickers(tickers='AIR.NZ ANZ.NZ ^NZ50 BTC-USD'):

    def foreach(ticker):
        info = ticker.info
        price = info.get('bid') or info.get('ask') or info.get('open')
        return '{}={:.2f}'.format(info['symbol'], price)

    return map(foreach, yf.Tickers(tickers).tickers)


def get_sina_ticker(ticker='s_sh000001'):
    resp = requests.get(f'http://hq.sinajs.cn/list={ticker}')
    if resp.ok:
        # var hq_str_s_sh000001="上证指数,2920.8968,-22.8557,-0.78,2337229,28902326";
        text = resp.text
        left = text.index('"')
        right = text.rindex('"')
        assert right - left > 10
        data = text[left+1:right]
        name, price, _, percent, _, _ = data.split(',')
        return '{}:{}({}%)'.format(name, int(float(price)), percent)


print(
    get_exchange_rates(),
    get_sina_ticker(),
    *get_yfinance_tickers(),
)
