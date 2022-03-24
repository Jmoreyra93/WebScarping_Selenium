import random
from time import sleep
from selenium import webdriver

driver = webdriver.Chrome('./chromedriver.exe')

driver.get('https://www.olx.com.ec/autos_c378')

# TODOS LOS ANUNCIOS EN UNA LISTA
autos = driver.find_elements_by_xpath('//li[@data-aut-id="itemBox"]')

for auto in autos:
    precio = auto.find_element_by_xpath('.//span[@data-aut-id="itemPrice"]').text
    print(precio)

    titulo = auto.find_element_by_xpath('.//span[@data-aut-id="itemTitle"]').text
    print(titulo)

