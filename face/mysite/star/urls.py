from django.urls import path, include
from . import views
from star.views import classify_image
urlpatterns = [
    path('classify/', classify_image, name='classify_image'), # name은 다음에 경로를 바꿀때 경로를 다 바꾸지 않기 위해서 name이라는것을 미리 사용했다 
                                                              # star.views의 classify_image를 가져와서 views.classify_image의 경로의 길이를 줄였다
]