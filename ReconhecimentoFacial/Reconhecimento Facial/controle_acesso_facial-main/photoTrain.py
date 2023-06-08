import cv2
import os

import numpy as np

eigenface = cv2.face.EigenFaceRecognizer_create(threshold=10000)
# eigenface = cv2.face.EigenFaceRecognizer_create(num_components=50,threshold=5)
fisherface = cv2.face.FisherFaceRecognizer_create()
lbph = cv2.face.LBPHFaceRecognizer_create()

def getImagem():
    caminhos = [os.path.join('fotos',f) for f in os.listdir('fotos')]
    #print(caminhos)
    faces = []
    ids = []
    for caminho in caminhos:
        imagemFace = cv2.imread(caminho)
        imagemFace = cv2.cvtColor(imagemFace, cv2.COLOR_BGR2GRAY)
        faces.append(imagemFace)
        if "wellington" in caminho:
            ids.append(1)
        elif "susa" in caminho:
            ids.append(2)

    return np.array(ids),faces

id, faces = getImagem()
print('treinando ....')
eigenface.train(faces,id)
eigenface.write('classificadorEigen.yml')

fisherface.train(faces,id)
fisherface.write('classificadorFisher.yml')

lbph.train(faces,id)
lbph.write('classificadorLBPH.yml')

print('tremento realizado')