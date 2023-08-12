from rest_framework import serializers
from .models import *


class SER_Text(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = '__all__'