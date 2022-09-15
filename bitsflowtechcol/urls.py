from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    # path('collapp/',include('collapp.urls')),
    # path('legal/',include('legal.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('communication/',include('communication.urls')),
]