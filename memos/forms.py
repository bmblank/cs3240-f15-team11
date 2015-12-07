from .models import Memo
from django import forms
from django.contrib.auth.models import User
from django.db import models

class MemoForm(forms.ModelForm):

	class Meta:
		model = Memo
		fields = ('recipient_username', 'subject', 'body', 'encrypted')

class DecryptForm(forms.Form):
	decryptField = forms.CharField(max_length=5000, label='Private Key for Decryption', widget=forms.Textarea)