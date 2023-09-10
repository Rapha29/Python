import cv2

# Carregar a imagem
imagem = cv2.imread("2.png")

# Converter a imagem para escala de cinza
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Aplicar o filtro bilateral para preservar detalhes e suavizar
imagem_suavizada = cv2.bilateralFilter(imagem_cinza, 93, 55, 75)

# Aplicar o filtro Laplacian para realçar os detalhes
imagem_laplacian = cv2.Laplacian(imagem_suavizada, cv2.CV_8U, ksize=3)

# Aplicar o thresholding para obter os tons de cinza
_, imagem_tons_cinza = cv2.threshold(imagem_laplacian, 5, 355, cv2.THRESH_BINARY_INV)

# Exibir a imagem resultante
cv2.imshow("Desenho Realista", imagem_tons_cinza)
cv2.waitKey(0)
cv2.destroyAllWindows()
