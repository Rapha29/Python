import cv2
import os
import numpy as np

def webcan():
    classificador = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    camera = cv2.VideoCapture(0)
    amostra = 1
    nome = input('Digite o Nome da Pessoa')
    while True:
        success,img = camera.read()
        imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = classificador.detectMultiScale(imgGray,scaleFactor=1.5,minSize=(50,50))
        for (x,y,l,a) in faces:
            cv2.rectangle(img, (x, y), (x + l, y + a), (1, 237, 0), 2)
            if cv2.waitKey(1) & 0xFF ==ord('q'):
                imgFace = cv2.resize(imgGray[y:y + a, x:x + l],(220,220))
                cv2.imwrite("fotos/" + nome + str(amostra) + ".jpg",imgFace)
                amostra +=1

        cv2.imshow('img',img)
        cv2.imshow('img', imgGray)
        cv2.waitKey(1)

    camera.release()
    cv2.destroyAllWindows()



webcan()