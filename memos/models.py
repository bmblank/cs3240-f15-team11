from django.db import models
from django.contrib.auth.models import User
from Crypto.PublicKey import RSA
from Crypto import Random

random_generator = Random.new().read
PrivateKey = RSA.generate(1024, random_generator)
public_key = PrivateKey.publickey

# Create your models here.
class Memo(models.Model):
    sender = models.ForeignKey(User, null=True, related_name='sender')
    recipient = models.ForeignKey(User, null=True, related_name='recipient')
    recipient_username = models.CharField(max_length=100)
    subject = models.CharField(max_length=100, default=None)
    body = models.TextField(max_length=1000)
    created = models.DateTimeField(default=None)
    encrypted = models.BooleanField(default=False)

class Key(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    privateKey = models.TextField(null=True, blank=True)
    publicKey = models.TextField(null=True, blank=True)
    rKey = models.TextField(null=True, blank=True)
    #userKey = models.BinaryField(null=False)

    """def set_privateKey(self, value):
        self.privateKey = value
        self.privateKey = key.exportKey()
        print(self.privateKey)

    def get_privateKey(self):
        print(self.privateKey)
        return self.privateKey

    def set_publicKey(self, value):
        self.publicKey = value
        self.publicKey = key.publickey().exportKey()
        print(self.publicKey)

    def get_publicKey(self):
        print(self.publicKey)
        return self.publicKey"""

    def get_username(self):
        return self.user.username

