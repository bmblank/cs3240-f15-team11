from reports.models import Report
from django import forms
from django.contrib.auth.models import User

class ReportForm(forms.ModelForm):

    class Meta:
        model = Report
        fields = ('title', 'Short_Description', 'Detailed_Description', 'Location_of_Event', 'Attachments', 'sensitivity')


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')