import xlsxwriter  
import os #abre o arquivo excel

caminho_arquivo = 'alterando_cores.xlsx'
workbook = xlsxwriter.Workbook(caminho_arquivo)
sheet_dados = workbook.add_worksheet("Dados")

#altera a cor do fundo da célula
cor_fundo = workbook.add_format({'bg_color': 'pink'})
#altera a cor da fonte
cor_fonte = workbook.add_format()
cor_fonte.set_font_color('blue')

#adicionando dados na sheet
sheet_dados.write("A1", "Nome", cor_fundo)
sheet_dados.write("B1", "Idade", cor_fundo)
sheet_dados.write("A2", "Lais", cor_fonte)
sheet_dados.write("B2", 22, cor_fonte)
sheet_dados.write("A3", "Lorenna", cor_fonte)
sheet_dados.write("B3", 11, cor_fonte)

#fechando arquivo
workbook.close()

#abrindo arquivo
os.startfile(caminho_arquivo)