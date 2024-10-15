import xlsxwriter  
import os #abre o arquivo excel

caminho_arquivo = 'formatacao_condicional_icones.xlsx'
workbook = xlsxwriter.Workbook(caminho_arquivo)
sheet_dados = workbook.add_worksheet()

insert_dados = [["Coluna 1", "Coluna 2", "Coluna 3", "Coluna 4"],
                 [10, 16, 90, 54],
                 [23, 51, 64, 15],
                 [73, 18, 49, 63],
                 [13, 19, 67, 94],
                 [53, 75, 32, 98] ]

sheet_dados.write('A1', "Exemplos de Formatação Condicional com conjunto de icones")

for linha , range in enumerate(insert_dados):
    sheet_dados.write_row(linha + 2, 1, range) #linha 3, coluna 2

sheet_dados.conditional_format('B4:E4', {
    'type': 'icon_set',
    'icon_style': '3_traffic_lights'})

sheet_dados.conditional_format('B5:E5', {
    'type': 'icon_set',
    'icon_style': '3_traffic_lights',
    'reverse_icons': True
})

sheet_dados.conditional_format('B6:E6', {
    'type': 'icon_set',
    'icon_style': '3_arrows'
})

sheet_dados.conditional_format('B7:E7', {
    'type': 'icon_set',
    'icon_style': '4_arrows'
})

sheet_dados.conditional_format('B8:E8', {
    'type': 'icon_set',
    'icon_style': '5_ratings'
})


#fechando arquivo
workbook.close()

#abrindo arquivo
os.startfile(caminho_arquivo)