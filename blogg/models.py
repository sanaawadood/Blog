import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    content = models.TextField()
    heading = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    writer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return (self.heading)

class Comment(models.Model):
    content = models.TextField()
    pub_date = models.DateTimeField('date published')
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    of_post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return (self.content)
