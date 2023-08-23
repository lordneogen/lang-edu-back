from . import views
from django.urls import path, include

# from .views_cbf import RegisterView

urlpatterns = [
    path('',),
    path('<int:id>/'),
    path('<int:id>/video/'),
    path('<int:id>/video/<int:vid>/'),
    path('<int:id>/text/'),
    path('<int:id>/text/<int:tid>/'),
    path('<int:id>/voc/'),
    path('<int:id>/voc/<int:vid>/'),
]