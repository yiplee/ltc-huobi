# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.http import JsonResponse
from django.db.models import Max
from django.db.models import Min
import datetime
import time

from ltc.models import Record

# 数据库操作
def get_ltc_price(request):
    date = datetime.date.today()
    today = time.mktime(date.timetuple()) + 16 * 60 * 60
    objects = Record.objects.filter(timestamp__gte = today)
    arg = objects.aggregate(Max('price'),Min('price'))

    record = objects.latest()
    start = objects.earliest()
    if (record):
        record = record.dumpJSON()
        json = {"record" : record}
        json["max"] = arg['price__max']
        json["min"] = arg['price__min']
        # json["today"] = today
        json["start"] = start.price
        return JsonResponse(json)
    else:
        return HttpResponse('No Record')
