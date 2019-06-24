from django.db import models
from apps.quiz_app.models import *
from apps.course_app.models import *
from apps.video_app.models import *


# Create your models here.
class UserManager(models.Manager):
    pass


class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=100)
    password_hash = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    objects = UserManager()
