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
    record = Record.objects.latest()

    today = time.mktime(datetime.date.today().timetuple())
    objects = Record.objects.filter(timestamp__gte = today)
    max_price = objects.aggregate(Max('price'))
    min_price = objects.aggregate(Min('price'))

    if (record):
        record = record.dumpJSON()
        json = {"record" : record}
        json["max"] = max_price
        json["min"] = min_price
        return JsonResponse(json)
    else:
        return HttpResponse('No Record')
