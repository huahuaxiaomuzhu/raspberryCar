from django.db import models

# Create your models here.
from django.db import models
import time


class AccInfo(models.Model):  # 加速度传感器的信息
    x_acc = models.FloatField(max_length=20)
    y_acc = models.FloatField(max_length=20)
    z_acc = models.FloatField(max_length=20)
    record_time = models.TimeField(default=time.time())
