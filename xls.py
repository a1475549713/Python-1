from time import sleep
import xlrd
import sys
from functools import wraps

'''
xls文件操作
'''

# xlsnaem :Enter a file name or path
# index :The sheet is numbered from 0
def excel(xlsname, index=0):
    def function(fun):
        @wraps(fun)
        def wrapp(*arg, **kwargs):
            try:
                table = xlrd.open_workbook(xlsname)
                sheet = table.sheet_by_index(index)
            except FileNotFoundError:
                print('当前没有{}文件,三秒后退出程序'.format(xlsname))
                sleep(3)
                sys.exit()
            lows = sheet.nrows
            cols = sheet.ncols
            # print(lows,cols)
            data = {}
            for low in range(1, lows):
                for col in range(0, cols):
                    key = sheet.cell(0, col).value
                    value = sheet.cell(low, col).value
                    data[key] = value
                ret = fun(data=data, *arg, **kwargs)
                # return ret
        return wrapp
    return function


@excel('hah.xls')
def xls(data):
    for i,k in  data.items():
        print(i,k)

if __name__ == '__main__':
    xls()
