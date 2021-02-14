#!/usr/bin/env python3
from datetime import datetime
import pytz
import requests
import yfinance as yf


def check_hours(str_tz, start, end):
    now = datetime.now(tz=pytz.timezone(str_tz))
    return 0 <= now.weekday() <= 4 and start <= now.hour <= end


def get_url(url, fmt='text'):
    resp = requests.get(url)
    if fmt == 'json':
        return resp.json() if resp.ok else {}
    return resp.text if resp.ok else ''


def get_exchange_rates(base='NZD', currencies=['CNY', 'AUD', 'USD']):

    data = get_url(f'https://api.exchangeratesapi.io/latest?base={base}', fmt='json')

    if data:
        rates = data.get('rates', {})
        if rates:

            def foreach(currency):
                return '={:.2f}{}'.format(rates[currency], currency)

            return f'1{base}' + ''.join(map(foreach, currencies))

TICKERS = 'AIR.NZ ANZ.NZ ^NZ50 BTC-USD'
def get_yfinance_tickers(tickers=TICKERS):

    def foreach(ticker):
        info = ticker.get_info()
        price = info.get('bid') or info.get('ask') or info.get('open')
        return '{}={:.2f}'.format(info['symbol'], price)

    return map(foreach, yf.Tickers(tickers).tickers)


def get_sina_tickers(tickers='s_sh000001,s_sh000905,s_sz399975,s_sz002432'):
    items = []
    if check_hours('Asia/Shanghai', 9, 15):
        text = get_url(f'http://hq.sinajs.cn/list={tickers}')
        for line in text.splitlines():
            # var hq_str_s_sh000001="上证指数,2920.8968,-22.8557,-0.78,2337229,28902326";
            left = line.index('"')
            right = line.rindex('"')
            assert right - left > 10
            fields = line[left+1:right]
            name, price, _, percent, _, _ = fields.split(',')
            item = '{}:{}({}%)'.format(name, price, percent)
            items.append(item)
    return items


print(
    get_exchange_rates(),
    *get_sina_tickers(),
    *get_yfinance_tickers(),
)
