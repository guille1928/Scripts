import smtplib  #importo para enviar email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from selenium import webdriver

#3 lineas puestas para buscar compatibilidad, me da probelasm por que en el nas no debo de usar brave o similares.. 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#creamos funcion para enviar email 
def enviarEmail (precio):

 # Datos de tu cuenta de Gmail
    sender_email = "email para el envio"
    sender_password = "password de terceros para el email de envio"
    receiver_email = "email para recibir el email"
      
  

        # Crear el mensaje
    subject = "¡Alerta de precio!"
    body = f"El precio del producto ha bajado {precio} ¡Es el momento de comprar!"
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    # Añadir el cuerpo del mensaje con codificación UTF-8
    msg = MIMEText(body, 'plain', 'utf-8')
    message.attach(msg)

    try:
        # Conectar al servidor SMTP de Gmail
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
        print("Correo enviado exitosamente")
    except Exception as e:
        print(f"No se pudo enviar el correo: {e}")

# Configurar las opciones de Selenium para usar Brave en el propio pc
options = Options()
options.binary_location = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"

options.add_argument("--headless")  # Sin interfaz gráfica
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)


# Abrir la URL del producto
url = "https://www.amazon.es/Philips-Recortadora-Afeitadora-Longitudes-QP2824/dp/B0DCFYVR1Z/ref=sr_1_2?sr=8-2"
url2 = "https://www.amazon.es/Philips-OneBlade-360-Maquinilla-Afeitadora/dp/B0C815WY3Z/ref=pd_vtp_d_sccl_3_5/262-4247595-7957624?psc=1"
url3 = "https://www.google.com"
driver.get(url2)

# Espera para asegurar que la página se cargue completamente
driver.implicitly_wait(10)

# Esperar a que el botón de aceptar cookies esté presente (ajustar el selector si es necesario)
try:
    accept_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.ID, 'sp-cc-accept'))   # Usar el ID del botón de aceptación de cookies
    )
    accept_button.click()  # Hacer clic en el botón de aceptación
    print("Cookies aceptadas")

except Exception as e:
    print("No se pudo aceptar las cookies automáticamente:", e)

# Espera para asegurar que el precio haya cargado
try:
  # Obtener parte entera
    price_integer = driver.find_element(By.CLASS_NAME, 'a-price-whole')

    # Obtener decimales
    price_decimal = driver.find_element(By.CLASS_NAME, 'a-price-decimal')

    # Obtener el símbolo de la moneda
    price_symbol = driver.find_element(By.CLASS_NAME, 'a-price-symbol')

    # Imprimir el precio completo
    print(f"El precio es: {price_integer.text}{price_decimal.text}{price_symbol.text}")
    precioTotal =  float(f"{price_integer.text}{price_decimal.text.replace(',', '.')}")
    #genero el precio maximo para realizar una comparacion  
    precioMax = 54 
    #si el precio leido de la web es menor al precio maximo nos envia un email 
    if precioTotal < precioMax : 
        enviarEmail(precioTotal)
    else :
        print ("El precio esta alto")
       
except Exception as e:
    print ("No se encontró el precio:", e)
# Cerrar el navegador después de obtener la información
driver.quit()