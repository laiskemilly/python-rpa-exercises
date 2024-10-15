import xlsxwriter  
import os #abre o arquivo excel

caminho_arquivo = 'graficos.xlsx'
workbook = xlsxwriter.Workbook(caminho_arquivo)
sheet_dados = workbook.add_worksheet("Resumo")

linha_bold = workbook.add_format({'bold': 1})

#Dados da planilha
titulos = ['Vendedores', 'Total Vendas']
dados_tabela = [
    ["Ana", "Maria", "Pedro", "João", "Mariana"],
    [200, 132, 203, 165, 201]
]

#escrevendo os dados na planilha
sheet_dados.write_row('A1', titulos, linha_bold)
sheet_dados.write_column('A2', dados_tabela[0])
sheet_dados.write_column('B2', dados_tabela[1])

#criando um gráfico de colunas
grafico_colunas = workbook.add_chart({'type': 'column'})

#configurando as séries
grafico_colunas.add_series({
    'name': '=Resumo!$B$1',
    'categories': '=Resumo!$A$2:$A$6',
    'values': '=Resumo!$B$2:$B$6'
})

#adicionando título no gráfico e alguns rótulos do eixo
grafico_colunas.set_title({'name': 'Gráfico Total de Vendas'})
grafico_colunas.set_x_axis({'name': 'Vendedores'})
grafico_colunas.set_y_axis({'name': 'Vendas'})

#definindo um estilo de gráfico do excel
grafico_colunas.set_style(11)

#inserindo o gráfico na planilha com os deslocamentos dos eixos x e y
sheet_dados.insert_chart('D2', grafico_colunas, {'x_offset': 25, 'y_offset': 10})

#------------------------------------------------------------------------------------------------------------------#

#criando um gráfico empilhado
grafico_empilhado = workbook.add_chart({'type': 'area', 'subtype': 'stacked'}) #stacked significa que o gráfico será empilhado

#configurando as séries
grafico_empilhado.add_series({
    'name': '=Resumo!$B$1',
    'categories': '=Resumo!$A$2:$A$6',
    'values': '=Resumo!$B$2:$B$6'
})

#adicionando título no gráfico e alguns rótulos do eixo
grafico_empilhado.set_title({'name': 'Gráfico Empilhado'})
grafico_empilhado.set_x_axis({'name': 'Funcionários'})
grafico_empilhado.set_y_axis({'name': 'Vendas'})

#definindo um estilo de gráfico do excel
grafico_empilhado.set_style(12)

#inserindo o gráfico na planilha com os deslocamentos dos eixos x e y
sheet_dados.insert_chart('L2', grafico_empilhado, {'x_offset': 25, 'y_offset': 10})

#fechando arquivo
workbook.close()

#abrindo arquivo
os.startfile(caminho_arquivo)

#Os estilos de gráficos que podem ser utilizados podemser encontrados na documentação do XlsxWriter e do Microsoft Excel
#https://support.microsoft.com/pt-br/office/tipos-de-gr%C3%A1fico-dispon%C3%ADveis-no-office-a6187218-807e-4103-9e0a-27cdb19afb90 
#https://xlsxwriter.readthedocs.io/chart.html#chart-styles
