from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Memo(models.Model):
    sender = models.ForeignKey(User, null=True, related_name='sender')
    recipient = models.ForeignKey(User, null=True, related_name='recipient')
    recipient_username = models.CharField(max_length=100)
    subject = models.CharField(max_length=100, default=None)
    body = models.TextField(max_length=1000)
    created = models.DateTimeField(default=None)
