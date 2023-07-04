from django.urls import path
from .views import *

urlpatterns = [
    path('', ShoppingView.as_view(),name='shopping'),
    path('tanlangan/', TanlanganView.as_view(),name='tanlangan'),
    path('tanlangan-ochir/<int:son>', TanlanganOchirView.as_view()),
    path('orders/', BuyurtmaView.as_view(),name='orders'),
    path('savat_k/<int:son>/', MiqdorKamaytir.as_view()),
    path('savat_q/<int:son>/', MiqdorQosh.as_view()),
    path('savat_item_q/<int:pk>/', SavatItemQosh.as_view()),
    path('buyurtma_qosh/<int:pk>/', BuyurtmaQosh.as_view()),
    path('ochirish/<int:son>/', OchirishView.as_view()),
]




