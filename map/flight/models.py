from django.db import models

# Create your models here.
class dataFlight(models.Model):
    hex = models.CharField(max_length=255)
    squawk = models.CharField(max_length=255)
    flight = models.CharField(max_length=255)
    lat  = models.FloatField()
    lon = models.FloatField()
    validposition = models.IntegerField()
    altitude = models.IntegerField()
    vert_rate = models.IntegerField()
    track = models.IntegerField()
    validtrack = models.IntegerField()
    speed = models.IntegerField()
    messages = models.IntegerField()
    seen = models.IntegerField()

    def __str__(self):
        return f'{self.flight} valid : {self.validposition}'