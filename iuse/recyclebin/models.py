from django.db import models
from sources.models import Source
from django.contrib.auth.models import User


# Create your models here.

class Garbage(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    source = models.ForeignKey(Source, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
