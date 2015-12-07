from django.contrib.auth.models import User, Group
from reports.models import Report
from rest_framework import serializers




class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    groups = GroupSerializer(many=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class ReportSerializer(serializers.HyperlinkedModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Report
        fields = ('title', 'author', 'Short_Description', 'Detailed_Description', 'Location_of_Event', 'created',
                  'group_name', 'Attachments', 'url')  # TODO folder doesn't work
