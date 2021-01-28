from openpyxl import Workbook


def produs_to_excel(test):
    filename = "hello_world.xlsx"
    workbook = Workbook()
    sheet = workbook.active
    sheet.row = 1
    for prod in test:
        sheet.columns = 'A'
        cell = sheet.columns + sheet.row
        sheet[cell] = prod
        sheet.columns += 1
    workbook.save(filename=filename)


test = []
test[1] = 10
test[2] = 15
test[3] = 25

produs_to_excel(test)