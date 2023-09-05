from . import views
from django.urls import path, include

# from .views_cbf import RegisterView

urlpatterns = [
    path('video/'),
    path('video/page/<int:id>/'),
    path('video/<int:id>/'),
    path('text/'),
    path('text/page/<int:id>/'),
    path('text/<int:id>/'),
    path('voc/'),
    path('voc/page/<int:vid>/'),
    path('voc/<int:vid>/'),
]