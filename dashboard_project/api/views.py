from django.shortcuts import render

# Create your views here.
# views.py in your Django app (e.g., api/views.py)

from rest_framework import viewsets
from .models import DataPoint
from .serializers import DataPointSerializer

class DataPointViewSet(viewsets.ModelViewSet):
    queryset = DataPoint.objects.all()
    serializer_class = DataPointSerializer
