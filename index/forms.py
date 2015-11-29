from reports.models import Report, Folder
from django import forms
from django.contrib.auth.models import User

class ReportForm(forms.ModelForm):

    class Meta:
        model = Report
        fields = ('title', 'Short_Description', 'Detailed_Description', 'Location_of_Event', 'Attachments', 'Attachment_is_Encrypted', 'Report_is_Public', 'group_name', 'folder')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('first_name', 'last_name','username', 'email', 'password')

class GivePermissionsForm(forms.Form):
    group = forms.CharField(max_length=200)
    user = forms.ModelMultipleChoiceField(queryset=User.objects.filter(is_active=True))

class SuspensionForm(forms.Form):
    active_users = forms.ModelMultipleChoiceField(queryset=User.objects.filter(is_active=True))

class UnsuspensionForm(forms.Form):
    suspended_users = forms.ModelMultipleChoiceField(queryset=User.objects.filter(is_active=False))


class MoveToFolderForm(forms.Form):
    folder_to_move_to = forms.CharField(max_length=200)

class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ('Folder_Name',)