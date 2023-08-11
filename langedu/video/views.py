from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny

from . import serializers
from .models import *
from .serializers import SER_Videos
from rest_framework.response import Response

class LIST_Videos(generics.ListAPIView, generics.RetrieveAPIView):
    queryset =  Videos.objects.all()
    serializer_class = serializers.SER_Videos

    def list(self, request, *args, **kwargs):
        pk=kwargs.get('id')
        if pk:
            queryset = Videos.objects.filter(pk=pk)
        else:
            queryset = self.get_queryset()
        serializer = serializers.SER_Videos(data=queryset, many=True)
        if serializer.is_valid():
            return {'error':'Нету видео'}
        if pk:
            return Response(serializer.data[0])
        else:
            return Response(serializer.data)
    def post(self, request, *args, **kwargs):
        ser = serializers.SER_Videos(data=request.data)
        if ser.is_valid():
            ser.save()
        return Response(ser.data)
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('id')
        if pk==None:
            return Response("Обьекта не сущетсвует в списке")
        obj = Videos.objects.get(pk=pk)
        obj.delete()
        return Response("Item succsesfully delete!")
    def put(self, request, *args, **kwargs):
        pk = kwargs.get('id')
        obj = Videos.objects.get(id=pk)
        ser = serializers.SER_Videos(instance=obj, data=request.data)
        if ser.is_valid():
            ser.save()
        return Response(ser.data)