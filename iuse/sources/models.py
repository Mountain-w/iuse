from django.db import models
from django.contrib.auth.models import User
from utils.modelshelpers.enums import FileType, DeleteStatus

# Create your models here.\


class Source(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    type = models.CharField(max_length=1, choices=FileType.choices, default=FileType.FILE)
    name = models.CharField(max_length=200, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    parent_dir = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, default=None)
    on_delete = models.CharField(max_length=1, choices=DeleteStatus.choices, default=DeleteStatus.exists)
    deleted_at = models.DateTimeField(auto_now=True)

    class Meta:
        index_together = (('name', 'created_at'),)
        ordering = ('created_at', 'name')
