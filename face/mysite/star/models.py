import tensorflow as tf
from django.db import models
from PIL import Image
import numpy as np
import os

class ImageClassifier:
    def __init__(self, model_path):
        self.model = tf.keras.models.load_model(model_path)
    def classify_image(self, image):
        class_label=['강해린',
'김채원',
'뉴진스 하니',
'안유진',
'아린',
'장원영',
'카즈하',
'차은우',
'방탄소년단 뷔',
'정준하',
 '정형돈',
 '서강준',
 '카리나',
 '마동석',
 '박보검',
 '손석구',
 '아이브 가을',
 '이광수',
 '침착맨',
 '르세라핌 사쿠라',]
        img = Image.open(image)
        img = img.resize((224, 224))  # 모델에 맞는 이미지 크기로 조정
        img = np.array(img) / 255.0  # 이미지 정규화
        img = np.expand_dims(img, axis=0)  # 배치 차원 추가
        predictions = self.model.predict(img)
        pred_class = np.argmax(predictions, axis=1)
        class_index = np.argmax(predictions[0])  # 가장 높은 확률을 가진 클래스 인덱스
        confidence = predictions[0][class_index]  # 분류 확률
        result = class_label[pred_class[0]]
        result = {
            'class_label': result,
            'confidence': confidence,
            #'image_path': os.path.join(settings.MEDIA_URL, 'images'),
        }
        return result
    def get_class_label(self, class_index):
        # 클래스 레이블을 반환하는 로직을 구현해야 합니다.
        # 예: 클래스 레이블이 저장된 딕셔너리나 데이터베이스에서 조회하여 반환하는 코드를 작성합니다.
        pass
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    def __str__(self):
        return self.title