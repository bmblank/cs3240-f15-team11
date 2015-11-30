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

    """def encryptBody(self, Rkey):
        #key = publicKey.importKey()
        public_key = Rkey.publickey()
        self.body = public_key.encrypt(self.body.encode('utf-8'), 32)

    def decryptBody(self, privateKey):
        key = privateKey.importKey()
        self.body = key.decrypt(self.body)"""

