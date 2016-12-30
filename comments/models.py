from django.db import models
from django.utils import timezone

# Create your models here.

class Comment(models.Model):
    email = models.CharField(max_length=100)
    body = models.TextField()
    updated_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email
