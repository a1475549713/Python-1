import win32com.client
from time import sleep, ctime, strftime, localtime
import random
import sys
from multiprocessing import Process

now = lambda: strftime("%X", localtime())

dm = win32com.client.Dispatch('dm.dmsoft')
print(dm.ver())
g = dm.Reg("2244939288cfa31e5135147e45e56bbc65440c5b8c", "")

xx = lambda: random.randint(1, 10) / 3
Zi_Ku = dm.SetDict(0, r"C:\Users\Administrator\Desktop\wenjian\新建文件夹\主线库.txt")
Tu_Ku = dm.SetPath(r'C:\Users\Administrator\Desktop\wenjian\图文件')
Zhao_Tu = lambda x1=881, y1=652, x2=1014, y2=735, file="继续.bmp|继续1.bmp|继续2.bmp|继续3.bmp|继续4.bmp|",color="36.2.87-180.5.60"\
    : dm.FindPic(x1, y1, x2, y2, file, color, 0.8, 0)



Zhao_Zi = lambda x1=1009, y1=372, x2=1283, y2=606, color='42.91.91-5.10.60,|36.2.87-180.5.60' \
    : dm.OcrEx(x1, y1, x2, y2, color, 0.8).split('|')  # 任务框加白色字体

Zhao_Se = lambda x1=1007, y1=375, x2=1295, y2=605, color="bc7905-000000|f9b517-030303|feb817-202020|dda118-000000" \
    : dm.FindColor(x1, y1, x2, y2, color, 1.0, 0)  # 任务框


def Di_Tu():
    dm.keypresschar('M')
    sleep(0.5)
    dm.movetoex(613,403,10,10)
    sleep(0.2)
    dm.leftclick()
    sleep(0.5)
    dm.keypresschar('M')



def A1():
    name = ''
    l = [['九灵.bmp', '九灵']]
    for i in l:
        z = Zhao_Tu(83, 67, 109, 89, i[0])
        if z[0] != -1:
            name = i[1]
    while True:
        if name == '九灵':
            Z = Zhao_Tu(260, 58, 463, 134, '宝宝.bmp')
            if Z[0] == -1:
                dm.keypresschar('f4')
                sleep(1)
        dm.keypresschar('tab')
        sleep(0.5)
        t = dm.FindColor(517,92,597,105, 'de4d52-0f0e0e', 1.0, 0)
        print(t)
        if t[0] != 0:  # 有怪
            print("开始打怪了")
            dm.keypresschar('1')
            while True:
                jin = ["1", '2', "3", '4', '5']
                for i in jin:
                    if i =="1":
                        sleep(3)
                    dm.keypresschar(i)
                    sleep(random.randint(1, 5) / 5)
                    t = dm.FindColor(517, 92, 597, 105, 'de4d52-0f0e0e', 1.0, 0)
                    if t[0] == 0:  # 怪死了
                        print('怪死了')
                        Di_Tu()
                        break
                # dm.keypresschar('tab')
                # sleep(0.2)
                # t = dm.FindColor(425, 55, 866, 120, 'de4d52-0f0e0e', 1.0, 0)
                # if t[0]==0:
                #     Di_Tu()
                #     break
        else:
            Di_Tu()
            tim = 0
            while True:
                dm.keypresschar('tab')
                sleep(0.5)
                t = dm.FindColor(425, 55, 866, 120, 'de4d52-0f0e0e', 1.0, 0)
                if t[0] != 0 or tim%30==0:
                    break
                else:
                    sleep(1)
                    tim +=1

def PiPei():
    shij = Zhao_Tu(987,91,1106,148,"试剑天下.bmp")
    Jiemian = Zhao_Tu(4, 23, 57, 62, '三.bmp')
    wolong = Zhao_Tu(987,91,1106,148,"卧龙岭.bmp")

    if shij[0]!=-1 or wolong[0] != -1:
        print("已找到试剑天下")
        dm.movetoex(1041,114,5,5)
        dm.leftclick()
        sleep(1)
        pipei = Zhao_Tu(716,588,1010,678,"单人匹配.bmp")
        if pipei[0]!=-1:
                dm.movetoex(pipei[1], pipei[2], 5, 5)
                dm.leftclick()
                dm.keypresschar('esc')
                sleep(30)
    elif Jiemian[0]!=-1:
        print('未找到试剑天下，脚本结束')
        return False
def Shi_Jian():

    while True:
        zhanbao = Zhao_Tu(956,370,1276,699,"侠士.bmp")
        if zhanbao[0]!=-1:
            print("战场中")
            A1()
        else:
            zhanguo = Zhao_Tu(425,41,698,109,"试剑天下战报.bmp|卧龙岭战报.bmp")
            if zhanguo[0]!=-1:
                print('一把结束了')
                dm.keypresschar('esc')
                dm.keypresschar('esc')
                dm.keypresschar('esc')
                while True:
                    XiTong = Zhao_Tu(134, 56, 1109, 660, '系统设置.bmp')
                    Jiemian = Zhao_Tu(4, 23, 57, 62, '三.bmp')
                    if XiTong[0]!=-1:
                        dm.keypresschar('esc')
                        sleep(1)
                    if Jiemian[0]!=-1:
                        break
                    else:
                        dm.keypresschar('esc')
                        sleep(1)
            else:
                print("开始报名")
                if not PiPei():
                    break


if __name__ == '__main__':
    dm.keyupchar("1")
    # Shi_Jian()