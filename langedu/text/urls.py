from . import views
from django.urls import path, include

# from .views_cbf import RegisterView

urlpatterns = [
    path('', views.LIST_CR_Texts.as_view()),
    path('<int:id>/', views.RUD_Texts.as_view()),
]