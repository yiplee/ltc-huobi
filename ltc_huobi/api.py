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

    date = datetime.date.today()
    today = time.mktime(date.timetuple()) + 16 * 60 * 60
    objects = Record.objects.filter(timestamp__gte = today)
    max_price = objects.aggregate(Max('price'))
    min_price = objects.aggregate(Min('price'))

    if (record):
        record = record.dumpJSON()
        json = {"record" : record}
        json.update(max_price)
        json.update(min_price)
        json["time"] = today
        return JsonResponse(json)
    else:
        return HttpResponse('No Record')
