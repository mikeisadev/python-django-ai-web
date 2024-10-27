import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=120, unique=True)
    password = models.CharField(max_length=128)

    registration_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.first_name
    
    def was_registered_recently(self):
        return self.registration_date >= timezone.now() - datetime.timedelta(days=1)

class Upload(models.Model):
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    upload_uuid = models.CharField(max_length=36, unique=True)
    file_path = models.CharField(max_length=1024)
    file_mime_type = models.CharField(max_length=50)
    file_ext = models.CharField(max_length=50)
    file_size = models.FloatField()

    uploaded_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.upload_uuid
    
    def was_uploaded_recently(self):
        return self.uploaded_on >= (timezone.now() - datetime.timedelta(days=1))