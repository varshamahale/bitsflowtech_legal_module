
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('colapp/',include('collapp.urls')),
    path('legal/',include('legal.urls')),
]
