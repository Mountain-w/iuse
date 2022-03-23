from django.contrib import admin
from sources.models import Source
# Register your models here.

@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ('parent_dir', 'name', 'owner')