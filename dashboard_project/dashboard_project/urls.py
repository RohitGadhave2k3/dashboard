from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('dashboard.urls')),  # Include your app's URLs here
    # Add a catch-all route for the root path to handle requests
    path('', include('dashboard.urls')),  # Assuming you want to route root path to dashboard app
]
