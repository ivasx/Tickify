import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from tasks.models import Task



class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        # fields = ('slug', 'title', 'description', 'completed', 'priority', 'deadline', 'category', 'user', 'photo', 'created_at', 'updated_at', 'completed_at')
        fields = '__all__'

    # slug = serializers.CharField(max_length=255)
    # title = serializers.CharField(max_length=255)
    # description = serializers.CharField()
    # completed = serializers.BooleanField(default=False)
    # priority = serializers.IntegerField()
    # deadline = serializers.DateTimeField(required=False)
    # category_id = serializers.IntegerField()
    # user_id = serializers.IntegerField()
    # photo = serializers.ImageField(required=False)
    #
    # created_at = serializers.DateTimeField(read_only=True)
    # updated_at = serializers.DateTimeField(read_only=True)
    # completed_at = serializers.DateTimeField(read_only=True)

    # def create(self, validated_data):
    #     return Task.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.slug = validated_data.get('slug', instance.slug)
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.completed = validated_data.get('completed', instance.completed)
    #     instance.priority = validated_data.get('priority', instance.priority)
    #     instance.deadline = validated_data.get('deadline', instance.deadline)
    #     instance.category_id = validated_data.get('category_id', instance.category_id)
    #     instance.user_id = validated_data.get('user_id', instance.user_id)
    #     instance.photo = validated_data.get('photo', instance.photo)
    #     instance.updated_at = validated_data.get('updated_at', instance.updated_at)
    #     instance.save()
    #     return instance

