# Binarización híbrida para segmentación de hojas de cafeto (Gaussian + Otsu)

Este repositorio contiene el algoritmo de binarización híbrida (suavizado Gaussiano + umbralización de Otsu) aplicado a imágenes de hojas de cafeto, con el objetivo de mejorar la segmentación bajo condiciones de iluminación variable y apoyar el análisis de deficiencias nutricionales.

## Contenido del repositorio
## Contenido del repositorio
- [`algoritmo_binarizacion_hibrida.py`](algoritmo_binarizacion_hibrida.py): implementación del algoritmo en Python.
- [`Articulo.pdf`](Articulo.pdf): artículo del proyecto.
- [`PROYECTO VISION ARTIFICIAL.pdf`](PROYECTO%20VISION%20ARTIFICIAL.pdf): informe del proyecto.
  

## Resumen del método
1. Lectura de la imagen
2. Conversión a escala de grises
3. Suavizado con filtro Gaussiano (reduce ruido)
4. Umbralización automática con Otsu (genera máscara binaria)
5. Visualización de resultados (original, gris, binaria)

## Resultados (según el artículo)
El enfoque reporta desempeño con métricas como **PSNR** e **IoU** (ver detalles en `Articulo.pdf`).

## Autor
Kevin Santiago Quimbaya Andrade  
GitHub: https://github.com/Naivelk
