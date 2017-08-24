from django.db import models
import datetime

class Record(models.Model):
    price      = models.DecimalField('the price of ltc', max_digits=6, decimal_places=2)
    timestamp  = models.IntegerField('date of record', db_index=True)
    count      = models.IntegerField('fetch times', default = 0)

    class Meta:
        get_latest_by = 'timestamp'

    def __str__(self):
        offset = datetime.timedelta(hours=8)
        tz  = datetime.timezone(offset,'Asia/Shanghai')
        date = datetime.datetime.fromtimestamp(self.timestamp)
        date = date.replace(tzinfo=datetime.timezone.utc).astimezone(tz=tz)
        desc = date.strftime('%y年%m月%d日 %H:%M:%S') + '   ' + str(self.price)
        if self.count > 1:
            desc = desc + '   x' + str(self.count)
        return desc

    @classmethod
    def create(cls, price, timestamp):
        record = cls(price = price,timestamp = timestamp,count = 1)
        record.save()
        return record

    def dump_json(self):
        json = {}
        json['price'] = self.price
        json['timestamp']  = self.timestamp
        json['count'] = self.count
        return json
