import xml.etree.ElementTree as Et
import base64
import time
import sys
import xlrd
import zipfile
import configparser

'''
公安报文，如需修改为其他类型报文，需修改
xmltxt字段 --报文模板
跟随jz.xls文件，第一行为需修改的字段名，后面为需修改的值，全部用文本形式写入
parse .root字段，值为xml文件tag
parse函数中农
if k in iv.attrib:
    iv.set(k, str(encod(str(v))).replace('b', '').split("'")[1])
此处修改v，无需加密  
'''

conf = configparser.ConfigParser()
conf.read('conf.cfg')


def encod(s):
    # s= str(s)
    ss = base64.b64encode(s.encode('utf-8'))
    return ss


def zipdir():
    # file 要打包的文件
    s = str(time.time() * 100000).split('.')[0]

    outfilename = conf.get('zipname', 'name') + s + '.zip'
    print(outfilename, '打包完成')
    outfullfile = conf.options('filename')
    # print(outfullfile)
    zip = zipfile.ZipFile(outfilename, 'w')
    for i in outfullfile:
        # i 配置中所有文件
        witefilename = conf.get('filename', i)
        # print(witefilename)
        witefilename = './' + witefilename
        zip.write(witefilename)
    zip.close()


def parse(data):
    f = conf.get('filename', 'f1')
    f = './' + f
    # print(f)
    while True:
        try:
            # file = input('输入需要格式化文件路径：')
            tree = Et.parse(f)
            # print(tree)
            root = tree.getroot()
            break
            # print(root)
        except FileNotFoundError:
            print('文件路径错误，3秒后退出重新输入')
            time.sleep(3)
            sys.exit()
    roots = conf.options('tag')
    for isw in roots:
        isw = conf.get('tag', isw)
        for iv in root.iter(isw):
            # print(i.attrib)
            for k, v in data.items():
                # print(type(v))
                # print(str(encod(v)).replace('b',''))
                if k in iv.attrib:
                    iv.set(k, str(encod(str(v))).replace('b', '').split("'")[1])
    tree.write(f, encoding='utf-8')
    zipdir()


def creat_data():
    data = {}
    try:
        table = xlrd.open_workbook('./jz.xls')
    except FileNotFoundError:
        print('当前文件夹没有jz.xls文件，检查！三秒后退出程序')
        time.sleep(3)
        sys.exit()
    sheet = table.sheet_by_index(0)  # 获取第一张表
    # 获取有效行
    all_low = sheet.nrows
    # 获取有效列
    all_col = sheet.ncols
    # print(all_low,'行')
    # print(all_col,'列')
    # 获取表头字段，作为xml文档索引,值为xml属性值
    count = 1
    for il in range(1, all_low):
        for ik in range(0, all_col):
            key = sheet.cell(0, ik)
            val = sheet.cell(il, ik)
            # print(key.value,end=" ")
            data[key.value] = val.value

        parse(data)

        print('第{}个文件完成'.format(count))
        count += 1


if __name__ == '__main__':
    creat_data()
    i = 5
    while i > 0:
        print('加密报文全部完成，bye~~{0}秒后退出'.format(i))
        time.sleep(1)
        i -= 1
# xmlfile()
