from django.db import models
from django.utils import timezone

class DataPoint(models.Model):
    end_year = models.IntegerField(null=True, blank=True)
    intensity = models.IntegerField(null=True, blank=True)
    sector = models.TextField()
    topic = models.TextField()
    insight = models.TextField()
    url = models.TextField()
    region = models.TextField()
    start_year = models.IntegerField(null=True, blank=True)
    impact = models.TextField()
    added = models.DateTimeField(default=timezone.now)
    published = models.DateTimeField(default=timezone.now)
    country = models.TextField()
    relevance = models.IntegerField(null=True, blank=True)
    pestle = models.TextField()
    source = models.TextField()
    title = models.TextField()
    likelihood = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'datapoint'
