from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    highlight = serializers.HyperlinkedIdentityField(view_name='task-highlight', format='html')
    created_by = serializers.ReadOnlyField(source='created_by.username')
    class Meta:
        model = Task
        fields = '__all__'
        

class UserSerializer(serializers.HyperlinkedModelSerializer):
    tasks = serializers.HyperlinkedRelatedField(many=True,view_name='task-detail', queryset=Task.objects.all(),source='task_set')
    class Meta:
        model = User
        fields = ['url','username','email','tasks']
        