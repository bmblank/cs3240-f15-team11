from django.db import models

# Create your models here.
class Memo(models.Model):
    sender = models.CharField(max_length=200)
    recepient = models.CharField(max_length=200)
    subject = models.CharField(max_length=100)
    body = models.TextField(max_length=1000)
