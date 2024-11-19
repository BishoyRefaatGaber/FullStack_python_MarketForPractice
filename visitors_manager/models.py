from django.db import models

# Create your models here.



class Visitors(models.Model):
    ip = models.CharField(default='0.0.0.0',max_length=15)
    location = models.CharField(default='Unknown',max_length=50)
    no_visits = models.IntegerField(default=0)
    def __str__(self):
        return self.ip