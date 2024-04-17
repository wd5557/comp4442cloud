from django.db import models


class DriveData(models.Model):
    driverID = models.CharField(max_length=100)
    carPlateNumber = models.CharField(max_length=100)
    unix_Time = models.BigIntegerField()
    speed = models.FloatField()
    isOverspeed = models.IntegerField()

    class Meta:
        db_table = 'drivedata'

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
