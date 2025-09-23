from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from tasks.models import Task

class TaskModel:
    def __init__(self, title, description, category):
        self.title = title
        self.description = description
        self.category = category


class TaskSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    category = serializers.CharField(max_length=255)

def encode():
    model = TaskModel(title="test", description="test", category="test")
    model_sr = TaskSerializer(model)
    print(model_sr.data, type(model_sr.data), sep="\n")
    json = JSONRenderer().render(model_sr.data)
    print(json)