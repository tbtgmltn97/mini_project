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
    results = []
    for image_path in image_paths:
        try:
            with Image.open(image_path) as image:
                result = image_classify.classify(image)
                results.append(result)
        except Exception as e:
            results.append(str(e))
    
    # 결과를 템플릿으로 전달하여 표시
    return render(request, 'result.html', {'results': results})
    