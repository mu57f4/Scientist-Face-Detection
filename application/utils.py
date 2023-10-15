import numpy as np
import cv2
import joblib
import json


# load our artifcats
__model = joblib.load('application/artifacts/svm_model.pkl')
with open('application/artifacts/class_dictionary.json') as class_file:
    __class_dict = json.load(class_file)


def read_image(uploaded_file):
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, 1)
        return image


def preprocess_image(image):
    face_cascade = cv2.CascadeClassifier('application/artifacts/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('application/artifacts/haarcascade_eye.xml')

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    cropped_faces = []
    for (x,y,w,h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = image[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        if len(eyes) >= 2:
            cropped_faces.append(roi_color)
    
    X = []
    for face_image in cropped_faces:
        IMAGE_SIZE = (64, 64)
        # Resize image
        resized_image = cv2.resize(face_image, IMAGE_SIZE)
        # reshape for the model
        X.append(resized_image)
    
    X = np.array(X).reshape(len(X), 64*64*3).astype(float)
    if len(X) < 2:
        X = X.reshape(1, -1)
    return X

def predict(X):
    y = __model.predict(X)[0]
    y_class = list(__class_dict.keys())[y]
    y_probability = np.around(__model.predict_proba(X)*100,2).tolist()[0]
    return y_class, y_probability[y]