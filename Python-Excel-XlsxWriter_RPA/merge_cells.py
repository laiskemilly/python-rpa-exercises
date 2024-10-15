import xlsxwriter  
import os #abre o arquivo excel

caminho_arquivo = 'merge_cells.xlsx'
workbook = xlsxwriter.Workbook(caminho_arquivo)
sheet_dados = workbook.add_worksheet()


#formatando as células
add_merge_cells = workbook.add_format({
    'bold': True,
    'border': 6, 
    'align': 'center', #alinhamento horizontal
    'valign': 'vcenter', #alinhamento vertical
    'fg_color': 'pink',
    'font_color': 'white',
    'size': 30
})

sheet_dados.merge_range('B3:I5', 'Test Merge Cells', add_merge_cells)

#fechando arquivo
workbook.close()

#abrindo arquivo
os.startfile(caminho_arquivo)