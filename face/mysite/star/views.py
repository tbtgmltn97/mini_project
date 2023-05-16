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
    image_dir = '/Users/jangjinsu/encore/crawling/구교환'
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
     
    # 결과 값을 prediction 변수에 할당
    prediction = ', '.join(results)
    
    # 결과를 템플릿으로 전달하여 표시
    return render(request, 'result.html', {'results': prediction})

import os
import face_recognition
from django.shortcuts import render
from matplotlib import pyplot as plt
import matplotlib.image as img

def face_recognition(request):
    # load the image to be matched
    image_to_be_matched = face_recognition.load_image_file('123.jpg')
    image_to_be_matched_encoded = face_recognition.face_encodings(image_to_be_matched)[0]
    # load all the images in the directory
    images = os.listdir('images')
    # Calculate the face distance for each image and store it in a dictionary
    distances = {}
    for image in images:
        current_image = face_recognition.load_image_file("images/" + image)
        current_image_encoded = face_recognition.face_encodings(current_image)[0]
        distance = face_recognition.face_distance([image_to_be_matched_encoded], current_image_encoded)
        distances[image] = distance
    # Sort the dictionary by distance and get the closest image
    closest_image = min(distances, key=distances.get)
    # Print the closest image and display it
    print("Matched: " + closest_image)
    fileName = "images/" + closest_image
    ndarray = img.imread(fileName)
    response_data = {'image': ndarray}
    return render(request, 'face_recognition.html', response_data)

