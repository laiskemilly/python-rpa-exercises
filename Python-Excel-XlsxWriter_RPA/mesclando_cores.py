import xlsxwriter  
import os #abre o arquivo excel

caminho_arquivo = 'mesclando_cores.xlsx'
workbook = xlsxwriter.Workbook(caminho_arquivo)
sheet_dados = workbook.add_worksheet("Dados")


#altera a cor da fonte
cor_fonte = workbook.add_format()
cor_fonte.set_font_color('blue')

#alterando a cor do fundo e da fonte da celula
cor_fonte_e_fundo = workbook.add_format({
    'align': 'center',
    'font_color': 'white',
    'bold': True,
    'bg_color': 'pink'
})

#adicionando dados na sheet
sheet_dados.write("A1", "Nome", cor_fonte_e_fundo)
sheet_dados.write("B1", "Idade", cor_fonte_e_fundo)
sheet_dados.write("A2", "Lais", cor_fonte)
sheet_dados.write("B2", 22, cor_fonte)
sheet_dados.write("A3", "Lorenna", cor_fonte)
sheet_dados.write("B3", 11, cor_fonte)

#fechando arquivo
workbook.close()

#abrindo arquivo
os.startfile(caminho_arquivo)