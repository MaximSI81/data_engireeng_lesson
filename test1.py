import time

import requests
import json
import datetime


curr = 'RUB,GBP,EUR'
start_date = datetime.date(year=2015, month=7, day=10)
end_date = datetime.date(year=2024, month=7, day=10)

api_key = 'd570f2a79f438392960a9932dfcfeb07'
for i in range(1,10):
    link = (f'http://api.currencylayer.com/change?access_key={api_key}'
            f'&currencies={curr}&start_date={start_date + datetime.timedelta(days=i)}'
            f'&end_date={end_date + datetime.timedelta(days=i)}')
    time.sleep(1)

    r = requests.get(url=link)
    print(r.json().get('quotes').get('USDRUB').get('start_rate'))
    print(r.json().get('quotes').get('USDRUB').get('end_rate'))