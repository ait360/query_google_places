import xlsxwriter as xls



def create_workbook(entity='', state=''):
    # Create an Excel workbook
    if state:
        xls_filename = state + '.xlsx'

    else:

        xls_filename = f"{entity}.xlsx"

    workbook = xls.Workbook(xls_filename)

    return workbook


def create_worksheet(workbook, data, state):
    """
    Add worksheets to the workbook created
    in the create_workbook function

    :param workbook:    returned by create_workbook
    :param data:        entries
    :param state:       eg 'Abia', 'Lagos'
    :return:
    """

    worksheet = workbook.add_worksheet(state)
    bold = workbook.add_format({ 'bold': True })

    attributes = [('A1','Name'),
				   ('B1','Address'),
                ('C1', 'Phone Number'),
				   ('D1','Latitude'),
				   ('E1','Longitude'),
				   ('F1','Place ID')]
    for col, attr in attributes:
        worksheet.write(col, attr, bold)

    row = 1
    col = 0

    for item in data:
        for index in range(len(item)):
            worksheet.write(row, col + index, item[index])

        row += 1

    print(f'done creating excel sheet for {state}')