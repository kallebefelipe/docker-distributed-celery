import xlrd
from remote import run_extracao_task
from search.steps.insert_process import insert


def read_data(path):
    workbook = xlrd.open_workbook(path, on_demand=True)
    try:
        worksheet = workbook.sheet_by_index(0)
    except xlrd.XLRDError:
        return []
    first_row = []
    for col in range(worksheet.ncols):
        first_row.append(worksheet.cell_value(0, col))
    data = []
    for row in range(1, worksheet.nrows):
        elm = {}
        for col in range(worksheet.ncols):
            cell = worksheet.cell_value(row, col)
            elm[first_row[col]] = cell
        data.append(elm)
    return data


def trat_num(processos):
    new_process = []

    for pro in processos:
        new_process.append(pro.get('numero'))
    return new_process


def run_tasks(collection, path, row_id):
    processos = read_data(path)
    processos = trat_num(processos)

    insert(collection, processos)
    run_extracao_task.delay(collection, processos)
