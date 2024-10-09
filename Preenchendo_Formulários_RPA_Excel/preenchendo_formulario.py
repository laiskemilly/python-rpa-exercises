from selenium import webdriver as opcoes_selenium 
from selenium.webdriver.common.by import By  #o By é utilizado para definir os métodos de localização dos elementos em uma página web
from selenium.webdriver.common.keys import Keys #o Keys é usado para enviar comandos do teclado como Enter, Escape 

import pyautogui as tempo_espera

navegadorFormulario = opcoes_selenium.Chrome()
navegadorFormulario.get("https://pt.surveymonkey.com/r/CTPM5RP")

tempo_espera.sleep(2)

nome = navegadorFormulario.find_element(By.ID, "212207848")
nome.send_keys("Lais")
tempo_espera.sleep(2)

email = navegadorFormulario.find_element(By.ID, "212207937")
email.send_keys("laisteste@gmail.com")
tempo_espera.sleep(2)

telefone = navegadorFormulario.find_element(By.ID, "212207948")
telefone.send_keys("(55) 5555-5555")
tempo_espera.sleep(2)

radio_button = navegadorFormulario.find_element(By.ID, "212208065_1520339727_label")
tempo_espera.sleep(1)
radio_button.click()
tempo_espera.sleep(2)

sobre = navegadorFormulario.find_element(By.ID, "212208216")
sobre.send_keys("Desenvolvedora Python")
tempo_espera.sleep(5)

enviar = navegadorFormulario.find_element(By.XPATH, '//*[@id="patas"]/main/article/section/form/div[2]/button')
#enviar.click()