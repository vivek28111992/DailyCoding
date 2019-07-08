import os
import datetime
from random import randint
from xlrd import open_workbook
from xlutils.copy import copy


def fillAttendance(file):

    filePath = '/'.join(os.getcwd().split('/')[:3]) + '/Downloads'
    wb = open_workbook(filePath + '/' + file)
    wbNew = copy(wb)

    sheetToEdit = wbNew.get_sheet(0)

    sheet = wb.sheet_by_index(0)

    # Extracting number of rows
    # print(sheet.nrows)

    # Extracting number of columns
    # print(sheet.ncols)

    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    holidaysTaken = [19]

    for i in range(sheet.nrows):
        firstCellValue = sheet.cell_value(i, 0)

        if firstCellValue != '' or i == 21:

            if i == 0:
                sheetToEdit.write(i, 1, 'Vivek Pawar')
            elif i == 1:
                sheetToEdit.write(i, 1, 'Mahindra Logistics')
            elif i == 2:
                sheetToEdit.write(i, 1, 'Goregaon West (Mumbai)')
            elif firstCellValue in days:
                for j in range(1, sheet.ncols, 3):
                    cellValue = sheet.cell_value(i, j)
                    cellValue1 = sheet.cell_value(i, j+1)
                    if cellValue != '' and cellValue1 != 'Holiday' and cellValue not in holidaysTaken:
                        randomInTime = str(datetime.datetime.now().replace(hour=randint(10, 10), minute=randint(0, 40)).time())[0:5]
                        sheetToEdit.write(i, j+1, randomInTime + ' am')
                        randomOutTime = str(datetime.datetime.now().replace(hour=randint(19, 20), minute=randint(0, 59)).time())[0:5]
                        sheetToEdit.write(i, j+2, randomOutTime + ' pm')
                    elif cellValue in holidaysTaken:
                        sheetToEdit.write(i, j+1, 'Holiday')
            elif i == 17:
                sheetToEdit.write(i-1, 0, 'Rahul Divekar')
                sheetToEdit.write(i-1, 12, 'Vivek Pawar')
            elif i == 21:
                sheetToEdit.write(i, 13, '77060')

    wbNew.save(file)


if __name__ == '__main__':
    fileName = input('Please enter the file name: ')
    fillAttendance(fileName)