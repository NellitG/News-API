from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('travelnews/', include('travelnews.urls')),
    path('destinations/', include('travelnews.urls')),
]
