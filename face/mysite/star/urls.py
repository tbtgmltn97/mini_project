from django.urls import path, include
from . import views
from star.views import classify_image
urlpatterns = [
    # path('', views.index) ,
    #path('', views.index, name='index'),
    #path('classify/', classify_image, name='classify_image'),
    path('', classify_image, name='classify_image'),
]