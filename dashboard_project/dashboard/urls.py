from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DataPointViewSet, index

router = DefaultRouter()
router.register(r'datapoints', DataPointViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('api/', include(router.urls)),
]
