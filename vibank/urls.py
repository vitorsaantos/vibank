from django.urls import path
from . import views

app_name = 'vibank'

urlpatterns = [
    path('', views.home, name="home")
]
