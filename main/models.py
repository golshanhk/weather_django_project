from django.db import models

class SearchHistory(models.Model):
    city_name = models.CharField(max_length=100)
    temperature = models.FloatField()
    humidity = models.IntegerField()
    description = models.CharField(max_length=50, null=True, blank=True)
    searched_at = models.DateTimeField(auto_now_add=True)