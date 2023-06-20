from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(),name='home'),
    path('bolimlar/', HammaBolimView.as_view(),name='bolimlar'),
    path('mahsulot/<int:pk>/', BittaMahsulotView.as_view()),
    path('bolim/<int:pk>/', BolimView.as_view(),name='Mahsulotlar'),
]





