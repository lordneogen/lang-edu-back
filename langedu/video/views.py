from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny

from . import serializers
from .models import *
from rest_framework.response import Response
from rest_framework import status

class LIST_CR_Videos(generics.ListAPIView, generics.RetrieveAPIView):
    
    model=Videos
    queryset =  model.objects.all()
    serializer_class = serializers.SER_CR_Videos
    
    def list(self, request, *args, **kwargs):
        
        serializer = self.serializer_class(data=self.get_queryset(), many=True)

        if serializer.is_valid() or len(self.get_queryset())==0 :
            return Response({'error':'Нету видео'},status=404)
        
        return Response(serializer.data)
        
    def post(self, request, *args, **kwargs):
        
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
        return Response(serializer.data)

class RUD_Videos(generics.RetrieveUpdateDestroyAPIView):
    
    
    model=Videos
    serializer_class = serializers.SER_RUD_Videos
    
    
    def get(self, request, *args, **kwargs):
        try:
            pk = kwargs.get('id')
            video = self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            return Response({"error": "Нет такого видео"}, status=status.HTTP_404_NOT_FOUND)
        except:
            return Response({"error": "Неправильно введенные данные"}, status=status.HTTP_400_BAD_REQUEST)
    
        serializer = self.serializer_class(video)
        return Response(serializer.data)
        
    def delete(self, request, *args, **kwargs):
        
        try:
            pk=kwargs.get('id')
        except:
            return Response({"error":"Непрравильно введенны данные"})
        
        if not self.model.objects.filter(pk=pk):
            return Response({"error":"Нету такого видео"},status=404)
        
        queryset =self.model.objects.get(pk=pk)
        queryset.delete()
        
        return Response({"result":"Видео удалено"},status=200)
    
    def put(self, request, *args, **kwargs):
        
        try:
            pk=kwargs.get('id')
        except:
            return Response({"error":"Непрравильно введенны данные"})
        
        if not self.model.objects.get(pk=pk):
            return Response({"error":"Нету такого видео"},status=404)
        
        queryset = self.model.objects.get(id=pk)
        serializer = self.serializer_class(instance=queryset, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
        return Response(serializer.data)