from reports.models import Report
from django import forms

class ReportForm(forms.ModelForm):

    class Meta:
        model = Report
        fields = ('title', 'Short_Description', 'Detailed_Description', 'Location_of_Event', 'Attachments', 'sensitivity')

