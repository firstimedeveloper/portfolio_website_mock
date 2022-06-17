from django.contrib.auth.models import User, Group
from rest_framework import serializers

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProjectSerializer
        fields = ['title', 'description', 'start_date', 'end_date', 'tags', 'url']
