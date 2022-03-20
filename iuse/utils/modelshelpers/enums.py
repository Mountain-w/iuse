from django.db import models


class FileType(models.IntegerChoices):
    FILE = 1
    DIR = 2


class DeleteStatus(models.IntegerChoices):
    has_deleted = 1
    exists = 0