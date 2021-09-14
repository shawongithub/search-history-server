from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SearchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    keyword = models.CharField(max_length=100)
    created_at = models.DateField()
    result = models.TextField()

    def __str__(self):
        return f'{self.user.username} searched {self.keyword}'