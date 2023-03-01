import openpyxl

wb= openpyxl.load_wordbook('sample_file.xlsx')

sheet = wb.activate

x1 = sheet['A1']
x2 = sheet['A2']
#usa cell() como funcion
x3 = sheet.cell(row=3, column=1)

Imprimir ("El valor de la primera celda:"
