import requests
import pandas as pd
import json


class CryptoCurrencies():
    def get_crypto_price(self, cur_symbol, exchange, start_date = None):
        api_key = 'SVZ8DJAEA6ZJ6C51'
        api_url = f'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol={cur_symbol}&market={exchange}&apikey={api_key}'
        raw_df = requests.get(api_url).json()
        df = pd.DataFrame(raw_df['Time Series (Digital Currency Daily)']).T
        df = df.rename(columns = {'1a. open (USD)': 'open', '2a. high (USD)': 'high', '3a. low (USD)': 'low', '4a. close (USD)': 'close', '5. volume': 'volume'})
        for i in df.columns:
            df[i] = df[i].astype(float)
        df.index = pd.to_datetime(df.index)
        df = df.iloc[::-1].drop(['1b. open (USD)', '2b. high (USD)', '3b. low (USD)', '4b. close (USD)', '6. market cap (USD)'], axis = 1)
        if start_date:
            df = df[df.index >= start_date]
        df = df.to_json(orient='index', date_format='iso')
        parsed = json.loads(df)
        data = json.dumps(parsed, indent=4)
        return data