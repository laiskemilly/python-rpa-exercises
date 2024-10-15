import xlsxwriter  
import os #abre o arquivo excel

caminho_arquivo = 'formulas.xlsx'
workbook = xlsxwriter.Workbook(caminho_arquivo)
sheet_dados = workbook.add_worksheet("Dados")


#adicionando títulos na sheet
sheet_dados.write("A1", "Número 1")
sheet_dados.write("B1", "Número 2")
sheet_dados.write("C1", "Fórmula")

#adicionando valores na coluna A
sheet_dados.write("A2", 4)
sheet_dados.write("A3", 6)
sheet_dados.write("A4", 7)
sheet_dados.write("A5", 16)
sheet_dados.write("A8", "Lais")

#adicionando valores na coluna B
sheet_dados.write("B2", 9)
sheet_dados.write("B3", 3)
sheet_dados.write("B4", 5)
sheet_dados.write("B5", 2)
sheet_dados.write("B8", "Azevedo")

#adicionando fórmulas na coluna C
sheet_dados.write_formula("C2", "=A2+B2")
sheet_dados.write_formula("C3", "=A3-B3")
sheet_dados.write_formula("C4", "=A4*B4")
sheet_dados.write_formula("C5", "=A5/B5")
sheet_dados.write_formula("C8", '=CONCATENATE(A8," ",B8)')

#alterando o tamanho das colunas 
sheet_dados.set_column('A:C', 15)

#fechando arquivo
workbook.close()

#abrindo arquivo
os.startfile(caminho_arquivo)