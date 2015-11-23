from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Memo(models.Model):
    sender = models.ForeignKey(User)
    recipient = models.CharField(max_length=200)
    subject = models.CharField(max_length=100)
    body = models.TextField(max_length=1000)
    created = models.DateTimeField(default=None)
