__author__ = 'jrh7qp'

from django import forms
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.db import models
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import ARC4
from Crypto.Hash import SHA256

random_generator = Random.new().read
key = RSA.generate(1024, random_generator)
public_key = key.publickey()
"""the sender must have the public key of receiver, receiver uses their own private key to decrypt"""
enc_body = public_key(MESSAGE_BODY)
signature = key.sign(enc_body, ' ')

#EVERY USERS PUBLIC KEY MUST BE GIVEN TO EVERY USER?



def encryptText():

    """checks capability of encrypting with this algorithm"""
    #key.can_encrypt()
    """checks key's capability of signing messages"""
    #key.can_sign()
    """checks if key object has private key"""
    #key.has_private()



class EncryptionWarning(RuntimeWarning):
    pass


class EncryptedTextField(models.TextField):

    __metaclass__ = models.SubfieldBase

    def __init__(self, *args, **kwargs):
        super(EncryptedTextField, self).__init__(*args, **kwargs)
        cipher_type = kwargs.pop('cipher', 'AES')
        self.encryptor = Encryptor(cipher_type)

    """def isEncrypted(self, value):
        return encrypt_if_not_encrypted(value, self.encryptor)

    def to_python(self, value):
        return decrypt_if_not_decrypted(value, self.encryptor)"""

    def encrypt(value):
        encrypted = public_key(value)
        """if isinstance(value, EncryptedString):
            return value
        else:
            encrypted = public_key(value)
            #encrypted = encryptor.encrypt(value)
            #return EncryptedString(encrypted)"""
        return encrypted

    def decrypt(value, privateKey):
        encrypted = value
        decrypted = privateKey()
        """if isinstance(value, DecryptedString):
            return value
        else:
            encrypted = encryptor.decrypt(value)
            return DecryptedString(encrypted)"""


class Encryptor(object):
  def __init__(self, cipher_type):
    imp = __import__('Crypto.Cipher', globals(), locals(), [cipher_type], -1)
    self.cipher = getattr(imp, cipher_type).new(settings.SECRET_KEY[:32])

  def decrypt(self, value):
    #values should always be encrypted no matter what!
    #raise an error if tthings may have been tampered with
    return self.cipher.decrypt(binascii.a2b_hex(str(value))).split('\0')[0]

  def encrypt(self, value):
    if value is not None and not isinstance(value, EncryptedString):
      padding  = self.cipher.block_size - len(value) % self.cipher.block_size
      if padding and padding < self.cipher.block_size:
        value += "\0" + ''.join([random.choice(string.printable) for index in range(padding-1)])
      value = EncryptedString(binascii.b2a_hex(self.cipher.encrypt(value)))
    return value
