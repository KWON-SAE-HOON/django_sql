from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    create_time = models.TimeField(auto_now=True)
    updated_time = models.TimeField(auto_now_add=True)