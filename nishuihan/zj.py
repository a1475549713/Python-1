import win32com.client
from time import sleep, strftime, localtime
import random

import logging

logformat = "%(asctime)s - %(levelname)s - %(message)s"
dataformat = '%Y/%m/%d %H:%M:%S '
logging.basicConfig(filename='jilu.log', level='DEBUG', format=logformat, datefmt=dataformat)

dm = win32com.client.Dispatch('dm.dmsoft')
# print(dm.ver())
g = dm.Reg("2244939288cfa31e5135147e45e56bbc65440c5b8c", "")

Zi_Ku = dm.SetDict(0, r"C:\Users\Administrator\Desktop\wenjian\主线库.txt")
Tu_Ku = dm.SetPath(r'C:\Users\Administrator\Desktop\wenjian\图文件')
Zhao_Tu = lambda x1=881, y1=652, x2=1014, y2=735, file="继续.bmp|继续1.bmp|继续2.bmp|继续3.bmp|继续4.bmp|", \
                 color="36.2.87-180.5.60" \
    : dm.FindPic(x1, y1, x2, y2, file, color, 0.8, 0)

Zhao_Zi = lambda x1=1009, y1=372, x2=1283, y2=606, color='42.91.91-5.10.60,|36.2.87-180.5.60' \
    : dm.OcrEx(x1, y1, x2, y2, color, 0.8).split('|')  # 任务框加白色字体

Zhao_Se = lambda x1=1007, y1=375, x2=1295, y2=605, color="bc7905-000000|f9b517-030303|feb817-202020|dda118-000000" \
    : dm.FindColor(x1, y1, x2, y2, color, 1.0, 0)  # 任务框

now = lambda: strftime("%X", localtime())
xx = lambda: random.randint(1, 5) / 3


def Ctf():
    dm.keydownchar('ctrl')
    dm.keypresschar('f')
    dm.keyupchar('ctrl')


def Shi_Bai():
    Z = Zhao_Tu(1017, 345, 1264, 410, '失败.bmp')
    if Z[0] != -1:
        dm.keypresschar('l')
        sleep(1)
        Z = Zhao_Tu(14, 140, 750, 601, '失败.bmp')
        sleep(.5)
        dm.movetoex(Z[1], Z[2], 10, 10)
        sleep(.5)
        dm.leftclick()
        sleep(.5)
        z = Zhao_Tu(499, 475, 949, 697, '放弃任务.bmp')
        dm.movetoex(z[1], z[2], 10, 10)
        sleep(1)
        dm.leftclick()
        sleep(1)
        dm.keypresschar("enter")
        sleep(1)
        dm.keypresschar("l")


def Zhao_Guai():
    return dm.FindColor(425, 55, 866, 120, 'ff4444-000000|a46ee8-191818|f1dc69-191818', 1.0, 0)  # 红紫黄


def zj_A():  # 打怪
    name = ''
    l = [['九灵.bmp', '九灵']]
    for i in l:
        z = Zhao_Tu(83, 67, 109, 89, i[0])
        if z[0] != -1:
            name = i[1]

    while True:
        if name == '九灵':  # 开宝宝
            Z = Zhao_Tu(260, 58, 463, 134, '宝宝.bmp')
            if Z[0] == -1:
                dm.keypresschar('f4')
                sleep(1)
        dm.keypresschar('tab')
        sleep(0.5)
        t = Zhao_Guai()
        if t[0] != 0:  # 有怪
            print("开始打怪了")
            dm.keypresschar('1')
            z = dm.IsDisplayDead(417, 700, 444, 726, 5)  ##判断1技能有没有变化除铁衣外   用来寻路。每个职业不一样，需要解决问题
            while True:
                SW()
                if z == 0:
                    l = random.randint(1, 5)
                    # print("按键",l)
                    dm.keypresschar(l)
                    sleep(0.2)
                    t = Zhao_Guai()
                    if t[0] == 0:  # 怪死了
                        print('怪死了')
                        dm.keyupchar('1')
                        break
                else:
                    dm.keypresschar('1')
                    sleep(1)
        else:
            break


def WangCheng():
    while True:
        Ctf()
        dm.movetoex(223, 287, 160, 90)
        sleep(xx())
        z = Zhao_Tu(467, 355, 795, 535, '完成1.bmp')
        z1 = Zhao_Tu(975, 460, 1246, 664, '提交4.bmp')
        if z[0] != -1:
            dm.movetoex(z[1], z[2], 5, 5)
            sleep(0.1)
            dm.leftclick()
            sleep(0.78)
            z = Zhao_Tu(975, 460, 1246, 664, '提交4.bmp')
            if z[0] != -1:
                dm.movetoex(z[1], z[2], 5, 5)
                sleep(0.1)
                dm.leftclick()
                sleep(0.5)
            break
        elif z1[0] != -1:
            dm.movetoex(z1[1], z1[2], 5, 5)
            sleep(0.1)
            dm.leftclick()
            sleep(1)
            break
        else:
            sleep(3)


def Zhao_DiTU(x1='', x2='', x3='', x4='', y1='', y2='', y3='', y4='', ):  # fuben外找地图
    dm.keypresschar('M')
    sleep(0.5)
    dm.moveto(933, 13)
    sleep(0.1)
    dm.leftclick()
    sleep(0.1)
    dm.keypresschar(x1)
    sleep(0.1)
    dm.keypresschar(x2)
    sleep(0.1)
    dm.keypresschar(x3)
    sleep(0.1)
    dm.keypresschar(x4)
    sleep(0.1)
    dm.keypresschar('tab')
    sleep(0.1)
    dm.keypresschar(y1)
    sleep(0.1)
    dm.keypresschar(y2)
    sleep(0.1)
    dm.keypresschar(y3)
    sleep(0.1)
    dm.keypresschar(y4)
    sleep(0.1)

    dm.movetoex(1030, 11, 5, 5)
    sleep(0.1)
    dm.leftclick()
    sleep(0.1)
    dm.keypresschar('M')


def Ti_Jiao1():
    z = Zhao_Tu(479, 242, 786, 433, '提交.bmp|提交1.bmp|提交2.bmp|')
    sleep(0.5)
    if z[0] != -1:
        dm.movetoex(z[1], z[2], 5, 5)
        sleep(0.1)
        dm.leftclick()


def SW():
    z = Zhao_Tu(433, 316, 986, 562, '疗伤.bmp')
    if z[0] != -1:
        dm.movetoex(z[1], z[2] - 20, 5, 5)
        sleep(0.5)
        dm.leftclick()


def mouse(x, y, *args):
    dm.movetoex(x, y, *args)
    sleep(random.randint(5, 10) / 5)
    dm.leftclick()
    sleep(0.5)


def Ren_WU_Kuan():  # 支线任务框
    return dm.FindMultiColor(965, 327, 1279, 590, '3db27a-000000',
                             '3|0|41bb79-000000,3|6|37b075-000000', 0.95, 0)


def jie_renwu(hwnd, str, msg):
    while True:
        z = Zhao_Tu(715, 526, 1021, 704, '提问.bmp')
        if z[0] != -1:
            mouse(z[1] - 300, z[2], 20, 10)
            sleep(xx())
            dm.SendString(hwnd, '仗剑江湖')
            sleep(0.1)
            dm.keypresschar('enter')
            sleep(xx())
            z = dm.findstre(335, 207, 1002, 601, '点击寻路至萧姨', '160.68.73-10.10.10', 0.95).split('|')
            print('点击寻路至萧姨', z)
            sleep(0.5)
            if z[0] == "0":
                mouse(int(z[1]) + 10, int(z[2]) + 2, 5, 5)
                sleep(0.5)
                dm.keydownchar('alt')
                sleep(0.2)
                dm.keypresschar('j')
                sleep(0.2)
                tan = dm.KeyUpChar('alt')
                print(tan)
                dm.KeyUpChar('alt')
                print('去接任务')
                sleep(xx())
                break
        else:
            print("呼唤小精灵")
            dm.keydownchar('alt')
            sleep(0.2)
            dm.keypresschar('j')
            sleep(0.2)
            tan = dm.KeyUpChar('alt')
            print(tan)
            dm.KeyUpChar('alt')
            print('睡两秒')
            sleep(2)


def Xiao_Yi():
    return Zhao_Tu(64, 148, 406, 354, "萧姨.bmp")


def XueZhong():
    Ctf()
    while True:
        Z1 = Xiao_Yi()
        print('箫姨', Z1)
        if Z1[0] != -1:
            WangCheng()
            break
        else:
            sleep(1)
            z = Zhao_Tu(473, 1, 1164, 471, '背包.bmp')
            print('背包', z)
            if z[0] != -1:  # 当前有背包
                dm.movetoex(z[1] + 100, z[2] + 20, 15, 15)  # 背包第一格
                sleep(0.1)
                dm.rightclick()
                sleep(xx())
                Ti_Jiao1()
                sleep(1)
                Jiemian = Zhao_Tu(0, 3, 122, 90, '三.bmp')
                if Jiemian[0]==-1:
                    tijiao = Zhao_Tu(933, 556, 1236, 700, '提交道具.bmp')
                    if tijiao[0] != -1:
                        mouse(tijiao[1], tijiao[2], 50, 5)
                    dm.movetoex(z[1] + 140, z[2] + 20, 15, 15)# 背包第2格
                    sleep(0.1)
                    dm.rightclick()
                    sleep(xx())
                    Ti_Jiao1()
                    sleep(xx())
                    Jiemian = Zhao_Tu(0, 3, 122, 90, '三.bmp')
                    if Jiemian[0] == -1:
                        tijiao = Zhao_Tu(933, 556, 1236, 700, '提交道具.bmp')
                        if tijiao[0] != -1:
                            mouse(tijiao[1], tijiao[2], 50, 5)
                            sleep(xx())
                        dm.movetoex(z[1] + 190, z[2] + 20, 15, 15) # 背包第3格
                        sleep(0.1)
                        dm.rightclick()
                        sleep(xx())
                        Ti_Jiao1()
                        sleep(1)
                        # = Zhao_Tu(933, 556, 1236, 700, '提交道具.bmp')

            else:
                Ctf()
                sleep(3)


def MoQi():
    Ctf()
    while True:
        z = Zhao_Tu(962, 546, 1269, 671, '别以为.bmp|再来练练.bmp')
        print("再来练练", z)
        if z[0] != -1:

            mouse(z[1], z[2], 100, 5)
            sleep(5)
            break
        else:
            Ctf()
            sleep(5)
    zj_A()
    WangCheng()


def Yuan_Zhu():
    # while True:
    sleep(1)
    Z1 = Zhao_Tu(71, 63, 545, 325, "帮会庙会分店.bmp")
    print('帮会庙会', Z1)
    if Z1[0] != -1:
        mouse(Z1[1], Z1[2], 55, 5)
        sleep(1)
    while True:
        Z = Zhao_Tu(461, 32, 784, 153, '店铺列表.bmp')
        print('店铺列表', Z)
        if Z[0] != -1:
            mouse(Z[1], Z[2] + 390, 100, 5)
            sleep(0.5)
            Z1 = Zhao_Tu(933, 426, 1250, 686, '购买.bmp')
            mouse(Z1[1], Z1[2], 20, 5)
            sleep(0.1)
            dm.keypresschar('enter')
            sleep(0.1)
            dm.keypresschar('esc')
            sleep(0.1)
            dm.keypresschar('esc')
            sleep(0.1)
            dm.keypresschar('esc')
            Ctf()
            while True:
                z = Zhao_Tu(471, 220, 798, 430, '提交.bmp|提交1.bmp|提交物品.bmp')
                if z[0] != -1:
                    Ti_Jiao1()
                    break
                else:
                    sleep(3)
            break
        else:
            sleep(3)

    WangCheng()




def Duan():
    sleep(1)
    z = Zhao_Tu(295, 499, 582, 682, '放弃任务.bmp')
    mouse(z[1], z[2], 50, 10)
    z1 = Zhao_Tu(440, 166, 887, 537, '确定1.bmp')
    sleep(0.1)
    mouse(z1[1], z1[2], 50, 10)
    sleep(5)


def JinChan():
    while True:
        Z1 = Xiao_Yi()
        print('箫姨', Z1)
        if Z1[0] != -1:
            WangCheng()
            break
        else:
            sleep(2)
            dm.keypresschar('tab')
            sleep(1)
            t = dm.FindColor(425, 55, 866, 120, 'ff4444-000000|ffe96e-000000|b479ff-000000', 1.0, 0)
            if t[0] != 0:
                print('打怪1')
                dm.keypresschar('1')
                dm.IsDisplayDead(417, 700, 444, 726, 5)
                ##血河1技能不刷新图像
                while True:
                    l = random.randint(1, 5)
                    dm.keypresschar(l)
                    t = dm.FindColor(519, 67, 582, 94, 'ff4444-000000|ffe96e-000000|b479ff-000000', 1.0, 0)
                    sleep(0.3)
                    if t[0] == 0:
                        sleep(1)
                        break
            else:
                Ctf()
                sleep(5)


def XunShe():
    while True:
        z = Zhao_Tu(22, 79, 530, 361, "特制熏烟.bmp")
        print("特制熏烟", z)
        if z[0] != -1 or Xiao_Yi()[0] != -1:
            break
        else:
            Ctf()
            sleep(5)
    zj_A()
    WangCheng()


def Zhang_Jian(hwnd):
    ziku = [['雪中送炭.bmp', XueZhong],
            ['资源援助.bmp', Yuan_Zhu],
            ['莫欺年少.bmp', MoQi],
            ['金蝉脱壳.bmp', JinChan],
            ["打草熏蛇.bmp", XunShe],
            ['断其喉舌.bmp|火眼金睛.bmp|千杯不醉.bmp|秋风落叶.bmp', Duan],
            ]
    print('当前--仗剑江湖')
    while True:
        Z = Ren_WU_Kuan()
        print('任务框', Z)
        if Z[0] == 0:
            z = Zhao_Tu(571, 311, 827, 540, '敖青云1.bmp')
            if z[0] != -1:
                print('接任务')
                dm.keypresschar('F')
            else:
                jie_renwu(hwnd, '仗剑江湖', '点击寻路至萧姨')
            n = 0
            while True:
                z = Zhao_Tu(435, 314, 839, 565, '再见.bmp')
                zz = Zhao_Tu(435, 314, 839, 565, '仗剑江湖3.bmp|')
                if zz[0] == -1 and z[0] != -1:
                    print('任务完成')
                    return None

                elif zz[0] != -1:
                    dm.movetoex(zz[1], zz[2], 50, 5)
                    sleep(0.1)
                    dm.leftclick()
                    sleep(0.8)
                    zz1 = Zhao_Tu(1036, 511, 1261, 685, '接受.bmp|')
                    sleep(0.5)
                    dm.movetoex(zz1[1], zz1[2], 15, 5)
                    sleep(0.1)
                    dm.leftclick()
                    sleep(0.5)
                    print('接到任务')
                    break
                elif n > 50:
                    break
                else:
                    n += 1
                    sleep(3)

        else:
            for i in ziku:
                Z1 = Zhao_Tu(68, 113, 539, 279, i[0])
                print(Z1)
                sleep(0.5)
                if Z1[0] != -1:
                    # print('当前任务{}'.format(i[0]))
                    i[1]()
                    sleep(xx())
                    break


if __name__ == '__main__':
    hwnds = dm.EnumWindowByProcess("GacRunnerNG.exe", "逆水寒", "", 1).split(',')
    a, b = 1, 2
    bd = dm.BindWindowEx(hwnds[0], 'dx2', 'dx2', 'dx', 'dx.public.disable.window.size', 101)
    dm.MoveWindow(hwnds[0], 1, 2)
    # dm.EnableKeypadSync(1, 500)
    # dm.EnableMouseSync(1, 500)
    Zhang_Jian(hwnds[0])
