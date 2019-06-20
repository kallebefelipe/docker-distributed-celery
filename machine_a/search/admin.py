from django.contrib import admin
from django.conf import settings
from search import models
from search.steps.manager_tasks import run_tasks
import os


def start_search(modeladmin, request, queryset):
    row = queryset.first()
    path = os.path.join(settings.MEDIA_ROOT, row.processes.name)
    run_tasks(row.collection, path, row.id)
    return path


start_search.shor_description = "Start Extração"


class ExtractionAdmin(admin.ModelAdmin):
    list_filter = ('collection', )
    list_display = ('collection', 'processes', 'status', )
    list_per_page = 20
    actions = [start_search]


admin.site.register(models.Extraction, ExtractionAdmin)
