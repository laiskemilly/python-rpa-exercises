from openpyxl import load_workbook
import os

caminho_arquivo =  'DeletarLinhaColuna.xlsx'
planilha_aberta = load_workbook(filename=caminho_arquivo)

sheet_selecionada = planilha_aberta['Aluno']

sheet_selecionada.delete_rows(3)
sheet_selecionada.delete_rows(3)
sheet_selecionada.delete_rows(5)

sheet_selecionada.delete_cols(2)

planilha_aberta.save(filename=caminho_arquivo)

os.startfile(caminho_arquivo)