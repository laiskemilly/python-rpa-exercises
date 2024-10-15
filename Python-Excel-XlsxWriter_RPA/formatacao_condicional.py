import xlsxwriter  
import os #abre o arquivo excel

caminho_arquivo = 'formatacao_condicional.xlsx'
workbook = xlsxwriter.Workbook(caminho_arquivo)
sheet_dados = workbook.add_worksheet()

formato_maior = workbook.add_format({
    'bg_color': 'green',
    'font_color': 'white'
})


formato_menor = workbook.add_format({
    'bg_color': 'red',
    'font_color': 'white'
})

insert_dados = [["Coluna 1", "Coluna 2", "Coluna 3", "Coluna 4"],
                 [10, 16, 90, 54],
                 [23, 51, 64, 15],
                 [73, 18, 49, 63] ]

sheet_dados.write('A1', "Valores >= 50 estão verdes e valores < 50 estão vermelhos")

for linha , range in enumerate(insert_dados):
    sheet_dados.write_row(linha + 2, 1, range) #linha 3, coluna 2

#condição para pintar os valores maior ou igual a 50 de verde
sheet_dados.conditional_format('B4:E6', {
    'type': 'cell',
    'criteria': '>=',
    'value': 50,
    'format': formato_maior
})

#condição para pintar os valores menor que 50 de vermelho
sheet_dados.conditional_format('B4:E6', {
    'type': 'cell',
    'criteria': '<',
    'value': 50,
    'format': formato_menor
})

#fechando arquivo
workbook.close()

#abrindo arquivo
os.startfile(caminho_arquivo)