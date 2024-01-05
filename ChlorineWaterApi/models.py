from django.db import models
import uuid
from datetime import datetime

# Create your models here.

class UserMaster(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    Name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    loginid = models.CharField(db_column='loginid',max_length=50)
    pwd = models.CharField(db_column='pwd',max_length=50)
    roleid = models.IntegerField(default=1)
    orgid = models.IntegerField(default = 1, blank=True, null=True)
    region = models.IntegerField(default = 1,blank=True, null=True)
    portion = models.IntegerField(default = 1,blank=True, null=True)
    user_group = models.IntegerField(default = 1,blank=True, null=True)
    stock_alltr = models.IntegerField(default = 1,blank=True, null=True)
    active = models.BooleanField(default = 1,blank=True, null=True)
    dbdatetime = models.DateTimeField(default=datetime.now(), null=True)

    class Meta:
        managed = True
        db_table = 'User_Master'   
