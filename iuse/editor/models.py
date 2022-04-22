from django.db import models


# Create your models here.

class Content(models.Model):
    from sources.models import Source
    file = models.ForeignKey(Source, on_delete=models.SET_NULL, null=True)
    content = models.TextField(max_length=2000)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        index_together = (('file', 'updated_at'),)
        ordering = ('updated_at',)

    def __str__(self):
        return f'{self.file.name}-{self.content}'



