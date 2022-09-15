from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('legal/<int:id>', collapp_vegeata_views),
    path('<int:id>', collapp_mst_views),
]