from django.db import models


class Extraction(models.Model):
    collection = status = models.CharField(
        max_length=100, null=True, blank=True, default=None)
    processes = models.FileField(blank=True, null=False)
    status = models.CharField(
        max_length=100, null=True, blank=True, default=None)
