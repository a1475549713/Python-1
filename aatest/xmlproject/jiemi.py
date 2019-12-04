import zipfile
from xml.etree import ElementTree as Et
import os
import base64
import time
import sys


# logformat = "%(asctime)s - %(levelname)s - %(message)s"
# dataformat = '%Y/%m/%d %H:%M:%S '
# logging.basicConfig(filename='hha.log', level='DEBUG', format=logformat, datefmt=dataformat)


# 解密函数
def decode(attr):
    # print('s', attr)
    attr = base64.b64decode(attr)
    # logging.info('the attr decode')
    return attr.decode('utf-8')


def enconde(attr):
    attr = base64.b64encode((attr.encode('utf-8')))
    #  logging.info('the attr encode')
    return attr


# 返回当前文件下所有zip文件
def zipjfile():
    allzip = []
    zipfiles = os.walk('./')
    for a, b, i in zipfiles:
        # print(i)
        for ip in i:
            # print(ip)
            if '.zip' in ip:
                allzip.append(ip)
            # logging.info('the file {} is find'.format(ip))
    return allzip


def jiaya():
    # 获取所有zip文件列表
    zipfilelist = zipjfile()
    print('当前一共', len(zipfilelist), '个文件待解压')
    for zipfiles in zipfilelist:
        zipnamelist = []
        print('========*******========')
        print('当前解压文件', zipfiles)
        print('========*******========')
        s = zipfiles.split('.')
        pwd = s[0]
        # logging.debug('now decode {},password is{}'.format(zipfiles, pwd))
        get_pwd = pwd.encode('utf-8')
        print(get_pwd)
       # print('密码',type(get_pwd.decode('utf-8')))
        # menber = s[1]
        # print(pwd)
        # print(menber)
        if not os.path.exists(pwd):
            os.makedirs(pwd)
        zippath = './' + zipfiles
        # print(zippath)
        zips = zipfile.ZipFile(zippath)
        # logging.info('the zip path is %s' % zippath)
        for file in zips.namelist():
            # print(file)
            if file != './':
                zipnamelist.append(file)
            try:
                zips.extract(member=file, pwd=get_pwd, path=pwd)
            except RuntimeError:
                # logging.warning('Password mistake exit ')
                print('密码错误,3秒后退出')
                time.sleep(3)
                sys.exit()
        # logging.info('Extract the complete {}'.format(file))
        print(zipfiles, '解压完成')
        writexml(pwd, zipnamelist)
    # return zipnamelist
    # print(zipnameList)
    # 修改xml文件


# 最大递归三层
def gettags(root):
    tags = []
    # attrs = {}
    for o in root:
        # print(o.tag)
        tags.append(o.tag)
        #  attrs.update(o.attrib)
        for ts in o:
            # print(t.tsg)
            tags.append(ts.tag)
            #  attrs.update(t.attrib)
            for s in ts:
                # print(s.tag)
                tags.append(s.tag)
            #   attrs.update(s.attrib)
    # logging.debug('get tags')
    return tags


def getattrs(root):
    # tags = []
    attrs = {}
    for o in root:
        # print(o.tag)
        # tags.append(o.tag)
        attrs.update(o.attrib)
        for td in o:
            # print(t.tsg)
            # tags.append(t.tag)
            attrs.update(td.attrib)
            for s in td:
                # print(s.tag)
                # tags.append(s.tag)
                attrs.update(s.attrib)
    # logging.debug('get attrs')
    return attrs


# print(tags)
def writexml(pwd, zipnamelist):
    # zipnamelist = jiaya()
    for xmlfile in zipnamelist:
        print('========*******========')
        print('当前解密文件', xmlfile)
        print('========*******========')
        try:
            xmlfiles = './' + pwd + '/' + xmlfile
            file = Et.parse(xmlfiles)
        except Et.ParseError:
            print('该文件{}非.xml文件或xml文件格式错误'.format(xmlfile))
            print('尝试解密下一个文件')
            continue
        root = file.getroot()
        # gettag
        tags = gettags(root)
        attrs = getattrs(root)
        for tag in tags:  # 获取标签
            for ivs in root.iter(tag):  # 获取标签下属性
                for k, v in attrs.items():  # 获取原属性键值对
                    # print(k,v)
                    if k in ivs.attrib:
                        try:  # 判断键值
                            # print('w', str(decode(str(v))).replace('b', '').split("'")[1])
                            ivs.set(k, str(decode(str(v))))  # 解码
                           # print(k, '解密成', str(decode(str(v))))
                        # logging.debug('{}is replace'.format(k))
                        except :
                            # logging.warning('{}Unable to decode'.format(k))
                            print(k, '密文错误跳过')
                            continue
        # logging.debug('{}Decoding to complete'.format(xmlfile))
        print(xmlfile, '解密完成')
        print('========*******========')
        file.write(xmlfiles, encoding='utf-8')


# 读取xml文件

if __name__ == '__main__':
    jiaya()
    t = 3
    while t > 0:
        print('文件全部解码完毕，{}秒后退出程序'.format(t))
        time.sleep(1)
        t -= 1
# logging.debug('all complete exit')
