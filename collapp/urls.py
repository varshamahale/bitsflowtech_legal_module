from django.contrib import admin
from django.urls import path

from .views import Colapp_legal_views,Colapp_mst_views

urlpatterns = [
    path('legal/<int:id>', Colapp_legal_views),
    path('<int:id>', Colapp_mst_views),
]