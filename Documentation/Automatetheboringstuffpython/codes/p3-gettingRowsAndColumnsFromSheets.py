import openpyxl
import numpy as np
import matplotlib.pyplot as pl

wb = openpyxl.load_workbook('example.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')
sheet1 = sheet['A1':'C3']
print(tuple(sheet['A1':'C3']))
print(sheet.max_row)
for rowOfCellObjects in sheet['A1':'C3']:
    for cellObj in rowOfCellObjects:
        print(cellObj.coordinate, cellObj.value)
    print('--- END OF ROW ---')

#solo imprimiremos la columna B
sheet = wb.get_active_sheet()
print(list(sheet.columns)[1])
print(sheet['B'])

x = []
y = []
for cellObj1 in sheet['B']:
    print(cellObj1.value)
    x.append(cellObj1.value)

print(x)
for cellObj1 in list(sheet.columns)[2]:
    print(cellObj1.value)
    y.append(cellObj1.value)

y = np.array(y)
pl.plot(y)
pl.show()
