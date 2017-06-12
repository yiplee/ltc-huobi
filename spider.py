# -*- coding: utf-8 -*-

import http.client
from ltc.models import Record
import json
import time

conn = http.client.HTTPSConnection('api.huobi.com')
conn.request('GET','/staticmarket/ticker_ltc_json.js')
while True:
    r = conn.getresponse()
    if r.status == 200 :
        data = r.read()
        string = data.decode('utf8').replace("'", '"')
        json_data = json.loads(string)
        print json_data
        ticker = json_data['ticker']
        price = ticker['last']
        date = int(json_data['time'])
        record = Record.create(price,date)
        record.save()

    time.sleep(5)
