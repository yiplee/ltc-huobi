# -*- coding: utf-8 -*-

import http.client
from ltc.models import Record
import json

def get_current_price():
    conn = http.client.HTTPSConnection('api.huobi.com')
    conn.request('GET','/staticmarket/ticker_ltc_json.js')
    r = conn.getresponse()
    if r.status == 200 :
        data = r.read()
        string = data.decode('utf8').replace("'", '"')
        json_data = json.loads(string)
        ticker = json_data['ticker']
        price = ticker['last']
        date = int(json_data['time'])
        # print(type(date))
        recod = Record.create(price,date)
        record.save()

if __name__ == '__main__':
    get_current_price()
