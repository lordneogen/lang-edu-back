from . import views
from django.urls import path, include

# from .views_cbf import RegisterView

urlpatterns = [
    path('', views.LIST_Text.as_view()),
    path('<int:id>/', views.LIST_Text.as_view()),
]