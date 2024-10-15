import xlsxwriter  
import os #abre o arquivo excel

caminho_arquivo = 'primeiro_arquivo.xlsx'
workbook = xlsxwriter.Workbook(caminho_arquivo)
sheet_padrao = workbook.add_worksheet()

#adicionando dados na sheet
sheet_padrao.write("A1", "Nome")
sheet_padrao.write("B1", "Idade")
sheet_padrao.write("A2", "Lais")
sheet_padrao.write("B2", 22)
sheet_padrao.write("A3", "Lorenna")
sheet_padrao.write("B3", 11)

#fechando arquivo
workbook.close()

#abrindo arquivo
os.startfile(caminho_arquivo)