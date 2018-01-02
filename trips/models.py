from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    photo = models.URLField(blank=True)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    #docfile = models.FileField(upload_to='documents/%Y/%m/%d')

    def __str__(self):
        return self.title
# Create your models here.
