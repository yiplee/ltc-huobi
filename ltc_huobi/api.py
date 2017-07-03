# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.http import JsonResponse
from django.db.models import Max
from django.db.models import Min
from django.db.models import Count
from django.db.models import Sum
import datetime
import time

from ltc.models import Record

# 数据库操作
def get_ltc_price(request):
    date = datetime.date.today()
    today = time.mktime(date.timetuple()) + 16 * 60 * 60
    objects = Record.objects.filter(timestamp__gte = today).order_by('timestamp')
    arg = objects.aggregate(Max('price'),Min('price'))
    count = 20
    if objects.count() < count:
        count = arg.objects()

    latest_objects = objects[:count]
    count_sum = latest_objects.aggregate(Sum('count'))['count__sum']
    active = count / count_sum
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
        json["sum"] = count_sum
        return JsonResponse(json)
    else:
        return HttpResponse('No Record')
