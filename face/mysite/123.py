import face_recognition
import os
import matplotlib.image as img
import matplotlib.pyplot as pp
import numpy as np

images = os.listdir('images')
image_to_be_matched = face_recognition.load_image_file('123.jpg')
image_to_be_matched_encoded = face_recognition.face_encodings(image_to_be_matched)[0]
best_match_distance = 1
best_match_image = None

for image in images:
    current_image = face_recognition.load_image_file(os.path.join("images", image))
    current_image_encoded = face_recognition.face_encodings(current_image)
    
    # numpy 배열로 변환
    current_image_encoded = np.array(current_image_encoded)

    result = face_recognition.compare_faces(np.array([image_to_be_matched_encoded]), current_image_encoded)
    if result[0] == True :
        print("당신이 닮은 연예인은 : " + image + "입니다.")
        fileName = "images/" + image
        ndarray = img.imread(fileName)
        pp.imshow(ndarray)
        pp.show()
        break
