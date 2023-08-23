from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *
from rest_framework.response import Response

class SER_CR_Videos(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = '__all__'
    
    def validate(self, attrs):
        if not attrs['str'] or not attrs['video'] or not attrs['owner']:
            raise serializers.ValidationError("Не null данные")
        else:
            return super().validate(attrs)


class SER_RUD_Videos(serializers.ModelSerializer):
    
    
    class Meta:
        model = Videos
        read_only_fields = ('video','str','owner')
        fields = '__all__'