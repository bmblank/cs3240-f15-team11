import datetime
from django.utils import timezone
from django.contrib.auth.models import User

from django.db import models
from django.utils import timezone

class Sensitivity(models.Model):
    Public = 3
    Private = 2

    PRIORITY_CHOICES = (
        (Public, 'public'),
        (Private, 'private'),
    )

    sensitivity = models.IntegerField(choices=PRIORITY_CHOICES)

PRIORITY_CHOICES = ((1, 'Public'), (2, 'Private'))

class Report(models.Model):
    title = models.CharField(max_length=200)
    Short_Description = models.CharField(max_length=200)
    Detailed_Description = models.TextField(max_length=1000)
    Location_of_Event = models.CharField(max_length=100)
    Attachments = models.FileField(upload_to='report', blank=True)
    sensitivity = models.IntegerField(choices=PRIORITY_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    group_name = models.CharField(max_length=200, default='public')
    author = models.ForeignKey(User, null=True, related_name='author')


    def __str__(self):              # __unicode__ on Python 2
        return self.title
    def was_published_recently(self):
        return self.created >= timezone.now() - datetime.timedelta(days=1)



class Choice(models.Model):
    question = models.ForeignKey(Report)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):              # __unicode__ on Python 2
        return self.title