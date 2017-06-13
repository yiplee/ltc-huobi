# -*- coding: utf-8 -*-

import http.client
from ltc.models import Record
import json
import time

while True:
    conn = http.client.HTTPSConnection('api.huobi.com')
    body = {}
    headers = {'Content-type': 'application/json', 'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0'}
    conn.request('GET','/staticmarket/ticker_ltc_json.js', json.dumps(body),headers)
    r = conn.getresponse()
    if r.status == 200 :
        data = r.read()
        string = data.decode('utf8').replace("'", '"')
        json_data = json.loads(string)
        ticker = json_data['ticker']
        price = ticker['last']
        date = int(json_data['time'])
        try:
            record = Record.objects.get(timestamp=date)
            record.count = record.count + 1
        except Record.DoesNotExist:
            record = Record.create(price,date)
    conn.close()
    time.sleep(5)
