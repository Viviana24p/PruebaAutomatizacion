import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from datetime import datetime


# Iniciar navegador
driver = webdriver.Chrome()
driver.get("https://www.demoblaze.com/")
time.sleep(3)

# Seleccionar el primer producto y agregarlo al carrito
primer_producto = driver.find_element(By.XPATH, "//a[contains(text(), 'Samsung galaxy s6')]")
primer_producto.click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[contains(text(), 'Add to cart')]").click()
time.sleep(2)

# Aceptar alerta
alert = driver.switch_to.alert
alert.accept()

# Tomar pantallazo después de agregar el primer producto
driver.save_screenshot("01_producto1_agregado.png")

# Volver al home
home = driver.find_element(By.XPATH, "//a[@id='nava']")
home.click()
time.sleep(2)

# Seleccionar el segundo producto y agregarlo al carrito
segundo_producto = driver.find_element(By.XPATH, "//a[contains(text(), 'Nokia lumia 1520')]")
segundo_producto.click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[contains(text(), 'Add to cart')]").click()
time.sleep(2)
alert = driver.switch_to.alert
alert.accept()

# Tomar pantallazo después de agregar el segundo producto
driver.save_screenshot("02_producto2_agregado.png")

# Volver al home
home = driver.find_element(By.XPATH, "//a[@id='nava']")
home.click()
time.sleep(2)

carrito = driver.find_element(By.XPATH, "//a[@id='cartur']")
carrito.click()

# Tomar pantallazo después de agregar el segundo producto
driver.save_screenshot("03_carrito.png")
driver.find_element(By.XPATH, "//button[contains(text(), 'Place Order')]").click()
time.sleep(2)

# Llenar el formulario con datos inventados
driver.find_element(By.ID, "name").send_keys("Vviana Pedraza")
driver.find_element(By.ID, "country").send_keys("Colombia")
driver.find_element(By.ID, "city").send_keys("Fusagasugá")
driver.find_element(By.ID, "card").send_keys("4111111111111111")  
driver.find_element(By.ID, "month").send_keys("12")               
driver.find_element(By.ID, "year").send_keys("2026")              
time.sleep(2)

# Dar clic en comprar
driver.find_element(By.XPATH, "//button[contains(text(), 'Purchase')]").click()
time.sleep(2)

# Tomar pantallazo de la confirmación
driver.save_screenshot("04_confirmacion_compra.png")

# (Opcional) Cerrar el mensaje de confirmación
driver.find_element(By.XPATH, "//button[contains(text(), 'OK')]").click()
time.sleep(1)

# Cerrar navegador
driver.quit()
