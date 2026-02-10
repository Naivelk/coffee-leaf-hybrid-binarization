
import cv2
import numpy as np
import matplotlib.pyplot as plt

def binarizacion_hibrida(imagen_path, redimension=(224, 224), sigma=1.5, kernel=(5, 5)):
    # 1. Cargar la imagen en color
    imagen_rgb = cv2.imread(imagen_path)
    imagen_rgb = cv2.cvtColor(imagen_rgb, cv2.COLOR_BGR2RGB)

    # 2. Redimensionar la imagen
    imagen_rgb = cv2.resize(imagen_rgb, redimension)

    # 3. Convertir a escala de grises
    gris = cv2.cvtColor(imagen_rgb, cv2.COLOR_RGB2GRAY)

    # 4. Aplicar filtro Gaussiano
    suavizada = cv2.GaussianBlur(gris, kernel, sigma)

    # 5. Aplicar binarización con Otsu
    _, binaria = cv2.threshold(suavizada, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # 6. Mostrar resultados
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    axes[0].imshow(imagen_rgb)
    axes[0].set_title("Imagen Original")
    axes[0].axis("off")

    axes[1].imshow(gris, cmap='gray')
    axes[1].set_title("Escala de Grises")
    axes[1].axis("off")

    axes[2].imshow(binaria, cmap='gray')
    axes[2].set_title("Binarización Híbrida")
    axes[2].axis("off")

    plt.tight_layout()
    plt.show()

    return binaria

# Ejemplo de uso:
# binarizacion_hibrida('ruta/a/una/imagen.jpg')
