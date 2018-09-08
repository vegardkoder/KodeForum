from django.db import models
from personal.models import UserProfile
from django.contrib.auth.models import User

class Post(models.Model):
    tittel = models.CharField(max_length=140)
    innhold = models.TextField(max_length=2500)
    date = models.DateTimeField()
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.tittel

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comment', on_delete=models.CASCADE)
    com_innhold = models.TextField(max_length=2500)
    user = models.ForeignKey(User, on_delete=None)

    def __str__(self):
        return self.com_innhold

