# -*- coding: utf-8 -*-

import http.client
from ltc.models import Record
import json
import os

def get_current_price():
    conn = http.client.HTTPSConnection('api.huobi.com')
    conn.request('GET','/staticmarket/ticker_ltc_json.js')
    r = conn.getResponse()
    if r.status == 200 :
        data = r.read()
        string = data.decode('utf8').replace("'", '"')
        json_data = json.loads(string)
        json = json.dumps(json_data,indent=4, sort_keys=True)

        price = json['ticker']['last']
        date = json['time']

        recod = Record.create(price,date)
        record.save()


if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ltc_huobi.settings")
    get_current_price()
