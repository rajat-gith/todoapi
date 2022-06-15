from dataclasses import fields
import imp
from re import M
from rest_framework import serializers
from .models import Task

class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields='__all__'