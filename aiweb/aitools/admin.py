from django.contrib import admin
from .models import User, Upload

# Register your models here.
admin.site.register([User, Upload])