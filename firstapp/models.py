from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(null=True, blank=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/post/{self.pk}'
        
        
class FileUpload(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=40, null=True)
    imgfile = models.ImageField(null=True, upload_to="", blank=True)
    memo = models.TextField()

    def __str__(self):
        return self.title