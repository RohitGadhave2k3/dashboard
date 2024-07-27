from django.http import HttpResponse
from rest_framework import viewsets
from .models import DataPoint
from .serializers import DataPointSerializer

# ViewSet for handling CRUD operations on DataPoint model
class DataPointViewSet(viewsets.ModelViewSet):
    queryset = DataPoint.objects.all()
    serializer_class = DataPointSerializer

# View function for the index/welcome page
def index(request):
    return HttpResponse("Welcome to the Dashboard API")
