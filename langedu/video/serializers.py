from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *


class SER_Videos(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = '__all__'