from django.db import models

# Create your models here.
from django.db import models
import datetime

class Record(models.Model):
    price      = models.DecimalField('the price of ltc',max_digits=6,decimal_places=2)
    timestamp  = models.IntegerField('date of record')

    class Meta:
        get_latest_by = 'timestamp'

    def __str__(self):
        tz  = datetime.timezone('Asia/Shanghai')
        date = datetime.datetime.fromtimestamp(self.timestamp,tz)
        return str(date) + '\t' + str(self.price)

    @classmethod
    def create(cls, price, timestamp):
        record = cls(price = price,timestamp = timestamp)
        record.save()
        return record

    def dumpJSON(self):
        json = {}
        json['price'] = self.price
        json['timestamp']  = self.timestamp
        return json
