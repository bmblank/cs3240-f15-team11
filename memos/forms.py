from .models import Memo
from django import forms
from django.contrib.auth.models import User

class MemoForm(forms.ModelForm):

    class Meta:
        model = Memo
        fields = ('sender', 'recipient', 'subject', 'body', 'cc_myself', )

        sender = forms.CharField(label="Sender", required=True)
        recipient = forms.CharField(label="Recipient", required=True)
        subject = forms.CharField(label="Subject", max_length=200)
        body = forms.CharField(label="Message Body", widget=forms.Textarea)
        cc_myself = forms.BooleanField(label="CC Myself", required=False)
        encrypt = forms.BooleanField(label="Encrypt Message", required=False)