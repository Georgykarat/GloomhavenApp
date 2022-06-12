from django.db import models
import datetime

# Create your models here.



class Squad(models.Model):
    squad_name = models.CharField(max_length = 40, default='Noname')
    squad_desc = models.CharField(max_length = 50, default='Noname')
    squad_start = models.DateTimeField(blank=True, default=datetime.datetime.now())
    squad_last = models.DateTimeField(blank=True, default=datetime.datetime.now())
    reputation = models.IntegerField(default=0)
    prospect = models.IntegerField(default=0)
    church = models.IntegerField(default=0)

    def __str__(self):
        return self.squad_name

class ActiveSession(models.Model):
    squad_id = models.IntegerField()

    def __str__(self):
        return self.squad_id

class AvaliableQuests(models.Model):
    squad_id = models.IntegerField()
    expansion = models.IntegerField()
    mission = models.CharField(max_length = 10, default=None, blank=True)
    finished = models.BooleanField()
    blocked = models.BooleanField()

