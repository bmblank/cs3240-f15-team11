from .models import Memo
from django import forms
from django.contrib.auth.models import User

class MemoForm(forms.ModelForm):

    class Meta:
        model = Memo
        fields = ('sender', 'recepient', 'subject', 'body')
