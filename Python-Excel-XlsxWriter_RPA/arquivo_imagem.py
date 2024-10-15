import xlsxwriter  
import os #abre o arquivo excel

caminho_arquivo = 'imagem_arquivo.xlsx'
workbook = xlsxwriter.Workbook(caminho_arquivo)
sheet_dados = workbook.add_worksheet()



sheet_dados.write("B3", "Imagem Logo GitHub")
sheet_dados.insert_image('B5','C:\\Users\\lais\\OneDrive\Área de Trabalho\\Curso Python\\Python com RPA\\rpa\\Python Excel\\github_logo.png', {'x_scale': 0.2, 'y_scale': 0.2})

#fechando arquivo
workbook.close()

#abrindo arquivo
os.startfile(caminho_arquivo)