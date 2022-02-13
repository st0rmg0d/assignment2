from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.line, name='line'),
    path('', views.pie, name='pie'),
]
