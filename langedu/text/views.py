from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny

from . import serializers
from .models import *
from rest_framework.response import Response


# Create your views here.
class LIST_Text(generics.ListAPIView, generics.RetrieveAPIView):
    queryset =  Text.objects.all()
    serializer_class = serializers.SER_Text

    def list(self, request, *args, **kwargs):
        pk=kwargs.get('id')
        if pk:
            queryset = Text.objects.filter(pk=pk)
        else:
            queryset = self.get_queryset()
        serializer = serializers.SER_Text(data=queryset, many=True)
        if ( serializer.is_valid() or len(queryset)==0 ) and pk:
            return Response({'error':'Нету видео'},status=404)
        if pk:
            return Response(serializer.data[0])
        else:
            return Response(serializer.data)
    def post(self, request, *args, **kwargs):
        ser = serializers.SER_Text(data=request.data)
        if ser.is_valid():
            ser.save()
        return Response(ser.data)
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('id')
        if pk==None:
            return Response("Обьекта не сущетсвует в списке")
        obj = Text.objects.get(pk=pk)
        obj.delete()
        return Response("Item succsesfully delete!")
    def put(self, request, *args, **kwargs):
        pk = kwargs.get('id')
        obj = Text.objects.get(id=pk)
        ser = serializers.SER_Text(instance=obj, data=request.data)
        if ser.is_valid():
            ser.save()
        return Response(ser.data)