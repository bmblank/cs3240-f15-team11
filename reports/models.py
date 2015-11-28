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


class Folder(models.Model):
    Folder_Name = models.CharField(max_length=200)
    creator = models.ForeignKey(User, default=None, null=True, related_name='creator')

    def pure_folder_name(self):
        ind = self.Folder_Name.find('_____')+4
        return self.Folder_Name[ind:]

class Report(models.Model):
    title = models.CharField(max_length=200)
    Short_Description = models.CharField(max_length=200)
    Detailed_Description = models.TextField(max_length=1000)
    Location_of_Event = models.CharField(max_length=100)
    Attachments = models.FileField(upload_to='report', blank=True)
    # sensitivity = models.IntegerField(choices=PRIORITY_CHOICES)
    Report_is_Public = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    group_name = models.CharField(max_length=200, default='Public')
    author = models.ForeignKey(User, null=True, related_name='author')
    folder = models.ForeignKey(Folder, default=None, null=True, related_name='author')


    def __str__(self):              # __unicode__ on Python 2
        return self.title
    def was_published_recently(self):
        return self.created >= timezone.now() - datetime.timedelta(days=1)

    def folder_name_as_string(self):
        if self.folder:
            return self.folder.Folder_Name
        else:
            return None

class Choice(models.Model):
    question = models.ForeignKey(Report)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):              # __unicode__ on Python 2
        return self.title