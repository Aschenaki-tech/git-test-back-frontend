# project_name/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('songs.urls')),
    path('admin/', admin.site.urls),
    
    # Include the app URLs
]
