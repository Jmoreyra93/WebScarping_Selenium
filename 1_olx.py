"""
OBJETIVO: 
    - Extraer el precio y el titulo de los anuncios en la pagina de OLX autos.
    - Realizar extracciones que requieran una accion de click para cargar datos.
    - Introducirnos a la logica de Selenium
CREADO POR: MOREYRA JUULIÁN
ULTIMA VEZ EDITADO: 24 MARZO 2022
"""

#####
### ATENCION: OLX necesita que le demos permisos de geolocalizacion al navegador de selenium para que nos muestre los datos
### Esto lo haremos una unica vez en la primer corrida del programa. Este problema es mas comun en usuarios de MAC
#####
import random
from time import sleep
from selenium import webdriver

# Instancio el driver de selenium que va a controlar el navegador
# A partir de este objeto voy a realizar el web scraping e interacciones
driver = webdriver.Chrome('./chromedriver.exe')
# Voy a la pagina que requiero
driver.get('https://www.olx.com.ec/autos_c378')
sleep(3)
# Solucion de un bug extraño en Windows en donde los anuncios solo cargan al hacerle refresh o al darle click a algun elemento
driver.refresh()
# Esperamos que cargue el boton
sleep(5)
# Busco el boton para cargar mas informacion
boton = driver.find_element_by_xpath('//button[@data-aut-id="btnLoadMore"]')
# Voy a darle click en cargar mas 3 veces
for i in range(3):
    try:
        # le doy click
        boton.click()
        # espero que cargue la informacion dinamica
        sleep(random.uniform(8.0, 10.0))
        # busco el boton nuevamente para darle click en la siguiente iteracion
        boton = driver.find_element_by_xpath('//button[@data-aut-id="btnLoadMore"]')
    except:
        # si hay algun error, rompo el lazo. No me complico.
        break

# Encuentro cual es el XPATH de cada elemento donde esta la informacion que quiero extraer
# Esto es una LISTA. Por eso el metodo esta en plural
autos = driver.find_elements_by_xpath('//li[@data-aut-id="itemBox"]')


# Recorro cada uno de los anuncios que he encontrado
for auto in autos:
    # Por cada anuncio hallo el precio
    precio = auto.find_element_by_xpath('.//span[@data-aut-id="itemPrice"]').text
    print(precio)
    # Por cada anuncio hallo la descripcion
    descripcion = auto.find_element_by_xpath('.//span[@data-aut-id="itemTitle"]').text
    print(descripcion)
