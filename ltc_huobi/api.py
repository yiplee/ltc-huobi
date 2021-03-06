# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.http import JsonResponse
from django.db.models import Max
from django.db.models import Min
from django.db.models import Count
from django.db.models import Sum
import datetime

from ltc.models import Record

# 数据库操作
def get_ltc_price(request):
    offset = datetime.timedelta(hours=8)
    tz  = datetime.timezone(offset,'Asia/Shanghai')
    now = datetime.datetime.now().astimezone(tz)
    today = datetime.datetime(now.year,now.month,now.day,tzinfo=tz).timestamp()
    objects = Record.objects.filter(timestamp__gte = today).order_by('timestamp')
    arg = objects.aggregate(Max('price'),Min('price'))
    count = 20
    count_sum = 0

    latest_objects = objects.reverse()[:count]
    for item in latest_objects:
        count_sum += item.count

    active = count / count_sum
    record = objects.last()
    start = objects.first()
    if (record):
        record_json = record.dunp_json()
        json = {"latest" : record_json}
        json["high"] = arg['price__max']
        json["low"] = arg['price__min']
        json["open"] = start.price
        json["active"] = active
        return JsonResponse(json)
    else:
        return HttpResponse('No Record')
