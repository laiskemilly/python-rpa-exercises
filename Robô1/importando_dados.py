import time 
from selenium import webdriver as opcoes_selenium_aula
from selenium.webdriver.common.keys import Keys

import pyautogui as TempoPausaComputador
import pyautogui as teclasAtalho 

from selenium.webdriver.common.by import By

meuNavegador = opcoes_selenium_aula.Chrome()
meuNavegador.get("https://google.com.br")

TempoPausaComputador.sleep(4)
meuNavegador.find_element(By.NAME,"q").send_keys("Dolar hoje")

TempoPausaComputador.sleep(2)
meuNavegador.find_element(By.NAME,"q").send_keys(Keys.RETURN)

TempoPausaComputador.sleep(2)
valorDolar = meuNavegador.find_elements(By.XPATH,'//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')[0].text 
print(valorDolar)

#-------------------------------------------------------------------------------------------------------------------------------------------#
TempoPausaComputador.sleep(2)
meuNavegador.find_element(By.NAME,"q").send_keys()

teclasAtalho.press('tab')

TempoPausaComputador.sleep(2)
teclasAtalho.press('enter')

meuNavegador.find_element(By.NAME,"q").send_keys("Euro hoje")
TempoPausaComputador.sleep(2)
meuNavegador.find_element(By.NAME,"q").send_keys(Keys.RETURN)

TempoPausaComputador.sleep(2)
valorEuro = meuNavegador.find_elements(By.XPATH,'//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')[0].text 
print(valorEuro)

#----------------------------------------------------------------------------------------------------------------------------------------------#

import xlsxwriter
import os

caminhoArquivo = "C:\\Users\\lais\\OneDrive\\Área de Trabalho\\Curso Python\\Python com RPA\\rpa\\robo2\extraindo_arquivos_excel\\Dolar e Euro Google.xlsx"
planilhaCriada = xlsxwriter.Workbook(caminhoArquivo)
sheet1 = planilhaCriada.add_worksheet()

sheet1.write("A1", "Dolar")
sheet1.write("B1", "Euro")
sheet1.write("A2", valorDolar)
sheet1.write("B2", valorEuro)

valorDolar = valorDolar.replace(",",".")
valorEuro = valorEuro.replace(",",".")

valorDolar_float = float(valorDolar)
valorEuro_float = float(valorEuro)

sheet1.write("A3", valorDolar_float)
sheet1.write("B3", valorEuro_float)
planilhaCriada.close()


os.startfile(caminhoArquivo) #abre o arquivo

time.sleep(10)
