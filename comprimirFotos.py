#para comprimir unas imagenes en macos, vienen en formato jpg normalmente, y meter en otra carpeta redimensionandolas


import os
from PIL import Image

#creo los 2 directorios para controlar la importacion de fotos

directorioRaiz = "/Users/guille/Desktop/ScriptFotoClau/carpeta1"
directorioFinal = "/Users/guille/Desktop/ScriptFotoClau/carpetaFinal"

ruta_completa = os.listdir(directorioRaiz)

extension_foto = ".jpg",".png",".jpeg"

for archivos in ruta_completa :
    print("las fotos son : ",archivos)
    ruta_origen = os.path.join(directorioRaiz,archivos)
    ruta_salida = os.path.join(directorioFinal,archivos)
    img= Image.open(ruta_origen)
    img_resized = img.resize((208,123))
    img_resized.save(ruta_salida)