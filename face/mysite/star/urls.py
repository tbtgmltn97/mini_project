from django.urls import path, include
from star import views

urlpatterns = [
    # path('', views.index) ,
    path('', views.index, name='index')
]