# librerias
import pandas as pd
import numpy as np
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
import requests
import os


# variables
variables = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
            "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
            "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4",
            "5", "6", "7", "8", "9", "0"]

# funcion aleatorio
def aleatorio():
    result = random.randint(0, 35)
    return result

# generar texto plano dinamico
codigo = []
iteraciones = 1000000

for i in range(0, iteraciones):
    add = variables[aleatorio()]
    codigo.append(add)
    #print(i, x, add)

# creando codigos a insertar
resultado = ""
resultado_final = resultado.join(codigo)
codigo_usar = []

for i in range(0, len(codigo), 9):
    if i > 9:
        hack = "L" + resultado_final[i-9:i]
        codigo_usar.append(hack)

    else:
        pass
print('codigos creados: ', len(codigo_usar))        

# abrir navegador
# ruta driver
path_driver = "./chromedriver.exe"

# opciones de driver
option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 2 
})

# definir driver
print("abriendo navegador")
driver = webdriver.Chrome(chrome_options=option, executable_path=path_driver)
driver.set_window_size(1600, 1024)

# definir web
print("ingresando a sitio")
driver.get("https://elbotindelays.cl/")

# boton inicio sesion
print("click boton inicio sesion")
boton_inicio_sesion = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[class='btn btn--red']"))).click()

# datos de usuario
print("ingresando datos de usuario")
input_email = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
input_email.clear()
input_email.send_keys('email@gmail.com')
input_rut = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='rut']")))
input_rut.clear()
input_rut.send_keys('111111111')
boton_ingresar = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='btn btn--yellow']"))).click()

# cambio de sitio a ingresar codigo
print("cambiando de pagina")
driver.get("https://elbotindelays.cl/codigo")

# ciclo actualizar pagina e inyectar codigo
# probando 100 veces
for i in range(0, 100):
    driver.get("https://elbotindelays.cl/codigo")

    # ingresar codigo
    input_codigo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='code']")))
    input_codigo.clear()
    print('intento: ', i, 'usando el codigo: ', codigo_usar[i])
    input_codigo.send_keys(codigo_usar[i])

    #click en ingresar codigo
    boton_ingresar_codigo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='square square--black']"))).click()

    time.sleep(2)
    
# cerrar driver
print("cerrando navegador")
driver.quit()
