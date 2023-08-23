from rest_framework import serializers
from .models import *


class SER_CR_Texts(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = '__all__'
    
    def validate(self, attrs):
        if not attrs['text'] or not attrs['owner']:
            raise serializers.ValidationError("Не null данные")
        else:
            return super().validate(attrs)


class SER_RUD_Texts(serializers.ModelSerializer):
    
    
    class Meta:
        model = Text
        read_only_fields = ('text','owner')
        fields = '__all__'