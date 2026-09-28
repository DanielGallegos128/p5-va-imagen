import cv2
# Leer la imagen con CV2 = Computer Vision
img = cv2.imread('perro.jpg')
# Determinar el tipo de imagen numpy.ndarray
print(type(img))
# Mostrar pixeles (447, 447, 3)
print(img.shape)
# Mostrando imagen en en ventana barra de titulo perro 1392
cv2.imshow('perro 1392', img)
## Tiempo de espera
cv2.waitKey(0)
# Destruit todas las ventanas
cv2.destroyAllWindows()