from django.db import models
from django.utils import timezone
class UserAccount(models.Model):
    user_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200,default='')
    phone = models.CharField(max_length=200,default='')
    start_date = models.DateField(default='')
    end_date = models.DateField(default='')
   # rides = models.JSONField(null=True)

    def __str__(self):
        return self.name;