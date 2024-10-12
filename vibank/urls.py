from django.urls import path
from . import views

app_name = 'vibank'

urlpatterns = [
    path('', views.home, name="home"),
    path('cartões', views.cartoes, name="cartões"),
    path('pjemei', views.pjemei, name="pjemei"),
    path('pessoafisica', views.pessoafisica, name="pessoafisica"),
]
