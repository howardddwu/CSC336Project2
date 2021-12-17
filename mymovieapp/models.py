from django.db import models

# Create your models here.
class Users(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=16)
    status = models.SmallIntegerField(default=0) # 0 is user 1 is admin

    class Meta:
        db_table = "user"

class Movies(models.Model):
    id = models.AutoField(primary_key=True)
    moviename = models.CharField(max_length=16)
    gnere = models.CharField(max_length=16)
    year = models.IntegerField(default=2000)
    actors = models.CharField(max_length=16)
    duration = models.CharField(max_length=16)
    rating = models.FloatField(default=0)
    class Meta:
        db_table = "movies"