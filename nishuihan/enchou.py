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

Zi_Ku =dm.SetDict(0,r"C:\Users\Administrator\Desktop\wenjian\新建文件夹\主线库.txt")
Tu_Ku =dm.SetPath(r'C:\Users\Administrator\Desktop\wenjian\图文件')
Zhao_Tu = lambda x1=881, y1=652, x2=1014, y2=735, file="继续.bmp|继续1.bmp|继续2.bmp|继续3.bmp|继续4.bmp|",color="36.2.87-180.5.60"\
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
def mouse(x, y, *args):
    dm.movetoex(x, y, *args)
    sleep(random.randint(1, 5) / 5)
    dm.leftclick()

def Ren_WU_Kuan():  # 支线任务框
    return dm.FindMultiColor(965, 327, 1279, 590, '3db27a-000000',
                             '3|0|41bb79-000000,3|6|37b075-000000', 0.95, 0)
def Wanc():
    while True:
        z = Zhao_Tu(467, 355, 795, 535, '我来帮你恢复.bmp')
        if z[0] != -1:
            sleep(100)
        else:
            z = Zhao_Tu(467, 355, 795, 535, '完成1.bmp')
            if z[0] != -1:
                dm.movetoex(z[1], z[2], 50, 5)
                sleep(0.1)
                dm.leftclick()
                sleep(1)
                z1 = Zhao_Tu(975, 460, 1246, 664, '提交4.bmp')
                if z[0] != -1:
                    dm.movetoex(z1[1], z1[2], 5, 5)
                    sleep(0.1)
                    dm.leftclick()
                    sleep(1)
                    break
            else:
                Ctf()
                sleep(5)
def XianFa():
    while True:
        z = Zhao_Tu(54, 142, 491, 413, '阴谋计划.bmp')
        print('打开包裹', z)
        if z[0] != -1:
            dm.keypresschar('b')
            sleep(1)
            z = Zhao_Tu(244, 49, 1244, 392, '背包.bmp')
            sleep(0.5)
            mouse(z[1] + 10, z[2] + 220, 10, 10)
            sleep(0.5)
            dm.movetoex(z[1] + 90, z[2] + 20, 10, 10)
            sleep(0.1)
            dm.rightclick()
            sleep(5)
            dm.keypresschar('b')
            break
        else:
            dm.keypresschar('tab')
            sleep(1)
            t = dm.FindColor(425, 55, 866, 120, 'ff4444-000000', 1.0, 0)
            # Rool()
            # print('一')
            if t[0] != 0:
                print('打怪1')
                dm.keypresschar('1')
                ##血河1技能不刷新图像
                while True:
                    S_W()
                    dm.keypresschar('1')
                    b = dm.IsDisplayDead(417, 700, 444, 726, 5)
                    if b == 0:
                        l = random.randint(1, 5)
                        dm.keypresschar(l)
                    t = dm.FindColor(425, 55, 866, 120, 'ff4444-000000', 1.0, 0)
                    sleep(0.3)
                    if t[0] == 0:
                        print('打死了')
                        # print('yi')
                        sleep(0.5)
                        break
            else:
                Ctf()
                sleep(3)
    Wanc()
def S_W():
    z = Zhao_Tu(433, 316, 986, 562, '疗伤.bmp')
    if z[0] != -1:
        dm.movetoex(z[1], z[2] - 20, 5, 5)
        sleep(0.5)
        dm.leftclick()


def Da_Jie():
    while True:
        z = Zhao_Tu(61, 110, 658, 335, '制造骚乱.bmp|演武堂管事.bmp|查看线索.bmp')
        if z[0] != -1:
            break
        else:
            Ctf()
            sleep(xx())
    while True:
        z = Zhao_Tu(61, 110, 658, 335, '与xxx对话.bmp|')
        print('与xxx对话.bmp|',z)
        if z[0] != -1:
            break
        else:
            dm.keypresschar('tab')
            sleep(1)
            t = dm.FindColor(410,0,905,148,
                             'ff4444-000000|a46ee8-191818|9ea6f1-191818', 1.0, 0)
            if t[0] != 0:
                print('打怪1')
                dm.keypresschar('1')
                ##血河1技能不刷新图像
                n=0
                while True:
                    S_W()
                    n+=1
                    Z = Zhao_Tu(1017, 345, 1264, 410, '失败.bmp')
                    if Z[0] != -1 or n>100: #解决木桩问题
                        z = Zhao_Tu(499, 475, 949, 697, '放弃任务.bmp')
                        dm.movetoex(z[1], z[2], 10, 10)
                        sleep(0.1)
                        dm.leftclick()
                        sleep(xx())
                        dm.keypresschar("enter")
                        sleep(xx())
                        break
                    else:
                        dm.keypresschar('1')
                        b = dm.IsDisplayDead(417, 700, 444, 726, 5)
                        if b == 0:
                            l = random.randint(1, 5)
                            dm.keypresschar(l)
                            sleep(0.3)
                        t = dm.FindColor(410,0,905,148,
                                         'ff4444-000000|a46ee8-191818|9ea6f1-191818', 1.0, 0)

                        if t[0] == 0 :
                            sleep(1)
                            break

            else:
                Ctf()
                sleep(2)

    Wanc()

def jie_renwu(hwnd,str,msg):
    while True:
        z = Zhao_Tu(715, 526, 1021, 704, '提问.bmp')
        if z[0] != -1:
            mouse(z[1] - 300, z[2], 20, 10)
            sleep(xx())
            dm.SendString(hwnd, str)
            sleep(0.1)
            dm.keypresschar('enter')
            sleep(xx())
            z = dm.findstre(335, 207, 1002, 601,msg , '160.68.73-10.10.10', 0.95).split('|')
            sleep(0.5)
            if z[0]!=0:
                mouse(int(z[1]) + 10, int(z[2]) + 2, 5, 5)
                sleep(0.5)
                dm.keypresschar('esc')
                print('去接任务')
                sleep(xx())
                break
        else:
            print("呼唤小精灵")
            dm.keydownchar('alt')
            sleep(0.1)
            dm.keypresschar('j')
            sleep(0.1)
            dm.keyupchar('alt')
            print('睡两秒')
            sleep(2)
def En_Chou(hwnd):
    enchou = [
        ["一探虚实1.bmp|瓦上君子1.bmp|牛刀杀鸡.bmp|驱虎呑狼.bmp", Wanc],
        ['先发制人.bmp', XianFa],
        ['趁火打劫.bmp|断敌一指.bmp|以眼还眼.bmp', Da_Jie],

    ]
    print('当前--快意恩仇')
    while True:
        Z =Ren_WU_Kuan()
        # print('任务框', Z)
        if Z[0] == 0: #当前没任务，去接任务
            z = Zhao_Tu(571, 311, 827, 540, '敖青云.bmp|光云长.bmp|敖青云1.bmp')
            if z[0] != -1:
                dm.keypresschar('F')
            else:
                jie_renwu(hwnd,str="快意恩仇",msg='敖青云')
            n=0
            while True:
                z = Zhao_Tu(435, 314, 839, 565, '我要进行修炼.bmp')
                zz = Zhao_Tu(435, 314, 839, 565, '快意恩仇.bmp|')
                if zz[0] == -1 and z[0] != -1 :
                    print('任务完成')
                    return None
                elif zz[0] != -1:
                        mouse(zz[1], zz[2], 50, 5)
                        sleep(2)
                        zz1 = Zhao_Tu(1036, 511, 1261, 685, '接受.bmp|')
                        mouse(zz1[1], zz1[2], 15, 5)
                        sleep(0.5)
                        print('接到任务')
                        break
                elif n>50:
                    break
                else:
                    n+=1
                    sleep(3)



        else: #有任务，执行任务
            for i in enchou:
                Z1 = Zhao_Tu(68,113,539,279,i[0])
                print(Z1)
                sleep(0.5)
                if Z1 [0]!= -1:
                    # print('当前任务{}'.format(i[0]))
                    i[1]()
                    sleep(xx())
                    break


if __name__ == '__main__':

    hwnds = dm.EnumWindowByProcess("GacRunnerNG.exe", "逆水寒", "", 1).split(',')
    a, b = 1, 2
    bd = dm.BindWindowEx(hwnds[0], 'dx2', 'dx2', 'dx', 'dx.public.disable.window.size', 101)
    dm.MoveWindow(hwnds[0], 1, 2)
    En_Chou(hwnds[0])

