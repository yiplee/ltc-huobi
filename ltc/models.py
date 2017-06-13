from django.db import models

# Create your models here.
from django.db import models
import datetime

class Record(models.Model):
    price      = models.DecimalField('the price of ltc', max_digits=6, decimal_places=2)
    timestamp  = models.IntegerField('date of record', db_index=True)

    class Meta:
        get_latest_by = 'timestamp'

    def __str__(self):
        offset = datetime.timedelta(hours=8)
        tz  = datetime.timezone(offset,'Asia/Shanghai')
        date = datetime.datetime.fromtimestamp(self.timestamp)
        date = date.replace(tzinfo=datetime.timezone.utc).astimezone(tz=tz)
        return date.strftime('%y年%m月%d日 %H:%M:%S') + '\t\t' + str(self.price) + '元'

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
