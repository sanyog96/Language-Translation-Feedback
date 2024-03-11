from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('homepage', views.index, name='homepage'),
    path('register', views.post, name='register')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)