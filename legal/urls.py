from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('<int:id>', Legal_views),
    path('colapp/<int:id>', Legal_colapp_views),
]