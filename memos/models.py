from django.db import models

# Create your models here.
from Crypto.PublicKey import RSA
from Crypto import Random
from django.conf import settings
AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

randomGen = Random.new().read


class Memo(models.Model):

    sender = models.ForeignKey(AUTH_USER_MODEL, null=True, blank=True, max_length=200, related_name="sender")
    recipient = models.ForeignKey(AUTH_USER_MODEL, max_length=200, null=True, blank=True, related_name="recipient")
    subject = models.CharField(max_length=100)
    body = models.TextField(max_length=1000, verbose_name="Message Body")
    cc_myself = models.BooleanField(verbose_name="CC Myself", null=False, blank=False)
    encrypt = models.BooleanField(verbose_name="Encrypt Message", null=False, blank=False)

    def encryptBody(self):
        publicKey = RSA.importKey(self.recipient.publicKey)
        self.body = publicKey.encrypt(self.body)
        return self.body

    def decryptBody(self):
        privateKey = RSA.importKey(self.private)
        self.body = privateKey.decrypt(self.body)
        return self.body
