# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.http import JsonResponse
from django.db.models import Max
from django.db.models import Min
from django.db.models import count
from django.db.models import Sum
import datetime
import time

from ltc.models import Record

# 数据库操作
def get_ltc_price(request):
    date = datetime.date.today()
    today = time.mktime(date.timetuple()) + 16 * 60 * 60
    objects = Record.objects.filter(timestamp__gte = today).order_by('timestamp')
    arg = objects.aggregate(Max('price'),Min('price'),Count('entry'))
    count = 20
    if arg["entry__count"] < count:
        count = arg["entry__count"]

    latest_objects = objects[:count]
    sum = latest_objects.aggregate(Sum('count'))
    active = count / sum
    record = objects.last()
    start = objects.first()
    if (record):
        record = record.dumpJSON()
        json = {"latest" : record}
        json["high"] = arg['price__max']
        json["low"] = arg['price__min']
        # json["today"] = today
        json["open"] = start.price
        json["active"] = active
        return JsonResponse(json)
    else:
        return HttpResponse('No Record')
