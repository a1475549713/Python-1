from time import sleep
import xlrd
import sys
from functools import wraps
import openpyxl
'''
xls文件操作
'''


def excel(xlsname, index=0):
    # xlsnaem :Enter a file name or path
    # index :The sheet is numbered from 0
    def function(fun):
        @wraps(fun)
        def wrapp(*arg, **kwargs):
            try:
                table = xlrd.open_workbook(xlsname)
                sheet = table.sheet_by_index(index)
            except FileNotFoundError:
                print('There is no {} file currently. Exit after 3 seconds'.format(xlsname))
                sleep(3)
                sys.exit()
            lows = sheet.nrows
            cols = sheet.ncols
            # print(lows,cols)
            global data
            data = {}
            for low in range(1, lows):
                for col in range(0, cols):
                    key = sheet.cell(0, col).value
                    value = sheet.cell(low, col).value
                    data[key] = value
                fun(data=data, *arg, **kwargs)
                # return ret
        return wrapp
    return function


