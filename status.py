#!/usr/bin/env python3
import requests
import yfinance as yf

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
        print(ticker)
        print(dir(ticker))
        info = ticker.get_info()
        price = info.get('bid') or info.get('ask') or info.get('open')
        return '{}={:.2f}'.format(info['symbol'], price)

    return map(foreach, yf.Tickers(tickers).tickers)


def get_sina_ticker(ticker='s_sh000001'):
    text = get_url(f'http://hq.sinajs.cn/list={ticker}')
    if text:
        # var hq_str_s_sh000001="上证指数,2920.8968,-22.8557,-0.78,2337229,28902326";
        left = text.index('"')
        right = text.rindex('"')
        assert right - left > 10
        fields = text[left+1:right]
        name, price, _, percent, _, _ = fields.split(',')
        return '{}:{}({}%)'.format(name, int(float(price)), percent)


print(
    get_exchange_rates(),
    get_sina_ticker(),
    #  *get_yfinance_tickers(),
)
