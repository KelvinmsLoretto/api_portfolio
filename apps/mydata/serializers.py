from rest_framework import serializers
from .models import MyData

class MyDataSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = MyData
        fields = '__all__'
        

