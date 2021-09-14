from django.db import models

# Create your models here.
class SearchHistory(models.Model):
    user = models.CharField(max_length=100)
    keyword = models.CharField(max_length=100)
    created_at = models.DateField()
    result = models.TextField()