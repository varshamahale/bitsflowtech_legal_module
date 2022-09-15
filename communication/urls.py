
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import * #index, detail,EmailAttachementView


urlpatterns = [
    path('detail/', detail, name='detail'),
    path('index/', index, name='index'),
    path('email/',EmailAttachementView),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
