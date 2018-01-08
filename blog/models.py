from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    HEAD
    author = models.ForeignKey('auth.User', on_delete = True)
    author = models.ForeignKey('auth.User', on_delete=True)
    81c3f9264219ca2d379da22000322fd70784f633
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
