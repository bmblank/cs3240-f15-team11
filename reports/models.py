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

    def __str__(self):
        return self.Folder_Name

class Report(models.Model):
    title = models.CharField(max_length=200)
    Short_Description = models.CharField(max_length=200)
    Detailed_Description = models.TextField(max_length=1000)
    Location_of_Event = models.CharField(max_length=100)
    Attachments = models.FileField(upload_to='report', blank=True)
    # sensitivity = models.IntegerField(choices=PRIORITY_CHOICES)
    Attachment_is_Encrypted = models.BooleanField(default=False)
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

# class AdditionalUserInfo(models.Model):
    # the_user = models.ForeignKey(User, null=True, related_name='the_user')
    # new_message = models.BooleanField(default=False)
    # public key??
    # user = models.OneToOneField(
    #     settings.AUTH_USER_MODEL,
    #     on_delete=models.CASCADE,
    # )
    # supervisor = models.OneToOneField(
    #     settings.AUTH_USER_MODEL,
    #     on_delete=models.CASCADE,
    #     related_name='supervisor_of',
    # )


#one to one relationship for adding attributes to User modelsclass MySpecialUser(models.Model):
# class MySpecialUser(models.Model):
#     user = models.OneToOneField(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#     )
#     supervisor = models.OneToOneField(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#         related_name='supervisor_of',
#     )