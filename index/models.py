from django.db import models
from Crypto.PublicKey import RSA
from Crypto import Random

# Create your models here.

from django.contrib.auth.models import User

randomGen = Random.new().read
key = RSA.generate(1024, randomGen)



"""class Key(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    privateKey = models.TextField(null=True, blank=True)
    publicKey = models.TextField(null=True, blank=True)

    def set_privateKey(self, value):
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
