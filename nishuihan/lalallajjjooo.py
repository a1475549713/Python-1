import win32com.client
from time import sleep, ctime, strftime, localtime
import random
import sys
import multiprocessing
from nishuihan import myMutilprocess
import logging

logformat = "%(asctime)s - %(levelname)s - %(message)s"
dataformat = '%Y/%m/%d %H:%M:%S '
logging.basicConfig(filename='jilu.log', level='DEBUG', format=logformat, datefmt=dataformat)

dm = win32com.client.Dispatch('dm.dmsoft')
# print(dm.ver())
g = dm.Reg("2244939288cfa31e5135147e45e56bbc65440c5b8c", "")
dm.EnableRealMouse (2,20,30)
dm.EnableRealKeypad (1)
Zi_Ku = dm.SetDict(0, r"C:\Users\Administrator\Desktop\wenjian\主线库.txt")
Tu_Ku = dm.SetPath(r'C:\Users\Administrator\Desktop\wenjian\图文件')


def Zhao_Tu(x1, y1, x2, y2, file, color="36.2.87-180.5.60"):
    return dm.FindPic(x1, y1, x2, y2, file, color, 0.8, 0)


def Zhao_Zi(x1, y1, x2, y2, color):
    return dm.OcrEx(x1, y1, x2, y2, color, 0.8).split('|')


def Zhao_Se(x1, y1, x2, y2, color):
    return dm.FindColor(x1, y1, x2, y2, color, 1.0, 0)


def Ren_WU_Kuan():  # 支线任务框
    return dm.FindMultiColor(965, 327, 1279, 590, '3db27a-000000',
                             '3|0|41bb79-000000,3|6|37b075-000000', 0.95, 0)


def mouse(x, y, *args):
    dm.movetoex(x, y, *args)
    sleep(random.randint(1, 5) / 5)
    dm.leftclick()


def Ctf():
    dm.keydownchar('ctrl')
    dm.keypresschar('f')
    dm.keyupchar('ctrl')


def S_W():  # 死亡处理
    S = Zhao_Tu(173, 149, 1149, 655, '等待救援.bmp|等待救援1.bmp')
    if S[0] != -1:
        sleep(3)
        # Q=Zhao_Tu(334,153,947,560,'确定4.bmp|确定5.bmp')
        y = Zhao_Tu(173, 149, 1149, 655, '回疗伤点.bmp')
        if y[0] != -1:
            mouse(y[1], y[2], 5, 5)
            sleep(1)
            y = Zhao_Tu(173, 149, 1149, 655, '确认1.bmp')
            if y[0] != -1:
                mouse(y[1], y[2], 5, 5)


def Zhao_Guai():
    return dm.FindColor(417, 12, 860, 108,
                        'ff4444-000000',
                        1.0, 0)


def Get_Name(hwnd):
    t = dm.GetWindowTitle(hwnd).split(":")[1].split('@')[0]
    if t == "11634700257":
        return '碎梦-你算哪只小浣熊'
    elif t == "3611800257":
        return '素问-你算那块小饼干'
    elif t == "1226900257":
        return '铁衣-你也算块小饼干'
    else:
        return t


def A():  # 打怪
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
        # print('一')
        print(t)
        if t[0] != 0:  # 有怪
            print("开始打怪了")
            dm.keypresschar('1')
            z = dm.IsDisplayDead(417, 700, 444, 726, 5)  ##判断1技能有没有变化除铁衣外   用来寻路。每个职业不一样，需要解决问题
            print(z)
            while True:
                S_W()
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
            # # 没怪
            # dm.keypresschar('g')
            # while True:
            #     dm.keypresschar('tab')
            #     sleep(0.5)
            #     t = Zhao_Guai()
            #     # print('一')
            #     print(t)
            #     if t[0] != 0:  # 有怪
            #         print("开始打怪了")
            break


def jie_renwu(hwnd, str, msg):
    while True:
        z = Zhao_Tu(715, 526, 1021, 704, '提问.bmp')
        if z[0] != -1:
            mouse(z[1] - 300, z[2], 20, 10)
            sleep(2.5)
            dm.SendString(hwnd, str)
            sleep(0.1)
            dm.keypresschar('enter')
            sleep(1.8)
            z = dm.findstre(335, 207, 1002, 601, msg, '160.68.73-10.10.10', 0.95).split('|')
            sleep(0.5)
            if z[0] == "0":
                mouse(int(z[1]) + 10, int(z[2]) + 2, 5, 5)
                sleep(0.5)
                mouse(880, 92, 5, 5)
                print('去接任务')
                sleep(1.1)
                break
        else:
            print("呼唤小精灵")
            mouse(1092, 9, 5, 5)
            print('睡两秒')
            sleep(2)


def Jie_Ren_Wu(hwnd, name):
    jie_renwu(hwnd, '连云寨押镖', '高俊领')
    C = 100
    while True:
        zz1 = Zhao_Tu(885, 663, 1016, 736, '对话1.bmp')
        # z = dm.findstr(268, 444, 924, 648, '最大的福气', '60.0.88-60.5.20', 0.8, '', '')
        Jiemian = Zhao_Tu(0, 3, 122, 90, '三.bmp')
        # print('界面', Jiemian)
        if Jiemian[0] != -1:  # 有界面 ，在跑
            print(name + '正在跑路...休息{}秒'.format(C))
            sleep(1)
            C -= 1
        else:  # 没有界面，判断对话还是读图还是没有任务了
            if zz1[0] != -1:  # 对话
                while True:
                    print(name + "开始对话")
                    dm.keypresschar('F')
                    sleep(0.5)
                    jiesou = Zhao_Tu(1036, 511, 1261, 685, '接受.bmp|')
                    if jiesou[0] != -1:
                        mouse(jiesou[1], jiesou[2], 15, 5)
                        dm.movetoex(474, 117, 236, 90)
                        sleep(1)
                        Ren = Ren_WU_Kuan()
                        if Ren[0] == 0:
                            print(name + '应该是活跃度不够了')
                            return False
                        else:
                            print(name + '接到任务开始跑咯...')
                            logging.debug(name + "---" + "开始押镖" + "---")
                            return True
            else:  # 不在界面且无对话F
                sleep(15)  # 15秒以后判断，，有可能卡的时间太长导致误判
                zz1 = Zhao_Tu(885, 663, 1016, 736, '对话1.bmp')
                Jiemian = Zhao_Tu(0, 3, 122, 90, '三.bmp')
                if Jiemian[0] == -1 and zz1[0] == -1:
                    print(name + "没任务了，结束")
                    dm.keypresschar('esc')
                    sleep(1)
                    dm.keypresschar('F10')
                    sleep(20)
                    return False


def Lin_Jian(z1):  # 领铜钱
    '''

    :param z1:铜钱交子坐标
            :技能交子、技能交子1
            ：全额交子、全额交子1
    :return:
    '''
    print("到终点领奖咯")
    mouse(z1[1], z1[2], 30, 5)
    sleep(1)
    dm.keypresschar('enter')
    # while True:
    sleep(1)
    z12 = Zhao_Tu(428, 225, 886, 521, '技能交子.bmp|技能交子1.bmp')  # 技能交子1|普通交子.bmp 领技能交子
    if z12[0] != -1:  # 没领到铜钱，开始领技能交子
        # mouse(z12[1], z12[2], 30, 5)
        # sleep(1)
        # z13 = Zhao_Tu(428, 225, 886, 521, '技能交子1.bmp')
        # if z13[0] != -1:
        #     mouse(z13[1], z13[2], 30, 5)
        # dm.keypresschar('enter')
        # print("领技能交子")
        # # logging.debug(hwnd + "---" + "战场结束" + "---" + '\r\n')
        # sleep(1)
        # z14 = Zhao_Tu(428, 225, 886, 521, '技能交子1.bmp')
        # if z14[0] != -1:  # 没领到技能交子，开始领普通交子
        #     print("领技能交子失败")
        #     dm.keypresschar('esc')
            sleep(1)
            z15 = Zhao_Tu(428, 225, 886, 521, '全额交子.bmp')  # 技能交子1
            mouse(z15[1], z15[2], 30, 5)
            sleep(1)
            print("领普通交子")
            z16 = Zhao_Tu(428, 225, 886, 521, '全额交子1.bmp')
            mouse(z16[1], z16[2], 30, 5)
            sleep(1)
            dm.keypresschar('enter')
            sleep(2)
            print("跑完了")
    #         break
    # else:
    #     break


def yaBiao(hwnd):
    name = Get_Name(hwnd)
    # dm.BindWindowEx(hwnd, 'dx2', 'dx2', 'dx', 'dx.public.disable.window.size', 101)
    while True:
        Ren = Ren_WU_Kuan()
        if Ren[0] == 0:  # 没任务，进接任务流程
            # 判断是否在主界面
            print(name + "去接任务~~~")
            if not Jie_Ren_Wu(hwnd, name):
                # logging.debug(hwnd + "---" + "开始押镖" + "---" + '\r\n')
                return None
        else:  # 有任务流程
            while True:
                Ren = Ren_WU_Kuan()
                S_W()  # 被人开红的情况下

                XiTong = Zhao_Tu(134, 56, 1109, 660, '系统设置.bmp')
                if XiTong[0] != -1:
                    dm.keypresschar('esc')
                XiTong1 = Zhao_Tu(134, 56, 1109, 660, '确认2.bmp')
                if XiTong1[0] != -1:
                    mouse(XiTong1[1], XiTong1[2], 5, 5)
                if Ren[0] != 0:  # 有任务框
                    print(name + "还没到终点，继续跑啊！！！")
                    dm.keypresschar('tab')
                    sleep(0.5)
                    t = dm.FindColor(425, 55, 866, 120, 'ff4444-000000', 1.0, 0)
                    if t[0] != 0:  # 有怪
                        A()
                    else:
                        Ctf()
                        sleep(random.randint(1, 10))

                else:  # 没任务框，判断对话或者剧情
                    Li_Kai = Zhao_Tu(885, 663, 1016, 736, '对话1.bmp')
                    if Li_Kai[0] == -1:  # 没有F按键
                        z = Zhao_Tu(976, 599, 1169, 695, '选择奖励1.bmp')
                        if z[0] != -1:  # 到终点了
                            print(name + '选择奖励')
                            mouse(z[1], z[2], 100, 5)
                            dm.movetoex(461, 115, 200, 100)
                            sleep(1)
                            tongqian = Zhao_Tu(428, 225, 886, 521, '铜钱交子.bmp')  # 技能交子.bmp|全额交子.bmp|铜钱交子.bmp
                            # jiaozi = Zhao_Tu(428, 225, 886, 521, '技能交子.bmp')
                            if tongqian[0] != -1:
                                Lin_Jian(tongqian)
                                logging.debug(name + "---" + "押镖一次结束" + "---尝试领取铜钱---")
                                break

                        else:  # 没到终点，剧情
                            print(name + '卡剧情了，点掉esc')
                            dm.keypresschar('esc')
                            sleep(0.5)
                    else:
                        dm.keypresschar('f')
                        print(name + '对话中~~')
                        sleep(0.2)


def Ji_He(hwnd):
    dm.BindWindowEx(hwnd, 'dx2', 'dx2', 'dx', 'dx.public.disable.window.size', 101)
    name = Get_Name(hwnd)
    # shiJian(hwnd)
    # logging.debug(name + "---" + "战场打完了" + "---")
    yaBiao(hwnd)
    logging.debug(name + "---" + "押镖完了" + "---")
   # # enChou(hwnd)
   #  zhangJian(hwnd)
    dm.SetWindowState(hwnd, 0)
    sleep(3)
    logging.debug(name + "----------------------退出游戏-----------------------------")
    # tuichu = Zhao_Tu(329, 602, 874, 732, "退出游戏.bmp")
    # if tuichu[0] != -1:
    #     mouse(tuichu[1], tuichu[2], 5, 5)
if __name__ == '__main__':
    hwnds = dm.EnumWindowByProcess("GacRunnerNG.exe", "逆水寒", "", 1).split(',')
    a, b = 1, 2
    bd = dm.BindWindowEx(hwnds[0], 'dx2', 'dx2', 'dx', 'dx.public.disable.window.size', 103)
    # A()
    for hwnd in hwnds:
        if bd == 1:
            print("绑定成功，开始撸")
            dm.MoveWindow(hwnd, a, b)
            t = multiprocessing.Process(target=Ji_He, args=(hwnd,))
            t.start()
            sleep(1)
            a, b = 1, 250
        else:
            print("绑定失败，检查原因")
