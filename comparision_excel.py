import pandas as pd
import xlrd

class Comparision():
    def __init__(self):
        self.one = 'file_path_one'
        self.two = 'file_path_two'

    def comp(self):
        wbone = xlrd.open_workbook(self.one)
        sheetone = wbone.sheet_by_index(0)

        wbtwo = xlrd.open_workbook(self.two)
        sheettwo = wbtwo.sheet_by_index(0)

        error = {}
        error['row'] = []
        error['column'] = []

        for i in range(sheetone.nrows):
            for j in range(sheetone.ncols):
                if str(sheetone.cell_value(i, j)).lower() == str(sheettwo.cell_value(i, j)).lower():
                    pass
                else:
                    error['row'].append(i)
                    error['column'].append(j)

        df_error = pd.DataFrame(error)
        return df_error[["row", "column"]]

if __name__ == '__main__':
    obj = Comparision()
    res = obj.comp()
    print(res)