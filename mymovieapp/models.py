from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Users(models.Model):
#     id = models.AutoField(primary_key=True)
#     username = models.CharField(max_length=16)
#     password = models.CharField(max_length=16)
#     status = models.SmallIntegerField(default=0) # 0 is user 1 is admin

#     class Meta:
#         db_table = "user"

class Movies(models.Model):
    movie_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64, default="title")
    overview = models.CharField(max_length=1024, default="no overview")
    backdrop_path = models.CharField(max_length=128, null=True)
    poster_path = models.CharField(max_length=128, null=True)
    release_date = models.DateField(null=True)
    rating = models.FloatField(default=0)
    favorites = models.ManyToManyField(
        User, related_name='favorite', default=None, blank=True
    )
    watchlist = models.ManyToManyField(
        User, related_name='watch', default=None, blank=True
    )
    
    def __str__(self):
        return self.title
    class Meta:
        db_table = "movies"