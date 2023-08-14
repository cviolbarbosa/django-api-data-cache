from django.db import models

# Create your models here.


class MeasurementModel(models.Model):
    name = models.CharField(blank=True, max_length=255, default='Untitled')
    data = models.TextField(blank=True)
    start_at = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
    end_at = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)