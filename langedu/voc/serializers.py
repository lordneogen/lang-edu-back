from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *
from rest_framework.response import Response

class SER_CR_Vocs(serializers.ModelSerializer):
    class Meta:
        model = Vocs
        fields = '__all__'


class SER_RUD_Vocs(serializers.ModelSerializer):
    
    
    class Meta:
        model = Vocs
        read_only_fields = ('owner')
        fields = '__all__'