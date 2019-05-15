import csv
import pandas as pd

class Comparision():
    def __init__(self):
        self.one = 'path_file_one'
        self.two = 'path_file_two'

    def comp(self):
        dataone = []
        datatwo = []
        with open(self.one, 'rt') as fone:
            data = csv.reader(fone)
            for row in data:
                dataone.append(row)

        with open(self.two, 'rt') as ftwo:
            data = csv.reader(ftwo)
            for row in data:
                datatwo.append(row)

        error = {}
        error['row'] = []
        error['column'] = []

        for i in range(len(dataone)):
            for j in range(len(dataone[i])):
                if dataone[i][j].lower() == datatwo[i][j].lower():
                    pass
                else:
                    error['row'].append(i)
                    error['column'].append(j)

        df_error = pd.DataFrame(error)
        return df_error[["row", "column"]]

if __name__ == '__main__':
    obj = Comparision()
    x = obj.comp()
    print(x)