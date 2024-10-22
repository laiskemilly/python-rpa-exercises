from openpyxl import load_workbook
import os

caminho_arquivo =  'InserirDados.xlsx'
planilha_aberta = load_workbook(filename=caminho_arquivo)

sheet_selecionada = planilha_aberta['Aluno']

dados_tabela = [
    ['Nome', 'Idade'],
    ['Ana', 18],
    ['João', 16],
    ['Gabriel', 26],
    ['Julia', 25],
    ['Maria', 29]
]

for linha_planilha in dados_tabela:
    sheet_selecionada.append(linha_planilha)

planilha_aberta.save(filename=caminho_arquivo)

os.startfile(caminho_arquivo)