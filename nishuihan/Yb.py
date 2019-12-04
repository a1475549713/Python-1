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

Zi_Ku = dm.SetDict(0, r"C:\Users\Administrator\Desktop\wenjian\主线库.txt")
Tu_Ku = dm.SetPath(r'C:\Users\Administrator\Desktop\wenjian\图文件')


def now():
    return strftime("%X", localtime())


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
    z12 = Zhao_Tu(428, 225, 886, 521, '技能交子.bmp|技能交子1.bmp')# 技能交子1|普通交子.bmp 领技能交子
    if z12[0] != -1: #没领到铜钱，开始领技能交子
        mouse(z12[1], z12[2], 30, 5)
        sleep(1)
        z13 = Zhao_Tu(428, 225, 886, 521, '技能交子1.bmp')
        if z13[0]!=-1:
            mouse(z13[1], z13[2], 30, 5)
        dm.keypresschar('enter')
        print("领技能交子")
        # logging.debug(hwnd + "---" + "战场结束" + "---" + '\r\n')
        sleep(1)
        z14 = Zhao_Tu(428, 225, 886, 521, '技能交子1.bmp')
        if z14[0] != -1:#没领到技能交子，开始领普通交子
            print("领技能交子失败")
            dm.keypresschar('esc')
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


def Di_Tu():
    dm.keypresschar('M')
    print("地图")
    sleep(0.5)
    jianlu = Zhao_Tu(268, 116, 1066, 618, "剑炉.bmp")
    if jianlu[0] != -1:
        l = [(488, 361), (625, 428), (756, 356), (759, 496), (476, 498)]
        i = random.choice(l)
        mouse(i[0], i[1], 5, 5)
    else:
        l = [(449, 388), (762, 393), (616, 383)]
        i = random.choice(l)
        mouse(i[0], i[1], 5, 5)
    print("关闭地图")
    dm.keypresschar('esc')
    sleep(0.5)
    d = Zhao_Tu(505, 101, 943, 291, '输入坐标寻路.bmp')
    if d[0] != -1:
        dm.keypresschar('esc')
        print("关闭地图")


def BaoBao():
    name = ''
    l = [['九灵.bmp', '九灵']]
    for i in l:
        z = Zhao_Tu(83, 67, 109, 89, i[0])
        if z[0] != -1:
            name = i[1]

    if name == '九灵':
        Z = Zhao_Tu(260, 58, 463, 134, '宝宝.bmp')
        if Z[0] == -1:
            dm.keypresschar('f4')
            sleep(1)


def A1(hwnd):
    # di = Zhao_Tu(425, 55, 866, 120, "神像.bmp|龙吟.bmp|碎梦.bmp|九灵.bmp|铁衣.bmp|素问.bmp|")
    t = dm.FindColor(425, 55, 866, 120, 'de4d52-0f0e0e', 1.0, 0)
    if t[0] != 0:  # 有人
        print("开始打人了")
        while True:  # 判断当前tab不到人退出
            dm.keypresschar('tab')
            sleep(0.5)
            t = dm.FindColor(425, 55, 866, 120, 'de4d52-0f0e0e', 1.0, 0)
            if t[0] == 0:  # 没有人
                print('当前没人了')
                break
            else:
                # 判断当前人死亡退出
                while True:
                    jineng = ["1", "2", "3", "4", "5", "q", "e", "r", "c", "v"]
                    i = random.choice(jineng)
                    if i == "1" or i == "4":
                        dm.keydownchar(i)
                        sleep(random.randint(20, 30) / 6)
                        dm.keyupchar(i)
                    else:
                        dm.keypresschar(i)
                        sleep(random.randint(1, 10) / 10)
                    t = dm.FindColor(425, 55, 866, 120, 'de4d52-0f0e0e', 1.0, 0)
                    if t[0] == 0:
                        print('人死了')
                        break

    else:
        Di_Tu()
        tim = 1
        sleep(0.5)
        # dm.keypresschar('enter')
        # dm.SendString(hwnd, "手动7500==25R,一天满，+v*lu201645聊")
        # dm.keypresschar('enter')
        while True:  # 找到人为止退出
            dm.keypresschar('tab')
            sleep(0.5)
            # di = Zhao_Tu(425, 55, 866, 120, "神像.bmp|龙吟.bmp|碎梦.bmp|九灵.bmp|铁衣.bmp|素问.bmp|")
            t = dm.FindColor(425, 55, 866, 120, 'de4d52-0f0e0e', 1.0, 0)
            if t[0] != 0 or tim % 20 == 0:  # 有人
                break
            # elif tim%19==0: #每15秒一次跟随队伍
            #     dm.keypresschar('g')
            # elif tim%29==0: #每35秒一次换地图
            #     Di_Tu()
            else:
                sleep(0.5)
                tim += 1


def PiPei(name):
    Jiemian = Zhao_Tu(0, 3, 122, 90, '三.bmp')
    wolong = Zhao_Tu(890, 56, 1090, 187, "卧龙岭.bmp|试剑天下.bmp")
    print(wolong)
    if wolong[0] != -1:  # 找到战场图标，进入报名流程
        print("已找到试剑天下")
        logging.debug(name + "---" + "战场开始报名" + "---")
        dm.movetoex(wolong[1], wolong[2], 5, 5)
        dm.leftclick()
        sleep(1)
        pipei = Zhao_Tu(716, 588, 1010, 678, "单人匹配.bmp")
        if pipei[0] != -1:
            dm.movetoex(pipei[1], pipei[2], 5, 5)
            dm.leftclick()
            dm.keypresschar('esc')
            sleep(2)
            zuida = Zhao_Tu(120, 50, 1189, 661, "本周声望已达最大值.bmp")
            if zuida[0] == -1:
                m = 1
                while True:
                    sleep(5)
                    m += 1
                    zhanbao = Zhao_Tu(897, 276, 1284, 604, "战报.bmp|侠士.bmp|狂士.bmp")
                    if zhanbao[0] != -1 or m % 150 == 0:
                        print("已进入战场")
                        sleep(1)
                        break
                return True
            else:
                print("声望已刷满")
                logging.debug(name + "---" + "声望已刷满退出" + "---")
                quxiao = Zhao_Tu(286, 123, 978, 459, "取消.bmp")
                if quxiao[0] != -1:
                    mouse(quxiao[1], quxiao[2], 5, 5)
                return False
        else:
            logging.debug(name + "---" + "界面被遮挡" + "---")
            import time
            dm.CapturePng(0, 0, 1278, 719, r"C:\Users\Administrator\Desktop\wenjian\{}.png".format(time.time()))
            return False
    elif Jiemian[0] != -1:  # 在界面上，没有找到图标，结束
        print('未找到试剑天下，脚本结束')
        logging.debug(name + "---" + "没找到战场图标退出" + "---")
        import time
        dm.CapturePng(0, 0, 1278, 719, r"C:\Users\Administrator\Desktop\wenjian\{}.png".format(time.time()))
        return False
    else:  # 不在界面，
        print('传送中')
        sleep(10)
        return True


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
                    if SW():
                        Duan()
                        break
                    else:
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


def SW():
    z = Zhao_Tu(433, 316, 986, 562, '疗伤.bmp|免费再起.bmp')
    z1 = Zhao_Tu(433, 316, 986, 562, '免费再起.bmp')
    if z[0] != -1:
        mouse(z[1], z[2] - 20, 5, 5)
        dm.keypresschar('f10')
        sleep(10)
        return True
    elif z1[0] != -1:
        mouse(z1[1] + 58, z1[2] + 72, 5, 5)
        dm.keypresschar('f10')
        sleep(10)
        return True
    else:
        return False


xx = lambda: random.randint(1, 5) / 3


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
        print('与xxx对话.bmp|', z)
        Z = Ren_WU_Kuan()
        if z[0] != -1 :
            Wanc()
            break
        elif Z[0]==0:
            dm.keypresschar('f10')
            sleep(10)
            break
        else:
            dm.keypresschar('tab')
            sleep(1)
            t = dm.FindColor(410, 0, 905, 148,
                             'ff4444-000000|a46ee8-191818|9ea6f1-191818', 1.0, 0)
            if t[0] != 0:
                print('打怪1')
                dm.keypresschar('1')
                ##血河1技能不刷新图像
                n = 0
                while True:
                    if SW():
                        Duan()
                        break
                    else:
                        n += 1
                        Z = Zhao_Tu(1017, 345, 1264, 410, '失败.bmp')
                        if Z[0] != -1 or n > 100:  # 解决木桩问题
                            z = Zhao_Tu(220, 283, 910, 700, '放弃任务.bmp')
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
                            t = dm.FindColor(410, 0, 905, 148,
                                             'ff4444-000000|a46ee8-191818|9ea6f1-191818', 1.0, 0)

                            if t[0] == 0:
                                sleep(1)
                                break

            else:
                Ctf()
                sleep(2)




def jie_renwu(hwnd, str, msg):
    while True:
        z = Zhao_Tu(715, 526, 1021, 704, '提问.bmp')
        if z[0] != -1:
            mouse(z[1] - 300, z[2], 20, 10)
            sleep(xx())
            dm.SendString(hwnd, str)
            sleep(0.1)
            dm.keypresschar('enter')
            sleep(xx())
            z = dm.findstre(335, 207, 1002, 601, msg, '160.68.73-10.10.10', 0.95).split('|')
            sleep(0.5)
            if z[0] == "0":
                mouse(int(z[1]) + 10, int(z[2]) + 2, 5, 5)
                sleep(0.5)
                mouse(880, 92, 5, 5)
                print('去接任务')
                sleep(xx())
                break
        else:
            print("呼唤小精灵")
            mouse(1092, 9, 5, 5)
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
                if Jiemian[0] == -1:
                    tijiao = Zhao_Tu(933, 556, 1236, 700, '提交道具.bmp')
                    if tijiao[0] != -1:
                        mouse(tijiao[1], tijiao[2], 50, 5)
                    dm.movetoex(z[1] + 140, z[2] + 20, 15, 15)  # 背包第2格
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
                        dm.movetoex(z[1] + 190, z[2] + 20, 15, 15)  # 背包第3格
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
    sleep(0.5)
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
                if SW():
                    Duan()
                    break
                elif z == 0:
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


def Ti_Jiao1():
    z = Zhao_Tu(479, 242, 786, 433, '提交.bmp|提交1.bmp|提交2.bmp|')
    sleep(0.5)
    if z[0] != -1:
        dm.movetoex(z[1], z[2], 5, 5)
        sleep(0.1)
        dm.leftclick()


def zhangJian(hwnd):
    ziku = [['雪中送炭.bmp', XueZhong],
            ['资源援助.bmp', Yuan_Zhu],
            ['莫欺年少.bmp', MoQi],
            ['金蝉脱壳.bmp', JinChan],
            ["打草熏蛇.bmp", XunShe],
            ['断其喉舌.bmp|火眼金睛.bmp|千杯不醉.bmp|秋风落叶.bmp', Duan],
            ]
    print('当前--仗剑江湖')
    name = Get_Name(hwnd)
    logging.debug(name + "~~~" + "开始仗剑江湖")
    while True:
        Z = Ren_WU_Kuan()
        print('任务框', Z)
        if Z[0] == 0:
            z = Zhao_Tu(571, 311, 827, 540, '敖青云1.bmp')
            if z[0] != -1:
                print('接任务')
                dm.keypresschar('F')
            else:
                jie_renwu(hwnd, '萧姨', '萧姨')  # 点击寻路至萧姨/萧姨
            n = 0
            while True:
                z = Zhao_Tu(435, 314, 839, 565, '再见.bmp')
                zz = Zhao_Tu(435, 314, 839, 565, '仗剑江湖3.bmp|')
                if zz[0] == -1 and z[0] != -1:
                    print('任务完成')
                    logging.debug(name + "~~~" + "仗剑江湖完成")
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


def enChou(hwnd):
    enchou = [
        ["一探虚实1.bmp|瓦上君子1.bmp|牛刀杀鸡.bmp|驱虎呑狼.bmp", Wanc],
        ['先发制人.bmp', XianFa],
        ['趁火打劫.bmp|断敌一指.bmp|以眼还眼.bmp', Da_Jie],
        ['下马作威.bmp', Duan]

    ]
    print('当前--快意恩仇')
    name = Get_Name(hwnd)
    logging.debug(name + "~~" + "开始快意恩仇")
    while True:
        Z = Ren_WU_Kuan()
        # print('任务框', Z)
        if Z[0] == 0:  # 当前没任务，去接任务
            z = Zhao_Tu(571, 311, 827, 540, '敖青云.bmp|光云长.bmp|敖青云1.bmp')
            if z[0] != -1:
                dm.keypresschar('F')
            else:
                jie_renwu(hwnd, str="快意恩仇", msg='敖青云')
            n = 0
            while True:
                z = Zhao_Tu(435, 314, 839, 565, '我要进行修炼.bmp')
                zz = Zhao_Tu(435, 314, 839, 565, '快意恩仇.bmp|')
                if zz[0] == -1 and z[0] != -1:
                    print('任务完成')
                    logging.debug(name + "~~" + "快意恩仇完成")
                    return None
                elif zz[0] != -1:
                    mouse(zz[1], zz[2], 50, 5)
                    sleep(2)
                    zz1 = Zhao_Tu(1036, 511, 1261, 685, '接受.bmp|')
                    mouse(zz1[1], zz1[2], 15, 5)
                    sleep(0.5)
                    print('接到任务')
                    break
                elif n > 50:
                    break
                else:
                    n += 1
                    sleep(3)



        else:  # 有任务，执行任务
            for i in enchou:
                Z1 = Zhao_Tu(68, 113, 539, 279, i[0])
                # print(Z1)
                sleep(0.5)
                if Z1[0] != -1:
                    # print('当前任务{}'.format(i[0]))
                    i[1]()
                    sleep(xx())
                    break


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


def shiJian(hwnd):
    name = Get_Name(hwnd)
    while True:
        ZhanBao = Zhao_Tu(897, 276, 1284, 604, "战报.bmp|侠士.bmp|狂士.bmp")  # 这个判断必须准确
        ZhanGuo = Zhao_Tu(9, 28, 1245, 377, "试剑天下战报.bmp|侠士1.bmp|狂士1.bmp")
        zudui = Zhao_Tu(120, 50, 1189, 661, '离开队伍1.bmp|签到.bmp|庙会快捷采购.bmp|队伍1.bmp')
        if ZhanBao[0] == -1 and ZhanGuo[0] == -1 and zudui[0] == -1:  # 不在战场内也没有战报没有组队界面遮挡，判断一定在外面或者传送，报名
            print(name + "开始报名")
            if not PiPei(name):
                break

        elif ZhanGuo[0] != -1:  # 此时有战果，必然没有战报，点掉所有东西
            while True:
                XiTong = Zhao_Tu(134, 56, 1109, 660, '系统设置.bmp')
                if XiTong[0] != -1:
                    dm.keypresschar('esc')
                    print(name + '一把结束了')
                    logging.debug(name + "---" + "战场结束" + "---")
                    break
                else:
                    dm.keypresschar('esc')
                    sleep(1)
        elif zudui[0] != -1:
            print(name + "清理界面")
            dm.keypresschar('esc')
            sleep(0.5)
        else:  # 在战场中，有战报，没战果，两者不可能同时出现

            print(name + "战场中")
            A1(hwnd)
            sleep(0.5)


def Ji_He(hwnd):
    #哈哈哈哈
    dm.BindWindowEx(hwnd, 'dx2', 'dx2', 'dx', 'dx.public.disable.window.size', 101)
    name = Get_Name(hwnd)
    shiJian(hwnd)
    logging.debug(name + "---" + "战场打完了" + "---")
    yaBiao(hwnd)
    logging.debug(name + "---" + "押镖完了" + "---")
   # enChou(hwnd)
    zhangJian(hwnd)
    dm.SetWindowState(hwnd, 0)
    sleep(3)
    logging.debug(name + "----------------------退出游戏-----------------------------")
    tuichu = Zhao_Tu(329, 602, 874, 732, "退出游戏.bmp")
    if tuichu[0] != -1:
        mouse(tuichu[1], tuichu[2], 5, 5)


if __name__ == '__main__':
    hwnds = dm.EnumWindowByProcess("GacRunnerNG.exe", "逆水寒", "", 1).split(',')
    a, b = 1, 2
    bd = dm.BindWindowEx(hwnds[0], 'dx2', 'dx2', 'dx', 'dx.public.disable.window.size', 101)
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
