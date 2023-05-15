import os
from PIL import Image
from .models import Post
from django.shortcuts import render
from django.http import HttpResponse
import image_classify

# Create your views here.
def index(request):
    posts = Post.objects.order_by('-views')[:5]
    context = {'posts': posts}
    return render(request, 'index.html', context)

def classify_image(request):
    # 이미지 파일 경로를 포함하는 리스트 생성
    image_dir = '/path/to/image/directory'
    image_paths = [os.path.join(image_dir, f) for f in os.listdir(image_dir) if f.endswith('.jpg')]
    
    # 이미지 분류 작업 처리 코드
    for image_path in image_paths:
        image = Image.open(image_path)
        result = image_classify.classify(image)
        print(result)
    
    return HttpResponse("Image classification is done.")
    