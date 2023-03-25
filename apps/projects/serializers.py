from rest_framework import serializers
from .models import Project, Tecnology


class ProjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        fields = '__all__'
    
class TecnologySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tecnology
        fields = '__all__'
