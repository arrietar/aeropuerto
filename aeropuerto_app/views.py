from django.shortcuts import render
from aeropuerto_app.models import *
from aeropuerto_app.serializers import *
from rest_framework import viewsets, status

# Create your views here.

class Base_view(viewsets.ModelViewSet):
    queryset = Base.objects.all()
    serializer_class = Base_Serializer
