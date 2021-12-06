from django.db import models

# Create your models here.
class Users(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=16)
    status = models.SmallIntegerField(default=0) # 0 is user 1 is admin

    class Meta:
        db_table = "user"