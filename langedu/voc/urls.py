from . import views
from django.urls import path, include
# from .views_cbf import RegisterView

urlpatterns = [
    path('', views.LIST_CR_Vocs.as_view(),name='my-view-name'),
    path('<int:id>/', views.RUD_Vocs.as_view()),
]
