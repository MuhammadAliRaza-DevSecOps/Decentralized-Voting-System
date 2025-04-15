from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vote.urls')),  # Your app URLs
    path('accounts/', include('django.contrib.auth.urls')),  # Includes login & logout
]
