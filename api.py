# -*- coding: utf-8 -*-

from django.http import HttpResponse

from ltc.models import Record

# 数据库操作
def get_ltc_price(request):
    record = Record.objects.latest()

    if (record):
        return HttpResponse(record.dumpJSON())
    else:
        return HttpResponse('No Record')
