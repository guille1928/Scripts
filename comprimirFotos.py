#para comprimir unas imagenes en macos, vienen en formato jpg normalmente, y meter en otra carpeta redimensionandolas


import os
from PIL import Image

#creo los 2 directorios para controlar la importacion de fotos

directorioRaiz = "/Users/guille/Desktop/ScriptFotoClau/carpeta1"
directorioFinal = "/Users/guille/Desktop/ScriptFotoClau/carpetaFinal"

ruta_completa = os.listdir(directorioRaiz)

extension_foto = ".jpg",".png",".jpeg"


#funcion para redimensionar la imagen respetando relacion aspecto

def redimensionar_relacion (imagen, alto, ancho) :
    #obtengo las dimensiones originales
    image_ancho , image_alto = imagen.size

 # Calcular la relación de aspecto
    relacion = min(ancho/image_ancho  , alto/image_alto)

    #nueva size
    new_size_respetando_ancho = int(image_ancho*relacion)
    new_size_respetando_alto = int(image_alto*relacion)
    imagen_modificada = imagen.resize((new_size_respetando_ancho,new_size_respetando_alto), Image.LANCZOS)
    # Crear una imagen nueva con fondo blanco y las dimensiones finales
    nueva_imagen = Image.new("RGB", (ancho, alto), (255,255,255))  # Fondo blanco
    
    # Pegar la imagen redimensionada en el centro de la nueva imagen
    nueva_imagen.paste(imagen_modificada, ((ancho - new_size_respetando_ancho) // 2, (alto - new_size_respetando_alto) // 2))
    return nueva_imagen

for archivos in ruta_completa :
    print("las fotos son : ",archivos)
    ruta_origen = os.path.join(directorioRaiz,archivos)
    ruta_salida = os.path.join(directorioFinal,archivos)
    ruta_salida = os.path.splitext(ruta_salida)[0] + ".png"
    img= Image.open(ruta_origen)
    img_redimensionada= redimensionar_relacion(img,264,414)
    img_redimensionada.save(ruta_salida, format="PNG")
   