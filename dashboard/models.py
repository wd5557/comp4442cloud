from django.db import models
from django.db import models


class Duxu1000009(models.Model):
    driverID = models.CharField(max_length=100)
    carPlateNumber = models.CharField(max_length=100)
    unix_Time = models.BigIntegerField()
    speed = models.FloatField()
    isOverspeed = models.IntegerField()

    class Meta:
        db_table = 'duxu1000009'


class Hanhui1000002(models.Model):
    driverID = models.CharField(max_length=100)
    carPlateNumber = models.CharField(max_length=100)
    unix_Time = models.BigIntegerField()
    speed = models.FloatField()
    isOverspeed = models.IntegerField()

    class Meta:
        db_table = 'hanhui1000002'


class Haowei1000008(models.Model):
    driverID = models.CharField(max_length=100)
    carPlateNumber = models.CharField(max_length=100)
    unix_Time = models.BigIntegerField()
    speed = models.FloatField()
    isOverspeed = models.IntegerField()

    class Meta:
        db_table = 'haowei1000008'


class Likun1000003(models.Model):
    driverID = models.CharField(max_length=100)
    carPlateNumber = models.CharField(max_length=100)
    unix_Time = models.BigIntegerField()
    speed = models.FloatField()
    isOverspeed = models.IntegerField()

    class Meta:
        db_table = 'likun1000003'


class Panxian1000005(models.Model):
    driverID = models.CharField(max_length=100)
    carPlateNumber = models.CharField(max_length=100)
    unix_Time = models.BigIntegerField()
    speed = models.FloatField()
    isOverspeed = models.IntegerField()

    class Meta:
        db_table = 'panxian1000005'


class Shenxian1000004(models.Model):
    driverID = models.CharField(max_length=100)
    carPlateNumber = models.CharField(max_length=100)
    unix_Time = models.BigIntegerField()
    speed = models.FloatField()
    isOverspeed = models.IntegerField()

    class Meta:
        db_table = 'shenxian1000004'


class Xiexiao1000001(models.Model):
    driverID = models.CharField(max_length=100)
    carPlateNumber = models.CharField(max_length=100)
    unix_Time = models.BigIntegerField()
    speed = models.FloatField()
    isOverspeed = models.IntegerField()

    class Meta:
        db_table = 'xiexiao1000001'


class Xiezhi1000006(models.Model):
    driverID = models.CharField(max_length=100)
    carPlateNumber = models.CharField(max_length=100)
    unix_Time = models.BigIntegerField()
    speed = models.FloatField()
    isOverspeed = models.IntegerField()

    class Meta:
        db_table = 'xiezhi1000006'


class Zengpeng1000000(models.Model):
    driverID = models.CharField(max_length=100)
    carPlateNumber = models.CharField(max_length=100)
    unix_Time = models.BigIntegerField()
    speed = models.FloatField()
    isOverspeed = models.IntegerField()

    class Meta:
        db_table = 'zengpeng1000000'


class Zengpeng1000000(models.Model):
    driverID = models.CharField(max_length=100)
    carPlateNumber = models.CharField(max_length=100)
    unix_Time = models.BigIntegerField()
    speed = models.FloatField()
    isOverspeed = models.IntegerField()

    class Meta:
        db_table = 'zengpeng1000000'


class Zouan1000007(models.Model):
    driverID = models.CharField(max_length=100)
    carPlateNumber = models.CharField(max_length=100)
    unix_Time = models.BigIntegerField()
    speed = models.FloatField()
    isOverspeed = models.IntegerField()

    class Meta:
        db_table = 'zouan1000007'


class Summary(models.Model):
    driverID = models.CharField(max_length=100)
    carPlateNumber = models.CharField(max_length=100)
    date = models.DateField()
    number_of_overspeed = models.IntegerField()
    total_overspeed = models.IntegerField()
    number_of_fatigueDriving = models.IntegerField()
    number_of_neutralSlide = models.IntegerField()
    total_neutralSlideTime = models.IntegerField()

    class Meta:
        db_table = 'summary'
