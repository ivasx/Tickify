
from rest_framework import serializers
from tasks.models import Task



class TaskSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Task
        # fields = ('slug', 'title', 'description', 'completed', 'priority', 'deadline', 'category', 'user', 'photo', 'created_at', 'updated_at', 'completed_at')
        fields = '__all__'

