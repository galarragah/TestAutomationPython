from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

opciones = Options()

#ENVIAR ARGUMENTOS (1 PERMITIENDO LA NOTIFICACION / 2 BLOQUEAN LA NOTIFICACION)

opciones.add_experimental_option("prefs",{
    "profile.default_content_setting_values.notifications" : 2
})

driver = webdriver.Chrome("chromedriver.exe", options=opciones)
driver.get('https://developer.mozilla.org/es/docs/Web/API/notification')
time.sleep(3)