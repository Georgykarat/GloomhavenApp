from django.db import models

# Create your models here.



class Squad(models.Model):
    squad_name = models.CharField(max_length = 20)
    squad_desc = models.CharField(max_length = 50)
    squad_start = models.DateTimeField()
    squad_last = models.DateTimeField()
    reputation = models.IntegerField()
    prospect = models.IntegerField()
    church = models.IntegerField()

    def __str__(self):
        return self.access