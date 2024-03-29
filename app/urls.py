from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('evaluate', views.evaluate, name='evaluate'),
    path('kannada_lambani', views.kannada_lambani, name='kannada_lambani'),
    path('lambani_kannada', views.lambani_kannada, name='lambani_kannada'),
    path('audio', views.audio, name='audio'),
    path('saveText', views.saveText, name='saveText'),
    path('saveKannadaLambani', views.saveKannadaLambani, name='saveKannadaLambani'),
    path('saveLambaniKannada', views.saveLambaniKannada, name='saveLambaniKannada'),
    path('saveAudio', views.saveAudio, name='saveAudio'),
    path('rating', views.rating, name='rating')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
