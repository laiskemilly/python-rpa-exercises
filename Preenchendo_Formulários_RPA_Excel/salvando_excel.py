from openpyxl import load_workbook  #abre arquivos do excel para trabalhar com eles

from selenium import webdriver as opcoes_selenium 
from selenium.webdriver.common.by import By  #o By é utilizado para definir os métodos de localização dos elementos em uma página web
from selenium.webdriver.support.ui import WebDriverWait  #WebDriverWait permite esperar uma condição específica antes de prosseguir com a execução
from selenium.webdriver.support import expected_conditions as EC  #fornece condições predefinidas para usar junto com o WebDriverWait


nomeCaminhoArquivo = "DadosFormulario.xlsx"
planilha_aberta = load_workbook(filename=nomeCaminhoArquivo)
sheet_selecionada = planilha_aberta['Dados']

for linha in range(2, len(sheet_selecionada['A']) + 1):  #loop for para iterar as linhas da planilha, começando pela segunda linha e ignorando a linha do cabeçalho

    nome = sheet_selecionada[f'A{linha}'].value
    email = sheet_selecionada[f'B{linha}'].value
    telefone = sheet_selecionada[f'C{linha}'].value
    sexo = sheet_selecionada[f'D{linha}'].value
    sobre = sheet_selecionada[f'E{linha}'].value

    navegadorFormulario = opcoes_selenium.Chrome()
    navegadorFormulario.get("https://pt.surveymonkey.com/r/CTPM5RP")

    espera = WebDriverWait(navegadorFormulario, 10)

    campo_nome = espera.until(EC.presence_of_element_located((By.ID, "212207848")))  #EC.presence_of_element_located espera até que o elemento especifico esteja presente na página
    campo_nome.send_keys(nome)

    campo_email= espera.until(EC.presence_of_element_located((By.ID, "212207937")))
    campo_email.send_keys(email)

    campo_telefone = espera.until(EC.presence_of_element_located((By.ID, "212207948")))
    campo_telefone.send_keys(telefone)

    if sexo == "Masculino":
        botao_masculino = espera.until(EC.element_to_be_clickable((By.ID, '212208065_1520339728_label')))
        botao_masculino.click()

    elif sexo == "Feminino":
        botao_feminino = espera.until(EC.element_to_be_clickable((By.ID, '212208065_1520339727_label')))
        botao_feminino.click()
    else:
        botao_outro = espera.until(EC.element_to_be_clickable((By.ID, '212208065_1520339729_label')))
        botao_outro.click()


    campo_sobre = espera.until(EC.presence_of_element_located((By.ID, "212208216")))
    campo_sobre.send_keys(sobre)


    botao_enviar = espera.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="patas"]/main/article/section/form/div[2]/button')))
    #botao_enviar.click()

    print("Formulários Preenchidos.")