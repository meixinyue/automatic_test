import xlrd, config

class Read_Ex:

    def read_excel(self):
        book = xlrd.open_workbook(config.excelfile)
        table = book.sheet_by_name(config.sheetname)
        row_Num = table.nrows
        col_Num = table.ncols
        httpurl_data = []
        key = table.row_values(0)

        if row_Num <= 1:
            print('没有数据')
        else:
            j = 1
            for i in range(row_Num - 1):
                d = {}
                values = table.row_values(j)

                for x in range(col_Num):
                    d[key[x]] = values[x]

                j += 1
                httpurl_data.append(d)

        return httpurl_data