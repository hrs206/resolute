from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import cv2
from deepface import DeepFace
import uuid
import time
# Create your views here.

imgs = []

def index(request):
    return render(request, "index.html")

def register(request):
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    id1 = uuid.uuid1()
    cv2.imwrite("img"+str(id1)+".jpg", frame)
    cv2.destroyAllWindows()
    cap.release()
    imgs.append("img"+str(id1)+".jpg")
    time.sleep(2)
    return render(request, "register.html")

def recognized(request):
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    id2 = uuid.uuid1()
    cv2.imwrite("img"+str(id2)+".jpg", frame)
    cv2.destroyAllWindows()
    cap.release()
    for img in imgs:
        authentication = DeepFace.verify(img1_path=img, img2_path="img"+str(id2)+".jpg", model_name="Facenet")
        if authentication["verified"]:
            return render(request, "recognized.html")
    
    return render(request, "nrecognized.html")