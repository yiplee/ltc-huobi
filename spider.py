# -*- coding: utf-8 -*-

import requests
from ltc.models import Record
import json
import time

huobi_api = "http://api.huobi.com/staticmarket/ticker_ltc_json.js"
headers = {'Content-type': 'application/json', 'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0'}
session = requests.session()
while True:
    try:
        r = session.get(huobi_api,headers = headers, timeout = 2)
        if r.status_code == requests.codes.ok:
            json_data = r.json()
            ticker = json_data['ticker']
            price = ticker['last']
            date = int(json_data['time'])
            try:
                record = Record.objects.get(timestamp=date)
                record.count = record.count + 1
                record.save()
            except Record.DoesNotExist:
                record = Record.create(price,date)

            time.sleep(3)
        else:
            time.sleep(8)
    except requests.exceptions.Timeout:
        continue
    except requests.exceptions.RequestException:
        time.sleep(10)
