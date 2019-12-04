import win32com.client
from time import sleep,ctime,strftime,localtime
import random
import sys
from multiprocessing import Process

now=lambda :strftime("%X", localtime())
dm = win32com.client.Dispatch('dm.dmsoft')
g = dm.Reg("2244939288cfa31e5135147e45e56bbc65440c5b8c","")
def  ZaiXianJieTu(add,file_name,x1,y1,x2,y2):
    #Xm =dm.BindWindow(Mubiaochuangkou,"normal","normal","normal",0)
    sleep(1)
    dm.SetPath(add)
    l =dm.CapturePng(x1,y1,x2,y2,file_name)
    return l

    #dm.DeleteFile(file_name)
Sleep =lambda :random.randint(1,3)
def F():
    dm.MoveToEx(1108, 400, 30, 30)
    sleep(Sleep())
    dm.LeftClick()
    sleep(1)
    dm.keypress(70)
def Ctf():
    dm.keypresschar('ctrl')
    dm.keypresschar('f')


Zi_Ku =dm.SetDict(0,r"C:\Users\Administrator\Desktop\wenjian\新建文件夹\主线库.txt")
Tu_Ku =dm.SetPath(r'C:\Users\Administrator\Desktop\wenjian\图文件')
Zhao_Tu =lambda x1=881,y1=652,x2=1014,y2=735,file ="继续.bmp|继续1.bmp|继续2.bmp|继续3.bmp|继续4.bmp|",color ="36.2.87-180.5.60"\
                    :dm.FindPic(x1,y1,x2,y2,file,color,0.8,0)

Zhao_Zi =lambda x1=1009,y1=372,x2=1283,y2=606,color ='42.91.91-5.10.60,|36.2.87-180.5.60'\
                    :dm.OcrEx(x1,y1,x2,y2,color ,0.8).split('|')#  任务框加白色字体

Zhao_Se =lambda x1=1007,y1=375,x2=1295,y2=605,color ="bc7905-000000|f9b517-030303|feb817-202020|dda118-000000"\
                    :dm.FindColor(x1,y1,x2,y2,color, 1.0, 0)  #任务框
def S_W():
    S =Zhao_Tu(173,149,1149,655,'等待救援.bmp|等待救援1.bmp')
    if S[0]!=-1:
        while True:
            #Q=Zhao_Tu(334,153,947,560,'确定4.bmp|确定5.bmp')
            y=Zhao_Tu(173,149,1149,655,'原地疗伤.bmp|原地疗伤1.bmp|原地疗伤2.bmp|原地疗伤3.bmp|原地疗伤4.bmp|确定4.bmp|确定5.bmp')
            sleep(1)
            if y[0]!=-1:
                dm.movetoex(y[1],y[2],5,5)
                sleep(0.5)
                dm.leftclick()
                sleep(1)
                y = Zhao_Tu(173, 149, 1149, 655, '确定4.bmp|确定5.bmp')
                if y[0] != -1:
                    dm.movetoex(y[1], y[2], 5, 5)
                    sleep(0.5)
                    dm.leftclick()
                break
def Rool():
    R=Zhao_Tu(944,262,1264,460,'roll点.bmp')
    if R[0]!=-1:
        dm.keydownchar('ctrl')
        sleep(0.5)
        dm.keypresschar('r')
        sleep(0.5)
        dm.keyupchar('ctrl')
    Zui_Di = Zhao_Tu(3, 283, 445, 685, '竞拍.bmp')
    if Zui_Di[0]!=-1:
        dm.movetoex(283,210,5,5)  ###改XX坐标
        sleep(0.5)
        dm.leftclick()
        sleep(0.5)
        dm.keypresschar('enter')
def Zhao_DiTU(x1='', x2='', x3='',x4='',y1='',y2='', y3='', y4='',):#fuben外找地图
    dm.keypresschar('M')
    sleep(0.5)
    dm.moveto(933,37)
    sleep(1)
    dm.leftclick()
    sleep(1)
    dm.keypresschar(x1)
    sleep(0.5)
    dm.keypresschar(x2)
    sleep(0.5)
    dm.keypresschar(x3)
    sleep(0.5)
    dm.keypresschar(x4)
    sleep(0.5)
    dm.keypresschar('tab')
    sleep(0.5)
    dm.keypresschar(y1)
    sleep(0.5)
    dm.keypresschar(y2)
    sleep(0.5)
    dm.keypresschar(y3)
    sleep(0.5)
    dm.keypresschar(y4)
    sleep(0.5)

    dm.movetoex(1030,33, 5, 5)
    sleep(0.5)
    dm.leftclick()
    sleep(0.5)
    dm.keypresschar('M')
def Zhao_DiTU1(x1='', x2='', x3='',x4='',y1='',y2='', y3='', y4='',):  ##fuben内找地图
    dm.keypresschar('M')
    sleep(0.5)
    dm.moveto(759,114)
    sleep(1)
    dm.leftclick()
    sleep(1)
    dm.keypresschar(x1)
    sleep(0.5)
    dm.keypresschar(x2)
    sleep(0.5)
    dm.keypresschar(x3)
    sleep(0.5)
    dm.keypresschar(x4)
    sleep(0.5)
    dm.keypresschar('tab')
    sleep(0.5)
    dm.keypresschar(y1)
    sleep(0.5)
    dm.keypresschar(y2)
    sleep(0.5)
    dm.keypresschar(y3)
    sleep(0.5)
    dm.keypresschar(y4)
    sleep(0.5)

    dm.movetoex(859,106, 5, 5)
    sleep(0.5)
    dm.leftclick()
    sleep(0.5)
    dm.keypresschar('M')

def Ti_Jiao1():
    z=Zhao_Tu(479,242,786,433,'提交.bmp|提交1.bmp|提交2.bmp|')
    if z[0]!=-1:
        dm.movetoex(z[1],z[2],5,5)
        sleep(0.3)
        dm.leftclick()
        sleep(0.5)
        dm.movetoex(50, 50, 50,  50)
def Hu_Dongl():
    z=Zhao_Tu(1004,368,1275,697,'走就走.bmp|前往自在门.bmp|进入卧房1.bmp|我走了.bmp|修复名画.bmp|画中人.bmp|询问客人.bmp|'
                  '询问客人.bmp|崇宁四年.bmp|灭门案.bmp|楚相玉.bmp|十三元凶.bmp|'
                  '疑案.bmp|盛家庄.bmp|令牌.bmp|选择修行方向.bmp|我想选.bmp|'
                  '拿出四逆汤.bmp|上前迎战.bmp|递过竹哨.bmp|得罪.bmp|'
                  '拿出令牌.bmp|二哥得罪.bmp|拿出一百二十文.bmp|'
                  '好我来试试.bmp|接过密码锁.bmp|好我来试试.bmp|'
                  '扬州.bmp|再来再来.bmp|建康.bmp|得罪1.bmp|鼠.bmp|十年前.bmp|记住了.bmp|准备好了.bmp|'
                  '拿出一百文.bmp|门卫.bmp|前往故地.bmp|送我上塔顶.bmp|带我上去.bmp|'
                     '兔毫.bmp|拿出白纸扇.bmp|放下旧扇.bmp|包袱还给她.bmp|'
                     '递过扇子.bmp|递交字纸.bmp|递交给婆婆.bmp|听曲.bmp|落花记前踪.bmp|茶.bmp|'
                     '向阳.bmp|熙春.bmp|舞隐.bmp|眉山人.bmp|眉.bmp|山.bmp|苏.bmp|东.bmp|坡.bmp|出示令牌.bmp|递过茶业.bmp|递过笔墨.bmp||集会.bmp|接招.bmp'
                                '|好啊.bmp')
    if z[0]!=-1:
        dm.movetoex(z[1],z[2],50,20)
        sleep(0.5)
        dm.leftclick()
        sleep(0.5)
        dm.movetoex(50, 50, 50, 50)
    Z=Zhao_Tu(479,242,786,433,'提交.bmp|提交1.bmp|提交2.bmp|')
    if Z[0]!=-1:
        dm.movetoex(Z[1],Z[2],10,10)
        sleep(0.5)
        dm.LeftClick()
        sleep(0.5)
        dm.movetoex(50, 50, 50, 50)
def WangQ():
    z=Zhao_Tu(25,34,1259,551,'晚晴之情.bmp|百合姑娘.bmp|面具.bmp|白发.bmp|好.bmp|等等.bmp|沈云山.bmp|每半年轮值一次.bmp|五招.bmp|'
                  '日短夜长.bmp|十二位.bmp|出门是敌人.bmp|'
                  '开盒子.bmp|四逆汤.bmp|交情.bmp|我不.bmp|蒲苇.bmp|不是.bmp|'
                  '情侣南线.bmp||告诉.bmp|不告诉.bmp|告诉1.bmp|告诉2.bmp|莲塘.bmp|寒酸.bmp|晏几道.bmp|我不太记得了.bmp|我能挺住.bmp|'
                   '明公胜.bmp|孤山胜.bmp|孤山胜.bmp|二千两.bmp|苏1.bmp|大苏.bmp||好吃.bmp|赞同.bmp|维护.bmp|瞒着.bmp|多了.bmp')

    if z[0]!=-1:
        dm.movetoex(z[1],z[2],5,5)
        sleep(.65)
        dm.leftclick()
        sleep(0.5)
        dm.movetoex(50, 50, 50, 50)
def Shen_Ji_JiNeng():
    z=Zhao_Tu(1004, 368, 1275, 697, '升级.bmp')
    if z[0]!=-1:

        Hu_Dongl()
        sleep(2)
    zz = Zhao_Tu(224, 70, 689, 666, '可升级.bmp|')
    while zz[0] !=-1:
        dm.moveto(zz[1],zz[2])
        dm.leftclick()

        sleep(Sleep())
        dm.movetoex(652, 135, 5, 6)
        count =1
        while count<8:
            s=random.randint(1,5)/8
            dm.leftclick()
            sleep(s)
            dm.leftclick()
            sleep(s)
            dm.leftclick()
            sleep(s)
            zzz = Zhao_Tu(224, 70, 689, 666, '确定1.bmp|')
            sleep(1)
            if zzz[0]!=-1:
                dm.KeyPressChar("enter")
            dm.MoveR(0, 70)
            z = Zhao_Tu(224, 70, 689, 666, '大于20000.bmp')
            if z[0]!=-1:
                break
            count += 1
        zz = Zhao_Tu(224, 70, 689, 666, '可升级.bmp|')
        z = Zhao_Tu(224, 70, 689, 666, '大于20000.bmp')
        if z[0] != -1:
            break
    dm.keypresschar('esc')
    sleep(s)
    dm.keypresschar('esc')
    sleep(s)
    dm.keypresschar('esc')
    sleep(s)
    dm.keypresschar('esc')
def Wu_Ming():
    dm.keypress(27)
    sleep(0.5)
    dm.moveto(1250,385)
    sleep(0.5)
    dm.leftclick()
def AA():
    dm.keydownchar(1)
    sleep(5)
    dm.keyupchar(1)
def yaoseng30():

    l=['野利广元.bmp','修贤.bmp','秒明.bmp','圣量.bmp|','净真.bmp|','贞庆.bmp|']
    ll=''
    for i in l:
        z=Zhao_Tu(934,500,1258,701,i)
        if z[0]!=-1:
            ll=i
            dm.keypresschar('esc')
            break
    if ll=='野利广元.bmp':
        ll='野利广元1.bmp'
    if ll=='秒明.bmp':
        ll='妖僧秒明.bmp'
    if ll=='圣量.bmp|':
        ll='妖僧圣量.bmp'
    if ll=='净真.bmp|':
        ll='妖僧净真.bmp'
    if ll =='贞庆.bmp|':
        ll ='贞庆1.bmp|'
    if ll =='修贤.bmp':
        ll ='妖僧修贤.bmp'

    zu = Zhao_Tu(134, 56, 1109, 660, '便捷组队.bmp')
    sleep(1)
    if zu[0] == -1:
        dm.keypresschar('t')
        sleep(1)
    Mu_Biao = Zhao_Tu(14, 55, 1156, 670, ll)
    print( Mu_Biao)
    sleep(1)
    while Mu_Biao[0]==-1:
        dm.movetoex(236,226,110,200)
        sleep(0.5)
        dm.WheelDown()
        sleep(2)
        Mu_Biao = Zhao_Tu(14, 55, 1156, 670, ll)
        print(Mu_Biao)
    dm.movetoex( Mu_Biao[1],Mu_Biao[2],5,5)
    sleep(0.9)
    dm.leftclick()
    t=Zhao_Tu(14, 55, 1156, 670, '自动匹配.bmp')
    if t[0]!=-1:
        dm.movetoex(t[1],t[2],5,5)
        sleep(1.2)
        dm.leftclick()
    sleep(.8)
    dm.keypresschar('t')
    while True:
        sleep(5)
        manyuan5 = Zhao_Tu(32, 149, 236, 210, '铁衣.bmp|神像.bmp|龙吟.bmp|素问.bmp|九灵1.bmp|血河.bmp')
        if manyuan5[0]!=-1:
            dm.keypresschar('g')
            sleep(60)
            break

    while True:
            z=Zhao_Tu(952, 345, 1263, 678,'急切询问.bmp')
            if z[0]!=-1:
                break
            dm.keypresschar('tab')
            sleep(1)
            t = dm.FindColor(425,55,866,120, 'ff4444-000000|ffe96e-000000|b479ff-000000', 1.0, 0)
            Rool()
            #print('一')
            if t[0]!=0:
                dm.keypresschar('1')
                dm.IsDisplayDead(417, 700, 444, 726, 15)  ##除铁衣外   用来寻路。每个职业不一样，需要解决问题
                while True:
                    S_W()
                    dm.keydownchar('1')
                    l=random.randint(2,5)
                    dm.keypresschar(l)
                    t = dm.FindColor(519, 67, 582, 94, 'ff4444-000000|ffe96e-000000|b479ff-000000', 1.0, 0)
                    sleep(0.3)
                    #print('二')
                    if t[0]==0:
                        dm.keyupchar('1')
                        #print('yi')
                        break
            else:
                sleep(3)
def Ping_Cou():
    z=Zhao_Tu(955,591,1297,688,'修复名画.bmp')
    dm.movetoex(z[1],z[2],50,10)
    sleep(0.5)
    dm.leftclick()
    sleep(1)
    dm.moveto(703,440)
    #按住鼠标
    dm.LeftDown()
    sleep(0.5)
    dm.moveto(510,564)
    dm.leftclick()
    dm.LeftUp()
    sleep(0.5)

    dm.moveto(704,556)
    dm.LeftDown()
    sleep(0.5)
    dm.moveto(229,630)
    dm.leftclick()
    dm.LeftUp()
    sleep(0.5)

    dm.moveto(923,265)
    dm.LeftDown()
    sleep(0.5)
    dm.moveto(608,400)
    dm.leftclick()
    dm.LeftUp()
    sleep(.5)

    dm.movetoex(747,587,60,10)
    sleep(.5)
    dm.leftclick()
    sleep(0.5)

    dm.movetoex(834, 378, 3, 3)
    dm.leftdown()
    dm.mover(5, 5)
    sleep(0.5)
    dm.movetoex(463, 493, 5, 5)
    dm.leftclick()
    dm.leftup()
    sleep(0.6)
    dm.movetoex(745,586,50,20)
    dm.leftclick()
def A ():
    name=''
    l=[['九灵.bmp','九灵']]
    for i in l:
        z=Zhao_Tu(83,67,109,89,i[0])
        if z[0]!=-1:
            name=i[1]

    while True:
        if name == '九灵':
            Z = Zhao_Tu(260, 58, 463, 134, '宝宝.bmp')
            if Z[0] == -1:
                dm.keypresschar('f1')
                sleep(1)
                dm.keypresschar('f2')
                sleep(1)
                dm.keypresschar('f3')
                sleep(1)
        dm.keypresschar('tab')
        sleep(1)
        t = dm.FindColor(425, 55, 866, 120, 'ff4444-000000|ffe96e-000000|b479ff-000000', 1.0, 0)
        # print('一')
        if t[0] != 0:
            dm.keypresschar('1')
            while True:
                S_W()
                dm.keydownchar('1')
                z=dm.IsDisplayDead(417, 700, 444, 726, 5)  ##除铁衣外   用来寻路。每个职业不一样，需要解决问题
                if z==1:
                    l = random.randint(2, 5)
                    dm.keypresschar(l)
                t = dm.FindColor(519, 67, 582, 94, 'ff4444-000000|ffe96e-000000|b479ff-000000', 1.0, 0)
                sleep(0.3)
                # print('二')
                if t[0] == 0:
                    dm.keyupchar('1')
                    # print('yi')
                    break
        else:
            Ctf()
            break
def Bu_Yu():
    dm.MoveToEx(1221, 421, 40, 20)
    sleep(Sleep())
    dm.LeftClick()
    sleep(Sleep())
    dm.LeftClick()
    sleep(5)
    dm.keypress(70)
def Bi_Yun():
    Ctf()
    sleep(5)
    Ctf()
    sleep(3)
    dm.MoveToEx(1221, 421, 40, 20)
    sleep(1)
    dm.LeftClick()
    dm.movetoex(1063,492,5,5)
    sleep(0.5)
    dm.LeftClick()
    sleep(5)
    dm.keypress(70)

def Yun_Qi():
    dm.MoveToEx(1221, 421, 40, 20)
    sleep(Sleep())
    dm.LeftClick()
    sleep(Sleep())
    dm.LeftClick()
    sleep(3)
    dm.keypress(123)
    sleep(0.5)
    dm.movetoex(913,207,30,60)
    sleep(Sleep())
    dm.LeftClick()
def Ji_Fei():
    dm.MoveToEx(1221, 421, 40, 20)
    sleep(Sleep())
    dm.LeftClick()
    dm.keydown(53)
    sleep(3)
    dm.keyup(53)
def Qian_Ma():
        ll = Zhao_Tu(528, 527, 873, 593, '牵马1.bmp')
        if ll[0] == -1:
            dm.MoveToEx(1221, 421, 40, 20)
            sleep(Sleep())
            dm.LeftClick()
            dm.keypress(85)
            sleep(1)
        else:
            dm.movetoex(654, 547, 30, 15)
            sleep(1)
            dm.leftclick()

def Qi_Ma():
        dm.MoveToEx(1221, 421, 40, 20)
        sleep(Sleep())
        dm.LeftClick()
        dm.keypress(122)
        sleep(Sleep())
        dm.keypress(116)
        sleep(Sleep())
def Qing_Ya_Shu():
    dm.movetoex(487,355,50,10)
    sleep(0.5)
    dm.leftclick()
    sleep(5)
    dm.movetoex(487, 355, 50, 10)
    sleep(0.5)
    dm.leftclick()
    sleep(5)
    dm.movetoex(486,29, 50, 10)
    sleep(0.5)
    dm.leftclick()
    dm.movetoex(584, 565, 50, 10)
    sleep(0.5)
    dm.leftclick()
def Za_Cao():
    dm.movetoex(489,184,400,300)
    sleep(0.3)
    dm.leftclick()
    dm.keypress(49)
    sleep(0.3)
    dm.keypress(49)
def Fang_Zong():
    while True:
        ll = Zhao_Tu(782,207,962,300, '芳踪.bmp')
        if ll[0]==-1:
            dm.keypresschar('k')
            sleep(1)
            ll = Zhao_Tu(782,207,962,300, '芳踪.bmp')
            break

    dm.moveto(ll[1] + 20, ll[2] - 20)
    dm.leftdown()
    dm.mover(5,5)
    sleep(1)
    dm.keypresschar('k')
    dm.movetoex(861,658,20,20)
    sleep(1)
    dm.leftclick()
    dm.leftup()
    sleep(1)
    dm.keypresschar('F10')
    sleep(3)

def Wu_Xue():
    dm.movetoex(948,28,10,10)
    dm.leftclick()
    sleep(2)
    zz =Zhao_Tu(508,370,1056,723, '开始试炼.bmp|进入试炼峰.bmp')
    if zz !=-1:
        dm.moveto(zz[1],zz[2])
        dm.leftclick()
        sleep(5)
        while True:
            z=Zhao_Tu (438, 346, 850, 490, '断招.bmp')
            sleep(5)
            if z[0]!=-1:
                dm.keypress(49)
                sleep(0.2)
                dm.keypress(8)
                sleep(5)
                dm.keypress(49)
                sleep(0.2)
                dm.keypress(8)
                z = Zhao_Tu(438, 346, 850, 490, '断招.bmp')
                if z[0] == -1:
                    break
def Zuo_Xia():
    dm.keydown(17)
    dm.keypress(70)
    dm.keyup(17)
    sleep(1)
    dm.movetoex(602,366,20,20)
    sleep(0.5)
    dm.leftclick()
def Meng_Pang():
    dm.keydown(17)
    dm.keypress(70)
    dm.keyup(17)
    sleep(2)
    dm.movetoex(658,262,30,30)
    sleep(1)
    dm.leftclick()
def Luoxia():
    dm.keypress(123)
    sleep(0.5)
    dm.movetoex(822,220, 30, 60)
    sleep(Sleep())
    dm.LeftClick()
def Wang_Qi():
    while True:
        Z=Zhao_Tu(444,197,1002,503,'望气1.bmp')
        if Z[0]==-1:
            dm.keypresschar('k')
            sleep(1)
        else:
            break
    sleep(.8)
    dm.movetoex(Z[1],Z[2],5,5)
    sleep(0.8)
    dm.leftdown()
    dm.mover(15,15)
    sleep(0.2)
    dm.keypresschar('k')
    sleep(0.7)
    dm.movetoex(529,659,10,10)
    dm.leftclick()
    dm.leftup()
    sleep(1)
    dm.keypresschar('f4')
def Lie_Hu():
    dm.keypresschar('f12')
    sleep(2)
    l=Zhao_Tu(803,121,1244,477,'猎虎1.bmp')
    dm.movetoex(l[1],l[2],5,5)
    sleep(0.5)
    dm.leftclick()
def Xie():
    Ctf()
    sleep(2)
    dm.movetoex(707,342,10,10)
    sleep(0.5)
    dm.leftclick()
    sleep(2)
def S():
    Zhao_DiTU('6','0','5','','1','8','8','')
    while True:
        Z = Zhao_Tu(541, 340, 764, 555, '对话图标.bmp')
        if Z[0]!=0:
            sleep(1)
            dm.keypresschar('f')
            break
def Sheng_suo():
    Zhao_DiTU('3','9','9','','2','7','7','')
    sleep(2)
    dm.keypresschar('f')
    sleep(3)
    Zhao_DiTU('4', '0', '3', '', '2', '7', '5', '')
    sleep(2)
    dm.keypresschar('f')
    sleep(3)
    Zhao_DiTU('4', '0', '5', '', '2', '7', '6', '')
    sleep(2)
    dm.keypresschar('f')
    sleep(3)
    Zhao_DiTU('4', '0', '3', '', '2', '7', '8', '')
    sleep(2)
    dm.keypresschar('f')
    sleep(3)
def Pang_bian():
    dm.movetoex(615,504,50,40)
    sleep(0.5)
    dm.leftclick()
def YFang():
    z=Zhao_Tu(952, 345, 1263, 678,'营房.bmp|衣服2.bmp')
    dm.movetoex(z[1],z[2],5,5)
    sleep(0.5)
    dm.leftclick()
def Zhui_Ji():
    Zhao_DiTU('5','5','1','','5','4','3','')
    sleep(40)
    while True:
        dm.keypresschar('tab')
        sleep(1)
        t = dm.FindColor(425, 55, 866, 120, 'ff4444-000000|ffe96e-000000|b479ff-000000', 1.0, 0)
        # print('一')
        if t[0] != 0:
            dm.keypresschar('1')
            dm.IsDisplayDead(417, 700, 444, 726, 15)  ##除铁衣外   用来寻路。每个职业不一样，需要解决问题
            while True:
                S_W()
                dm.keydownchar('1')
                l = random.randint(2, 5)
                dm.keypresschar(l)
                t = dm.FindColor(519, 67, 582, 94, 'ff4444-000000|ffe96e-000000|b479ff-000000', 1.0, 0)
                sleep(0.3)
                # print('二')
                if t[0] == 0:
                    dm.keyupchar('1')
                    # print('yi')
                    break
        Z=Zhao_Tu(952, 345, 1263, 678,'追击辽兵.bmp')
        if Z[0]==-1:
            break
def JinChuan():
    l=[['3','8','3','','4','7','1',''], ['3','8','4','','4','7','4','']   ,['3','8','7','','4','7','4',''],

     ['3','8','4','','4','7','1',''],['3','8','9','','4','6','8','']]
    for i in l:
        Zhao_DiTU(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7])
        sleep(2)
        while True:
            dm.movetoex(625,338, 80, 80)
            sleep(2)
            s = dm.findstr(415,176,896,578, '受伤的宋兵', '202.68.92-1.5.60', 0.6, '', '')
            # print(s)
            if s != -1:
                dm.leftclick()
                sleep(1)
                dm.keypresschar('f')
                sleep(3)
                break
    

def YLD():
    dm.keypresschar('1')
def Xun_Wen():
    name = ''
    l = [['九灵.bmp', '九灵']]
    for i in l:
        z = Zhao_Tu(83, 67, 109, 89, i[0])
        if z[0] != -1:
            name = i[1]
    while True:
        Ctf()
        if name == '九灵':
            Z = Zhao_Tu(260, 58, 463, 134, '宝宝.bmp')
            if Z[0] == -1:
                dm.keypresschar('f1')
                sleep(1)
                dm.keypresschar('f2')
                sleep(1)
                dm.keypresschar('f3')
                sleep(1)
        dm.keypresschar('tab')
        sleep(1)
        t = dm.FindColor(425, 55, 866, 120, 'b479ff-000000', 1.0, 0)
        # print('一')
        if t[0] != 0:
            dm.keypresschar('1')
            dm.IsDisplayDead(417, 700, 444, 726, 15)  ##除铁衣外   用来寻路。每个职业不一样，需要解决问题
            while True:
                S_W()
                dm.keydownchar('1')
                l = random.randint(2, 5)
                dm.keypresschar(l)
                t = dm.FindColor(519, 67, 582, 94, 'b479ff-000000', 1.0, 0)
                sleep(0.3)
                # print('二')
                if t[0] == 0:
                    dm.keyupchar('1')
                    # print('yi')
                    break
        z=Zhao_Tu(952, 345, 1263, 678,'询问时机.bmp|萧铭律.bmp')
        if z[0]==-1:
            break
def  Q_D():
    z=Zhao_Tu(475,497,885,684,'确定选择.bmp')
    dm.movetoex(z[1],z[2],10,10)
    sleep(0.5)
    dm.leftclick()
    sleep(1)
    dm.keypresschar('enter')
def Qiu_Long():
    dm.keypresschar('f12')
    sleep(2)
    l=Zhao_Tu(803,121,1244,477,'缚虎囚龙1.bmp')
    dm.movetoex(l[1],l[2],5,5)
    sleep(0.5)
    dm.leftclick()
def Shang_Yi():
    Zhao_DiTU1('1','3','7','','1','1','0','')
    sleep(15)
    while True:
        dm.movetoex(513,363,80,80)
        sleep(2)
        z=Zhao_Tu(561,267,901,578,'对话图标.bmp')
        if z[0]!=-1:
            dm.keypresschar('f')
            sleep(3)
            break
def ShenRuDaLao():
    Zhao_DiTU1('1','2','4','','1','8','8','')
    sleep(30)


def shengtai():
    z = Zhao_Tu(952, 345, 1263, 678, '升台机关.bmp')
    sleep(0.5)
    dm.movetoex(z[1], z[2], 5, 5)
    sleep(0.5)
    dm.leftclick()
    sleep(3)
    dm.movetoex(557, 280, 60, 60)
    sleep(0.5)
    dm.leftclick()


def Z_X():
    while True:
        dm.movetoex(607, 353, 10, 10)
        sleep(.5)
        dm.leftclick()
        sleep(2)
        z = Zhao_Tu(452, 50, 795, 159, '乌云.bmp')
        if z[0] != -1:
            dm.keypresschar('f')
            sleep(3)
            break

def  JinGong():
    name = ''
    l = [['九灵.bmp', '九灵']]
    for i in l:
        z = Zhao_Tu(83, 67, 109, 89, i[0])
        if z[0] != -1:
            name = i[1]

    while True:
        Z=Zhao_Tu(952, 345, 1263, 678,'进攻.bmp|击退辽兵.bmp|辽军大将.bmp')
        if Z[0]==-1:
            break
        else:
            if name == '九灵':
                Z = Zhao_Tu(260, 58, 463, 134, '宝宝.bmp')
                if Z[0] == -1:
                    dm.keypresschar('f1')
                    sleep(2)
                    dm.keypresschar('f2')
                    sleep(1)
                    dm.keypresschar('f3')
                    sleep(1)

            dm.keypresschar('tab')
            sleep(1)
            t = dm.FindColor(425, 55, 866, 120, 'ff4444-000000|ffe96e-000000|b479ff-000000', 1.0, 0)
            # print('一')
            if t[0] != 0:
                dm.keypresschar('1')
                dm.IsDisplayDead(417, 700, 444, 726, 15)  ##除铁衣外   用来寻路。每个职业不一样，需要解决问题
                while True:
                    S_W()
                    dm.keydownchar('1')
                    l = random.randint(2, 5)
                    dm.keypresschar(l)
                    t = dm.FindColor(519, 67, 582, 94, 'ff4444-000000|ffe96e-000000|b479ff-000000', 1.0, 0)
                    sleep(0.3)
                    # print('二')
                    if t[0] == 0:
                        dm.keyupchar('1')
                        # print('yi')
                        break
def Shao():
    Ctf()
    sleep(3)
    dm.keypresschar('1')
def WEI_Du():
    Ctf()
    sleep(3)
    dm.keypresschar('f')
def Tou_Xi():
    Zhao_DiTU('6','7','0','','1','8','0','')
    sleep(5)
    while True:
        Z=Zhao_Tu(643,218,931,439,'冷呼儿.bmp')
        print(Z)
        if Z[0]!=-1:
            dm.movetoex(Z[1],Z[2]+50,10,10)
            sleep(0.5)
            dm.leftclick()
            sleep(0.5)
            dm.keypresschar('f')
            sleep(2)
            break
        else:
            dm.keypresschar('w')
            sleep(2)
def  Luozhuo():
    Ctf()
    sleep(3)
    dm.movetoex(644,396,10,5)
    sleep(0.5)
    dm.leftclick()
    sleep(0.5)
def Peng_Xian():
    dm.keypresschar('f12')
    sleep(7)
    l=Zhao_Tu(817,224,1242,586,'烹鲜醉客1.bmp')
    dm.movetoex(l[1],l[2],5,5)
    sleep(0.5)
    dm.leftclick()
    sleep(0.5)
    dm.keypresschar('f12')

def Ru_Mu():
    while True:
        dm.keydownchar('w')
        sleep(1.5)
        dm.keyupchar('w')
        dm.keydownchar('a')
        sleep(1.5)
        dm.keyupchar('a')
        dm.keydownchar('d')
        sleep(0.8)
        dm.keyupchar('d')
        dm.keydownchar('x')
        sleep(1)
        dm.keyupchar('x')
        sleep(2)
        Z=Zhao_Tu(496,475,873,694,'写下一个.bmp')
        if Z[0]!=-1:
            dm.movetoex(Z[1],Z[2],10,10)
            sleep(0.5)
            dm.leftclick()
            break
        else:
            Z = Zhao_Tu(496, 475, 873, 694, '从头再来.bmp')
            dm.movetoex(Z[1], Z[2], 10, 10)
            sleep(0.5)
            dm.leftclick()
    while True:
        dm.keydownchar('w')
        sleep(1.5)
        dm.keyupchar('w')
        dm.keydownchar('a')
        sleep(2.5)
        dm.keyupchar('a')
        dm.keydownchar('f')
        sleep(1)
        dm.keyupchar('f')
        dm.keydownchar('z')
        sleep(1.5)
        dm.keyupchar('z')
        sleep(2)
        Z=Zhao_Tu(496,475,873,694,'写下一个.bmp')
        if Z[0]!=-1:
            dm.movetoex(Z[1],Z[2],10,10)
            sleep(0.5)
            dm.leftclick()
            break
        else:
            Z = Zhao_Tu(496, 475, 873, 694, '从头再来.bmp')
            dm.movetoex(Z[1], Z[2], 10, 10)
            sleep(0.5)
            dm.leftclick()
    while True:
        dm.keydownchar('w')
        sleep(1.5)
        dm.keyupchar('w')
        dm.keydownchar('a')
        sleep(1.8)
        dm.keyupchar('a')
        dm.keydownchar('r')
        sleep(1)
        dm.keyupchar('r')
        dm.keydownchar('z')
        sleep(1)
        dm.keyupchar('z')
        sleep(2)
        Z=Zhao_Tu(496,475,873,694,'写下一个.bmp')
        if Z[0]!=-1:
            dm.movetoex(Z[1],Z[2],10,10)
            sleep(0.5)
            dm.leftclick()
            sleep(2)
            break
        else:
            Z = Zhao_Tu(496, 475, 873, 694, '从头再来.bmp')
            dm.movetoex(Z[1], Z[2], 10, 10)
            sleep(0.5)
            dm.leftclick()
    while True:
        dm.keydownchar('w')
        sleep(1.5)
        dm.keyupchar('w')
        dm.keydownchar('s')
        sleep(2)
        dm.keyupchar('s')
        dm.keydownchar('r')
        sleep(1)
        dm.keyupchar('r')
        dm.keydownchar('x')
        sleep(1)
        dm.keyupchar('x')
        sleep(2)
        Z=Zhao_Tu(496,475,873,694,'完成.bmp')
        if Z[0]!=-1:
            dm.movetoex(Z[1],Z[2],10,10)
            sleep(0.5)
            dm.leftclick()
            sleep(2)
            break
        else:
            Z = Zhao_Tu(496, 475, 873, 694, '从头再来.bmp')
            dm.movetoex(Z[1], Z[2], 10, 10)
            sleep(0.5)
            dm.leftclick()
def Tang_Qian():
    dm.keypresschar('f12')
    sleep(7)
    l=Zhao_Tu(817,224,1242,586,'堂前风1.bmp')
    dm.movetoex(l[1],l[2],5,5)
    sleep(0.5)
    dm.leftclick()
    sleep(0.5)
    dm.keypresschar('f12')
def Tuikai():
    Ctf()
    sleep(2)
    dm.movetoex(546,306,70,30)
    sleep(0.5)
    dm.leftclick()
def GuangBi():
    dm.movetoex(643,428, 20, 30)
    sleep(0.5)
    dm.leftclick()
def Guang():
    Zhao_DiTU1('1','0','9','','1','9','9','')
    sleep(3)
    dm.movetoex(643,392, 20, 30)
    sleep(0.5)
    dm.leftclick()


def Guang1():
    Zhao_DiTU1('1', '0', '9', '', '1', '9', '9', '')
    sleep(3)
    dm.movetoex(643, 392, 20, 30)
    sleep(0.5)
    dm.leftclick()
    sleep(0.5)
    Zhao_DiTU1('1', '2', '8', '', '1', '9', '6', '')

def Tong_Da():
    dm.keypresschar('1')
    sleep(.65)
    dm.keypresschar('2')
    sleep(.65)
    dm.keypresschar('3')
    sleep(.65)
def ZUOguoqu():
    dm.movetoex(632,376,20,30)
    sleep(.65)
    dm.leftclick()

def Chuan_Gong():
    dm.keypresschar('tab')
    sleep(1)
    t = dm.FindColor(425, 55, 866, 120, 'ff4444-000000|ffe96e-000000|b479ff-000000', 1.0, 0)
    # print('一')
    if t[0] != 0:
        dm.keypresschar('1')
    else:
        dm.keypresschar('m')
        sleep(.65)
        dm.movetoex(569,258,20,30)
        sleep(.65)
        dm.leftclick()
        sleep(2)
        dm.keypresschar('m')
        sleep(.65)
        dm.keypresschar('shift')
        dm.keypresschar('w')
        dm.keypresschar('space')

def Chu_Yun():
    dm.keypresschar('f12')
    sleep(0.5)
    dm.movetoex(55,245,400,300)
    sleep(2)
    l=Zhao_Tu(804,206,1259,597,'初云装1.bmp')
    dm.movetoex(l[1],l[2],5,5)
    sleep(0.5)
    dm.leftclick()
    sleep(0.5)
    dm.keypresschar('f12')

def WEI_Zhi():
    Zhao_DiTU1('1','6','4','','1','2','7','')
    sleep(5)
    dm.movetoex(521,457,5,5)
    sleep(0.5)
    dm.leftclick()
def WEI_Zhi1():
    Ctf()
    sleep(3)
    dm.movetoex(942,705, 5, 5)
    sleep(0.5)
    dm.leftclick()
    sleep(1)
    dm.movetoex(940,666, 15, 15)
    sleep(0.5)
    dm.leftclick()
    sleep(1)
    dm.movetoex(644,434, 5, 5)
    sleep(0.5)
    dm.leftclick()
    dm.movetoex(942, 705, 5, 5)
    sleep(0.5)
    dm.leftclick()
    sleep(0.5)
    dm.movetoex(944,665, 5, 5)
    sleep(0.5)
    dm.leftclick()
def WEI_Zhi2():
    Ctf()
    sleep(3)
    dm.movetoex(942,705, 5, 5)
    sleep(0.5)
    dm.leftclick()
    sleep(1)
    dm.movetoex(940,666, 15, 15)
    sleep(0.5)
    dm.leftclick()
    sleep(1)
    dm.movetoex(609,502, 15, 15)
    sleep(0.5)
    dm.leftclick()
    dm.movetoex(942, 705, 5, 5)
    sleep(0.5)
    dm.leftclick()
    sleep(0.5)
    dm.movetoex(944,665, 5, 5)
    sleep(0.5)
    dm.leftclick()
    sleep(2)
def Xiu_Yao_Zhen():
    dm.keypresschar('b')
    sleep(1)
    z=Zhao_Tu(482,80,1236,714,'任务.bmp')
    sleep(0.5)
    dm.movetoex(z[1],z[2],5,5)
    sleep(0.5)
    dm.leftclick()
    sleep(0.5)
    dm.movetoex(z[1]+106,z[2]-184,5,5)
    sleep(2)
    Z=Zhao_Tu(482,80,1236,714,'筝弦.bmp')
    while Z[0]==-1:
        dm.mover(50,0)
        sleep(2)
        Z = Zhao_Tu(482, 80, 1236, 714, '筝弦.bmp')
    dm.rightclick()
    Zz = Zhao_Tu(482, 80, 1236, 714, '瑶筝.bmp')
    while Zz[0] == -1:
        dm.mover(50, 0)
        sleep(2)
        Zz = Zhao_Tu(482, 80, 1236, 714, '瑶筝.bmp')
    dm.leftclick()
    sleep(0.5)
    dm.keypresschar('b')
def YouChuan():
    dm.keypresschar('1')
    sleep(3)
def  Dui_Zhi():
    Z=Zhao_Tu(402,65,972,542,'曲和星.bmp')
    if Z[0]!=-1:
        sleep(1.8)
        dm.movetoex(Z[1],Z[2]+50,20,20)
        sleep(1.8)
        dm.leftclick()
    else:
        dm.keypresschar('w')
        sleep(2)

def ZhuiTan():
    while True:
        dm.keypresschar('t')
        sleep(1)
        Z = Zhao_Tu(730, 492, 1069, 671, '创建队伍.bmp')
        if Z[0]!=-1:
            dm.movetoex(Z[1], Z[2], 10, 10)
            sleep(1)
            dm.leftclick()
            sleep(1)
            dm.keypresschar('esc')
            break
        z=Zhao_Tu(480,93,897,217,'队伍.bmp')
        if z[0]!=-1:
            sleep(1)
            dm.keypresschar('esc')
            break
    sleep(1)
    dm.keypresschar('f')
def Mai_Jiu():
    Z=Zhao_Tu(230,76,880,453, '买酒.bmp')
    sleep(1)
    dm.movetoex(Z[1],Z[2],10,10)
    sleep(1)
    dm.rightclick()
    sleep(1)
    dm.keypresschar('esc')
def KanTu():
    for i in range(1,5):
        dm.movetoex(156,114,100,300)
        sleep(0.5)
        dm.leftdown()
        sleep(0.5)
        dm.movetoex(1065,111, 50, 300)
        sleep(0.5)
        dm.leftclick()
        sleep(0.5)
        dm.leftup()

def HongShao():
    Zhao_DiTU1('1','1','1','','1','3','7','')
    sleep(1)
    dm.keypresschar('f')
    sleep(3)
def Duo_Bi():
    while True:
        Ctf()
        sleep(1)
        dm.keypresschar('1')
        sleep(10)
        z = Zhao_Tu(952, 345, 1263, 678, '躲避和尚.bmp|躲避和尚1.bmp')
        if z[0]==-1:
            break
def Mu_Ji():
    dm.keypresschar('f12')
    sleep(0.5)
    dm.movetoex(55,245,400,300)
    sleep(2)
    l=Zhao_Tu(804,206,1259,597,'草帽木屐1.bmp')
    dm.movetoex(l[1],l[2],5,5)
    sleep(0.5)
    dm.leftclick()
    sleep(0.5)
    dm.keypresschar('f12')
def Gan_Chu():
    Zhao_DiTU1('1','4','3','','1','6','7','')
    sleep(5)
    dm.keypresschar('f')
    Zhao_DiTU1('1', '6', '3', '', '2', '0', '0', '')
    sleep(10)
    dm.keypresschar('f')
    Zhao_DiTU1('1', '3', '2', '', '1', '7', '4', '')
    sleep(10)
    dm.keypresschar('f')
def Xie1():
    Ctf()
    sleep(2)
    dm.movetoex(723,466,200,100)
    sleep(0.5)
    dm.leftclick()
    sleep(2)
def  Jie_Ren_Wu(i):
    sleep(1)
    Z = Zhao_Tu(49,67,551,289, '任务列表.bmp')
    print('一',Z)
    if Z[0]==-1:
        dm. keypresschar('l')
    sleep(1)
    z=Zhao_Tu(79,72,684,299,'山雨欲来.bmp|山雨欲来1.bmp')
    print('二',z)
    if z[0]!=-1:
        sleep(0.5)
        dm.movetoex(z[1],z[2],10,10)
        sleep(0.5)
        dm.leftclick()
    Mu_Biao=Zhao_Tu(15,115,662,659,i)
    C=0
    while True:
        dm.movetoex(z[1]+20,z[2]+100, 110, 200)
        sleep(0.5)
        dm.WheelDown()
        C+=1
        sleep(2)
        Mu_Biao = Zhao_Tu(15, 115, 662, 659, i)
        print(i)
        print(Mu_Biao)
        if Mu_Biao[0]!=-1:
            dm.movetoex(Mu_Biao[1],Mu_Biao[2],10,10)
            sleep(0.5)
            dm.leftclick()
            sleep(0.5)

            l = Zhao_Tu(230, 334, 1057, 704, '领取任务.bmp')
            print(l)
            if l[0]!=-1:
                dm.movetoex(l[1], l[2], 10, 10)
                sleep(0.5)
                dm.leftclick()
                dm.keypresschar('esc')
                sleep(1)
                while True:
                        Z=Zhao_Tu(937,457,1277,731,'接收.bmp|落花记前踪.bmp|灵隐求鱼.bmp')
                        if Z[0]!=-1:
                            dm.movetoex(Z[1],Z[2],5,5)
                            sleep(0.5)
                            dm.leftclick()
                            sleep(1)
                            break
        if C>5:
            break
def Fu_Ben(): ##除棋阵/虎口外 所有副本均适用。
    name=''
    l=[['九灵.bmp','九灵'],['铁衣1.bmp','铁衣']]
    for i in l:
        z=Zhao_Tu(83,67,109,89,i[0])
        if z[0]!=-1:
            print('职业{}'.format(i))
            name=i[1]

    while True:
            z = dm.findstr(1061, 35, 1241, 100, '落枫山庄|水啸钱塘|云起台|清明上河|'
                                                '冰火湖心|怒砸黑店|洞天福地|'
                                                '勇闯辽营|神州奇侠|', '52.42.73-2.5.30', 0.65, '', '')
            if z==-1:
                print('当前副本结束')
                break
            else:
                if name=='九灵':
                    Z = Zhao_Tu(260, 58, 463, 134, '宝宝.bmp')
                    if Z[0]==-1:
                        print('九灵没宝宝了')
                        dm.keypresschar('f1')
                        sleep(3)
                        dm.keypresschar('f3')
                        sleep(1)
                        dm.keypresschar('f2')
                        sleep(1)
                if name=='铁衣':
                    Z = Zhao_Tu(87,101,298,141, '金刚.bmp')
                    if Z[0] == -1:
                        print('铁衣没状态了')
                        dm.keypresschar('v')
                        sleep(1)
                print('找怪1')
                dm.keypresschar('tab')
                sleep(1)
                t = dm.FindColor(425,55,866,120, 'ff4444-000000|ffe96e-000000|b479ff-000000', 1.0, 0)
                #Rool()
                #print('一')

                if t[0]!=0 :
                    print('打怪1')
                    dm.keypresschar('1')
                      ##血河1技能不刷新图像
                    while True:
                        S_W()
                        dm.keydownchar('1')
                        b=dm.IsDisplayDead(417, 700, 444, 726, 5)
                        if b==0:
                            l=random.randint(2,5)
                            dm.keypresschar(l)
                        t = dm.FindColor(519, 67, 582, 94, 'ff4444-000000|ffe96e-000000|b479ff-000000', 1.0, 0)
                        sleep(0.3)
                        #print('二')
                        if t[0]==0:
                            dm.keyupchar('1')
                            #print('yi')
                            sleep(0.5)

                            break
                else:
                    dm.keypresschar('g')
                    while True:
                        s=random.randint(1,10)/7
                        dm.keypresschar('tab')
                        sleep(s)
                        t = dm.FindColor(425, 55, 866, 120, 'ff4444-000000|ffe96e-000000|b479ff-000000', 1.0, 0)

                        if  t[0] != 0:
                            # print('当前副本结束',now())
                            break
                        else:
                            print('找怪,休息两秒', now())
                            sleep(2)
def Fu(H):
    name = ''
    l = [['九灵.bmp', '九灵'], ['铁衣1.bmp', '铁衣']]
    for i in l:
        z = Zhao_Tu(83, 67, 109, 89, i[0])
        if z[0] != -1:
            print('职业{}'.format(i))
            name = i[1]

    while True:
            if name == '九灵':
                Z = Zhao_Tu(260, 58, 463, 134, '宝宝.bmp')
                if Z[0] == -1:
                    print('九灵没宝宝了')
                    dm.keypresschar('f1')
                    sleep(3)
                    dm.keypresschar('f3')
                    sleep(1)
                    dm.keypresschar('f2')
                    sleep(1)
            if name == '铁衣':
                Z = Zhao_Tu(87, 101, 298, 141, '金刚.bmp')
                if Z[0] == -1:
                    print('铁衣没状态了')
                    dm.keypresschar('v')
                    sleep(1)
            print('找怪1')
            dm.keypresschar('tab')
            sleep(1)
            t = dm.FindColor(425, 55, 866, 120, 'ff4444-000000|ffe96e-000000|b479ff-000000', 1.0, 0)
            # Rool()
            # print('一')

            if t[0] != 0:
                print('打怪1')
                dm.keypresschar('1')
                ##血河1技能不刷新图像
                while True:
                    S_W()
                    dm.keydownchar('1')
                    b = dm.IsDisplayDead(417, 700, 444, 726, 5)
                    if b == 0:
                        l = random.randint(2, 5)
                        dm.keypresschar(l)
                    t = dm.FindColor(519, 67, 582, 94, 'ff4444-000000|ffe96e-000000|b479ff-000000', 1.0, 0)
                    sleep(0.3)
                    # print('二')
                    if t[0] == 0:
                        dm.keyupchar('1')
                        # print('yi')
                        sleep(0.5)

                        break
            else:
                dm.keypresschar('g')
                while True:
                    s = random.randint(1, 10) / 7
                    dm.keypresschar('tab')
                    sleep(s)
                    t = dm.FindColor(519, 67, 582, 94, 'ff4444-000000|ffe96e-000000|b479ff-000000', 1.0, 0)

                    if t[0] != 0:
                        # print('当前副本结束',now())
                        break
                    else:
                        print('找怪,休息两秒', now())
                        sleep(2)

def Qi_Zhen():
    dm.keypresschar('h')
    while True:
        z = dm.findstr(1061, 35, 1241, 100, '落枫山庄|水啸钱塘|云起台|清明上河|'
                                            '冰火湖心|怒砸黑店|枫林追迹|洞天福地|'
                                            '勇闯辽营|神州奇侠|虎口夺食|棋阵迷踪', '52.42.73-2.5.30', 0.8, '', '')

        if z == -1:
            print('当前副本结束')
            dm.keypresschar('h')
            break

        else:
            sleep(5)
def Hu_Kou():
    #dm.UseDict(0)
    dm.keypresschar('h')
    while True:
        z = dm.findstr(1061, 35, 1241, 100, '落枫山庄|水啸钱塘|云起台|清明上河|'
                                            '冰火湖心|怒砸黑店|枫林追迹|洞天福地|'
                                            '勇闯辽营|神州奇侠|虎口夺食|棋阵迷踪', '52.42.73-2.5.30', 0.8, '', '')

        if z == -1:
            print('当前副本结束')
            dm.keypresschar('h')
            break

        else:
            sleep(5)
def x():
    while True:
        xx = random.randint(1, 8) / 3
        print('找怪1')
        sleep(xx)
        dm.keypresschar('tab')
        sleep(1)
        t = dm.FindColor(425, 55, 866, 120, 'ab73f2-000000|a7afff-000000|ff4444-000000|ffe96e-000000|b479ff-000000',
                         1.0, 0)
        # Rool()
        # print('一')
        if t[0] != 0:
            print('打怪1')
            dm.keypresschar('1')
            ##血河1技能不刷新图像
            while True:
                # S_W()
                Z = Zhao_Tu(1017, 345, 1264, 410, '失败.bmp')
                if Z[0] != -1:
                    z = Zhao_Tu(499, 475, 949, 697, '放弃任务.bmp')
                    dm.movetoex(z[1], z[2], 10, 10)
                    sleep(xx)
                    dm.leftclick()
                    sleep(xx)
                    dm.keypresschar("enter")
                    sleep(1)

                    break
                else:
                    dm.keydownchar('1')
                    b = dm.IsDisplayDead(417, 700, 444, 726, 5)
                    if b == 0:
                        l = random.randint(2, 5)
                        dm.keypresschar(l)
                    t = dm.FindColor(425, 55, 866, 120,
                                     'ab73f2-000000|a7afff-000000|ff4444-000000|ffe96e-000000|b479ff-000000', 1.0, 0)
                    sleep(0.3)
                    # print('二')
                    if t[0] == 0:
                        dm.keyupchar('1')
                        # print('yi')
                        break
        else:
            break
def WangCheng():
    while True:
        xx = random.randint(1, 8) / 3
        Ctf()
        dm.movetoex(223,287,160,90)
        sleep(xx)
        z=Zhao_Tu(467,355,795,535,'完成1.bmp')
        z1 = Zhao_Tu(975, 460, 1246, 664, '提交4.bmp')
        if z[0]!=-1:
            dm.movetoex(z[1],z[2],5,5)
            sleep(0.1)
            dm.leftclick()
            sleep(0.78)
            z = Zhao_Tu(975,460,1246,664, '提交4.bmp')
            if z[0]!=-1:
                dm.movetoex(z[1], z[2], 5, 5)
                sleep(0.1)
                dm.leftclick()
                sleep(0.5)
            break
        elif z1[0]!=-1:
            dm.movetoex(z1[1], z1[2], 5, 5)
            sleep(0.1)
            dm.leftclick()
            sleep(1)
            break
        else:
            sleep(3)

def shenzhou():
    name = ''
    l = [['九灵.bmp', '九灵'], ['铁衣1.bmp', '铁衣']]

    for i in l:
        print('职业{}'.format(i))
        z = Zhao_Tu(83, 67, 109, 89, i[0])
        if z[0] != -1:
            name = i[1]

    while True:
        if name == '九灵':
            Z = Zhao_Tu(260, 58, 463, 134, '宝宝.bmp')
            if Z[0] == -1:
                print('九灵没宝宝了')
                dm.keypresschar('f1')
                sleep(3)
                dm.keypresschar('f3')
                sleep(1)
                dm.keypresschar('f2')
                sleep(1)
        if name == '铁衣':
            Z = Zhao_Tu(87, 101, 298, 141, '金刚.bmp')
            if Z[0] == -1:
                print('铁衣没状态了')
                dm.keypresschar('v')
                sleep(1)
        print('找怪1')
        dm.keypresschar('tab')
        sleep(1)
        t = dm.FindColor(425, 55, 866, 120, 'ff4444-000000|ffe96e-000000|b479ff-000000', 1.0, 0)
        # Rool()
        # print('一')
        z = dm.findstr(1061, 35, 1241, 100, '落枫山庄|水啸钱塘|云起台|清明上河|'
                                            '冰火湖心|怒砸黑店|枫林追迹|洞天福地|'
                                            '勇闯辽营|神州奇侠|虎口夺食|棋阵迷踪', '52.42.73-2.5.30', 0.8, '', '')
        if t[0] != 0 and z != -1:
            print('打怪1')
            dm.keypresschar('1')
            ##血河1技能不刷新图像
            while True:
                S_W()
                dm.keydownchar('1')
                b = dm.IsDisplayDead(417, 700, 444, 726, 5)
                if b == 0:
                    l = random.randint(2, 5)
                    dm.keypresschar(l)
                t = dm.FindColor(519, 67, 582, 94, 'ff4444-000000|ffe96e-000000|b479ff-000000', 1.0, 0)
                sleep(0.3)
                # print('二')
                if t[0] == 0:
                    dm.keyupchar('1')
                    # print('yi')
                    dm.keypresschar('g')
                    break
        else:
            z = dm.findstr(1061, 35, 1241, 100, '落枫山庄|水啸钱塘|云起台|清明上河|'
                                                '冰火湖心|怒砸黑店|枫林追迹|洞天福地|'
                                                '勇闯辽营|神州奇侠|虎口夺食|棋阵迷踪', '52.42.73-2.5.30', 0.8, '', '')
            if z == -1:
                break
            else:
                #sleep(2)
                Zhuang_Bei = Zhao_Tu(266,162,1175,720, '使用.bmp|使用1.bmp|确定.bmp')
                                                        ##所有需要鼠标点击的右下角装备处理
                print(Zhuang_Bei)
                if Zhuang_Bei[0] != -1:
                    dm.movetoex(Zhuang_Bei[1], Zhuang_Bei[2], 20, 15)
                    sleep(0.58)
                    dm.leftclick()
                    sleep(0.5)
                    dm.movetoex(10, 10, 20, 15)

                X = Zhao_Tu(451, 198, 909, 556, '蛮力砸开.bmp')
                if X[0] != -1:
                    dm.movetoex(X[1], X[2], 5, 5)
                    sleep(0.5)
                    dm.leftclick()
                    sleep(0.5)
                    dm.movetoex(10, 10, 20, 15)
                z = dm.findstrE(467, 238, 796, 470, '神州侠义匣', '180.60.60-15.30.20', 0.8,).split('|')
                print(z)
                if z[0] != '-1':
                    dm.movetoex(z[1]+50, z[2]+70, 10, 10)
                    sleep(0.5)
                    dm.leftclick()
                    sleep(0.5)
                    dm.movetoex(10, 10, 20, 15)


def XunShe():
    Ctf()
    while True:
        #sleep(3)
        Z1 = dm.findstr(669, 377, 823, 530, 'F', '240.0.98-45.7.20', 0.95, '', '')
        if Z1!=-1:
            dm.keypresschar('f')
            print('开始读条')
            sleep(3)
            print('读条结束')
            break
        else:
            sleep(3)
    x()
    WangCheng()
def Yuan_Zhu():
    #while True:
        sleep(1)
        #Z1 = dm.findstrE(1027,376,1281,514, '帮会庙会', '38.94.65-3.15.15', 0.8,).split('|')
        Z1=Zhao_Tu(78,186,488,368,'帮会庙会分店.bmp')
        print('帮会庙会',Z1)
        if Z1[0]!=-1:
            dm.movetoex(Z1[1], Z1[2], 55, 5)
            sleep(0.1)
            dm.leftclick()
            sleep(1)
        while True:
            Z=Zhao_Tu(461,32,784,153,'店铺列表.bmp')
            print('店铺列表',Z)
            if Z[0]!=-1:
                dm.movetoex(Z[1],Z[2]+390,100,5)
                sleep(0.1)
                dm.leftclick()
                sleep(0.5)
                Z1 = Zhao_Tu(933,426,1250,686, '购买.bmp')
                dm.movetoex(Z1[1], Z1[2],20, 5)
                sleep(0.1)
                dm.leftclick()
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
                    z=Zhao_Tu(471,220,798,430,'提交.bmp|提交1.bmp|提交物品.bmp')
                    if z[0]!=-1:
                        Ti_Jiao1()
                        break
                    else:
                        sleep(3)
                break
            else:
                sleep(3)

        WangCheng()
def Qiu_Feng():

    while True:
        #xx = random.randint(1, 8) / 3
        Z1 = dm.findstre(310,106,988,583, '小迪', '127.42.90-4.7.18', 0.9,).split('|')
        if Z1[0]!='-1':
            dm.movetoex(int(Z1[1])-200,int(Z1[2])+20,500, 20)
            dm.keydownchar('1')
            sleep(2)
            #Z1 = dm.findstr(1027, 376, 1281, 514, '箫姨', '38.94.65-3.15.15', 0.9, '', '')
            Z1 =Zhao_Tu(95,223,451,318,'萧姨.bmp')
            print('箫姨',Z1)
            if Z1[0] != -1:
                dm.keyupchar('1')
                break
        else:
            Zhao_DiTU('2', '2', '8', '', '1', '5', '7', '')
            sleep(5)
    WangCheng()
def Duan():

    sleep(1)
    z=Zhao_Tu(295,499,582,682,'放弃任务.bmp')
    dm.movetoex(z[1],z[2],50,10)
    sleep(0.1)
    dm.leftclick()
    sleep(0.5)
    z1 = Zhao_Tu(440, 166, 887, 537, '确定1.bmp')
    sleep(0.1)
    dm.movetoex(z1[1], z1[2], 50, 10)
    sleep(0.1)
    dm.leftclick()
def XueZhong():
    Ctf()
    while True:
        xx = random.randint(1, 8) / 3
        z = Zhao_Tu(277, 136, 882, 571, '提交物品.bmp')
        z1 = Zhao_Tu(125,61,970,529, '背包.bmp')
        print('提交物品',z)
        if z1[0]!=-1:
            dm.movetoex(z1[1], z1[2], 50, 50)
            sleep(0.1)
            dm.leftdown()
            sleep(0.1)
            dm.movetoex(812,132, 50, 30)
            sleep(0.1)
            dm.leftclick()
            sleep(0.1)
            dm.leftup()
            sleep(xx)
            if z[0]!=-1:
                print(z)
                dm.movetoex(z[1], z[2], 50, 50)
                sleep(0.1)
                dm.leftdown()
                sleep(xx)
                dm.movetoex(599,265, 50, 30)
                sleep(0.1)
                dm.leftclick()
                sleep(0.1)
                dm.leftup()
                sleep(xx)
                break
        else:
            sleep(3)
    while True:
        xx = random.randint(1, 8) / 3
        #Z1 = dm.findstr(1027, 376, 1281, 514, '箫姨', '38.94.65-3.15.15', 0.9, '', '')
        Z1=Zhao_Tu(85,214,486,310,'与萧姨对话.bmp')
        print('箫姨', Z1)
        if Z1[0]!= -1:
            WangCheng()
            break
        else:
            sleep(1)
            z = Zhao_Tu(241, 61, 1236, 472, '背包.bmp')
            print('背包', z)
            #print(z)
            Z = dm.FindMultiColor(z[1],z[2],z[1]+400,z[2]+200, 'cce5e7-000000',
                                  '1|0|cfe8f3-000000,0|1|daeef6-000000', 0.9, 0)
            print('道具',Z)
            if z[0]!=-1:
                dm.movetoex(Z[1]+10, Z[2]+10, 15, 15)
                sleep(0.1)
                dm.rightclick()
                sleep(xx)
                Ti_Jiao1()
                sleep(1)
                z=Zhao_Tu(933,556,1236,700,'提交道具.bmp')
                if z[0]!=-1:
                    dm.movetoex(z[1],z[2],50,5)
                    sleep(0.1)
                    dm.leftclick()
                    sleep(xx)
                    dm.movetoex(Z[1] + 70, Z[2] + 10, 15, 15)
                    sleep(0.1)
                    dm.rightclick()
                    sleep(xx)
                    Ti_Jiao1()
                    sleep(xx)
                    z = Zhao_Tu(933, 556, 1236, 700, '提交道具.bmp')
                    if z[0] != -1:
                        dm.movetoex(z[1], z[2], 50, 5)
                        sleep(0.1)
                        dm.leftclick()
                        sleep(xx)
                        dm.movetoex(Z[1] + 110, Z[2] + 10, 15, 15)
                        sleep(0.1)
                        dm.rightclick()
                        sleep(xx)
                        Ti_Jiao1()
                        sleep(1)
                        # = Zhao_Tu(933, 556, 1236, 700, '提交道具.bmp')

            else:
                Ctf()
                sleep(3)
def MoQi():
    Ctf()
    while True:
        z=Zhao_Tu(967,568,1280,685,'别以为.bmp|再来练练.bmp')
        if z[0]!=-1:
            dm.movetoex(z[1],z[2],100,5)
            sleep(0.1)
            dm.leftclick()
            break
        else:
            Ctf()
            sleep(5)
    x()
    WangCheng()
def JinChan():
    #Ctf()
    while True:
        Z1 = dm.findstr(1027, 376, 1281, 514, '箫姨', '38.94.65-3.15.15', 0.9, '', '')
        print('箫姨', Z1)
        if Z1 != -1:
            WangCheng()
            break
        else:
            sleep(2)
            dm.keypresschar('tab')
            sleep(1)
            t = dm.FindColor(425, 55, 866, 120, 'ff4444-000000|ffe96e-000000|b479ff-000000', 1.0, 0)
            # Rool()
            # print('一')
            if t[0] != 0:
                print('打怪1')
                dm.keypresschar('1')
                ##血河1技能不刷新图像
                while True:
                    # S_W()
                    dm.keydownchar('1')
                    b = dm.IsDisplayDead(417, 700, 444, 726, 5)
                    if b == 0:
                        l = random.randint(2, 5)
                        dm.keypresschar(l)
                    t = dm.FindColor(519, 67, 582, 94, 'ff4444-000000|ffe96e-000000|b479ff-000000', 1.0, 0)
                    sleep(0.3)
                    # print('二')
                    if t[0] == 0:
                        dm.keyupchar('1')
                        # print('yi')
                        break
            else:
                Ctf()
                sleep(5)
def Wanc():
    while True:
        z=Zhao_Tu(467, 355, 795, 535, '我来帮你恢复.bmp')
        if z[0]!=-1:
            dm.movetoex(z[1],z[2],30,5)
            sleep(0.1)
            dm.leftclick()
            dm.keypresschar('b')
            sleep(1)
            z = Zhao_Tu(241, 61, 1236, 472, '背包.bmp')
            dm.movetoex(z[1]+98,z[2],5,5)
            sleep(0.1)
            dm.rightclick()
            sleep(1)
            z=Zhao_Tu(471,394,866,666,'提交5.bmp')
            dm.movetoex(z[1], z[2], 5, 5)
            sleep(0.1)
            dm.leftclick()
        else:
            z = Zhao_Tu(467, 355, 795, 535, '完成1.bmp')
            if z[0]!=-1:
                dm.movetoex(z[1],z[2],50,5)
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
        xx = random.randint(1, 8) / 3
        z = Zhao_Tu(54, 142, 491, 413, '阴谋计划.bmp')
        print('打开包裹',z)
        if z[0]!=-1:
            dm.keypresschar('b')
            sleep(1)
            z=Zhao_Tu(244,49,1244,392,'背包.bmp')
            sleep(0.5)
            dm.movetoex(z[1]+10, z[2] +220, 10, 10)
            sleep(0.1)
            dm.leftclick()
            sleep(0.5)
            dm.movetoex(z[1]+90,z[2]+20,10,10)
            sleep(0.3)
            dm.rightclick()
            sleep(3)
            dm.keypresschar('b')
            break
        else:
            dm.keypresschar('tab')
            sleep(1)
            t = dm.FindColor(425, 55, 866, 120, 'ff4444-000000|ffe96e-000000|b479ff-000000', 1.0, 0)
            # Rool()
            # print('一')
            if t[0] != 0:
                print('打怪1')
                dm.keypresschar('1')
                ##血河1技能不刷新图像
                while True:
                    # S_W()
                    dm.keydownchar('1')
                    b = dm.IsDisplayDead(417, 700, 444, 726, 5)
                    if b == 0:
                        l = random.randint(2, 5)
                        dm.keypresschar(l)
                    t = dm.FindColor(519, 67, 582, 94, 'ff4444-000000|ffe96e-000000|b479ff-000000', 1.0, 0)
                    sleep(0.3)
                    # print('二')
                    if t[0] == 0:
                        dm.keyupchar('1')
                        print('打死了')
                        # print('yi')
                        sleep(1)
                        break
            else:
                Ctf()
                sleep(3)
    Wanc()
def Da_Jie():
    while True:
        xx = random.randint(1, 8) / 3
        z=Zhao_Tu(61,110,658,335,'制造骚乱.bmp|演武堂管事.bmp|查看线索.bmp')
        if z[0]!=-1:
            break
        else:
            Ctf()
            sleep(xx)
    while True:
        print('找怪1')
        sleep(2)
        dm.keypresschar('tab')
        sleep(1)
        t = dm.FindColor(425, 55, 866, 120,
                         'ab73f2-000000|a7afff-000000|ff4444-000000|ffe96e-000000|b479ff-000000', 1.0, 0)
        # Rool()
        # print('一')
        if t[0] != 0:
            print('打怪1')
            dm.keypresschar('1')
            ##血河1技能不刷新图像
            while True:
                xx = random.randint(1, 8) / 3
                S_W()
                Z = Zhao_Tu(1017, 345, 1264, 410, '失败.bmp')
                if Z[0] != -1:
                    z = Zhao_Tu(499, 475, 949, 697, '放弃任务.bmp')
                    dm.movetoex(z[1], z[2], 10, 10)
                    sleep(0.1)
                    dm.leftclick()
                    sleep(xx)
                    dm.keypresschar("enter")
                    sleep(xx)

                    break
                else:
                    dm.keydownchar('1')
                    b = dm.IsDisplayDead(417, 700, 444, 726, 5)
                    if b == 0:
                        l = random.randint(2, 5)
                        dm.keypresschar(l)
                    t = dm.FindColor(425, 55, 866, 120,
                                     'ab73f2-000000|a7afff-000000|ff4444-000000|ffe96e-000000|b479ff-000000',
                                     1.0, 0)
                    sleep(1)
                    # print('二')
                    if t[0] == 0:
                        dm.keyupchar('1')
                        # print('yi')
                        break

            z = Zhao_Tu(61, 110, 658, 335, '与xxx对话.bmp|')
            if z[0] != -1:
                break
        else:
            Ctf()
            sleep(2)

    Wanc()
def ShuiJin():
    Ctf()
    sleep(5)
    dm.movetoex(607,279,5,5)
    sleep(.5)
    dm.leftclick()
Zhao_Tu_JiHe_W =[



[471,220,798,430,'提交.bmp|提交1.bmp|提交物品.bmp',Ti_Jiao1,'提交'],
[1004,368,1275,697,'前往自在门.bmp|进入卧房1.bmp|我走了.bmp|画中人.bmp|询问客人.bmp|'
                  '询问客人.bmp|崇宁四年.bmp|灭门案.bmp|楚相玉.bmp|十三元凶.bmp|'
                  '疑案.bmp|盛家庄.bmp|令牌.bmp|选择修行方向.bmp|我想选.bmp|'
                  '拿出四逆汤.bmp|上前迎战.bmp|递过竹哨.bmp|得罪.bmp|'
                  '拿出令牌.bmp|二哥得罪.bmp|拿出一百二十文.bmp|'
                  '好我来试试.bmp|接过密码锁.bmp|好我来试试.bmp|'
                  '扬州.bmp|再来再来.bmp|建康.bmp|得罪1.bmp|鼠.bmp|十年前.bmp|记住了.bmp|准备好了.bmp|'
                  '拿出一百文.bmp|门卫.bmp|走就走.bmp|出示令牌.bmp|接招.bmp|好啊.bmp',Hu_Dongl,'选择'],

[25,34,1259,551,'晚晴之情.bmp|百合姑娘.bmp|面具.bmp|白发.bmp|好.bmp|等等.bmp|沈云山.bmp|每半年轮值一次.bmp|五招.bmp|'
                  '日短夜长.bmp|十二位.bmp|出门是敌人.bmp|'
                  '开盒子.bmp|四逆汤.bmp|交情.bmp|我不.bmp|蒲苇.bmp|不是.bmp|'
                  '情侣南线.bmp|告诉.bmp|不告诉.bmp|告诉1.bmp|告诉2.bmp|好吃.bmp|赞同.bmp|维护.bmp|瞒着.bmp|多了.bmp',WangQ,'选择'],

[1004,368,1275,697, '升级.bmp',Shen_Ji_JiNeng,'升级技能'],
[952,345,1263,678, '无名老人1.bmp',Wu_Ming,'无名老人'],
[952,345,1263,678, '观众热情度.bmp|观众热情度1.bmp',AA,'观众热情度'],
[934,500,1258,701, '野利广元.bmp|修贤.bmp|秒明.bmp|圣量.bmp|净真.bmp|贞庆.bmp|', yaoseng30, '野利广元'],
[956,577,1269,706,'碎片拼凑.bmp|修复名画.bmp|',Ping_Cou,'碎片拼凑'],


]



Zhao_Tu_JiHe_Y = [
[1001,350,1282,591, '表明来意.bmp|表明来意1.bmp|表明来意2.bmp|'
                    '师兄.bmp|师兄1.bmp|师兄3.bmp|师兄4.bmp|微风.bmp|'
                    '姚久仁.bmp|摸摸白雪.bmp|释放冷呼儿.bmp|鲁熊.bmp|老王.bmp|穿上时装.bmp|'
                    '斟酒.bmp|斟酒1.bmp|斟酒2.bmp',F,'向追命表明来意'],


[1001,350,1282,591,'击败黑衣人.bmp|击败黑衣人1.bmp|击败黑衣人2.bmp|'
                   '黑衣人头目.bmp|黑衣人头目1.bmp|黑衣人头目3.bmp|黑衣人头目4.bmp|'
                   '教训.bmp|击败.bmp|教训何绍金.bmp|摆平守卫.bmp|摆平守卫1.bmp|教训1.bmp|教训2.bmp|教训3.bmp|教训4.bmp|'
                   '燕诗二.bmp|燕诗二1.bmp|燕诗二2.bmp|燕诗二3.bmp|燕诗二4.bmp|燕诗二5.bmp|燕诗二6.bmp|燕诗二7.bmp|'
                             '燕诗二8.bmp|燕诗二9.bmp|燕诗二10.bmp|燕诗二11.bmp|燕诗二12.bmp|'
                   '不速之客.bmp|莞儿.bmp|高府家丁.bmp|高衙内.bmp|辽军细作.bmp|'
                     '辽贼.bmp|神秘男子.bmp|辽国男子.bmp|'
                     '深入追击辽兵.bmp|萧乙辛.bmp|迟延.bmp|会合.bmp|等待沈云山前来.bmp|'
                     '战胜.bmp|战胜田大错.bmp|大寨主运功灭火.bmp|冥火台上升.bmp|让戚大哥先走.bmp|大战一触即发.bmp|'
                   '战胜1.bmp|迎战1.bmp|战胜2.bmp|击败2.bmp|战胜3.bmp|'
                     '击败3.bmp|战胜.bmp|击退.bmp|迎战2.bmp|'
                     '过招.bmp|和顾惜朝比试.bmp|战胜6.bmp|'
                     '击败4.bmp|击败5.bmp|帮助二哥.bmp|情势危急.bmp|抓住.bmp',A,'击败黑衣人'],




[1010,369,1276,527,'碧云溪.bmp|碧云溪1.bmp|碧云溪2.bmp|碧云溪3.bmp|碧云溪4.bmp',Bi_Yun,'碧云溪萃刀'],
[1006,369,1273,519,'捕鱼.bmp|下河.bmp|捕鱼2.bmp|捕鱼1.bmp',Bu_Yu,'下河捕鱼'],

[1004,368,1275,697,'云起风清.bmp|云起风清1.bmp',Yun_Qi,'云起风清'],
[1004,368,1275,697,'击飞落叶.bmp|击飞落叶1.bmp|击飞落叶2.bmp|击飞落叶3.bmp',Ji_Fei,"击飞落叶"],


[1004,368,1275,697,'牵马.bmp',Qian_Ma,'牵马'],
    [1004,368,1275,697,'骑马.bmp',Qi_Ma,'骑马'],

[436,98,846,609,'职业是.bmp|时间是.bmp|偏好是.bmp|',Qing_Ya_Shu,'翻阅青崖书'],
[1004,368,1275,697,'杂草.bmp|杂草1.bmp',Za_Cao,'杂草'],
[1004,368,1275,697,'方踪影.bmp|方踪影1.bmp|方踪影2.bmp|',Fang_Zong,'方踪影'],
[1004,368,1275,697,'武学试炼.bmp',Wu_Xue,'武学试炼'],
[1004,368,1275,697, '坐下.bmp',Zuo_Xia,'坐下'],
[952,345,1263,678, '门旁.bmp',Meng_Pang,'门旁'],
#S[952,345,1263,678, '衣服.bmp|衣服1.bmp',Luoxia,'衣服'],
[952, 345, 1263, 678,'望气.bmp|望气2.bmp',Wang_Qi,'望气'],
[952, 345, 1263, 678,'猎虎.bmp',Lie_Hu,'降龙猎虎'],
[952, 345, 1263, 678,'歇息.bmp', Xie,'歇息'],
[952, 345, 1263, 678,'尸身.bmp',S,'尸身'],
[952, 345, 1263, 678,'绳索.bmp',Sheng_suo,'绳索'],
[952, 345, 1263, 678,'旁边.bmp',Pang_bian,'旁边'],
[952, 345, 1263, 678,'营房.bmp|衣服2.bmp',YFang,'营房'],
[952, 345, 1263, 678,'追击辽兵.bmp',Zhui_Ji,'追击辽兵'],
[952, 345, 1263, 678,'金疮药.bmp',JinChuan,'金疮药'],
[952, 345, 1263, 678,'回营休息.bmp',Xie1,'回营休息'],
[952, 345, 1263, 678,'引狼弹.bmp',YLD,'引狼弹'],
[952, 345, 1263, 678,'询问时机.bmp|萧铭律.bmp',Xun_Wen,'询问时机'],
[475,497,885,684,'确定选择.bmp',Q_D,'确定选择'],
[952, 345, 1263, 678,'缚虎囚龙.bmp',Qiu_Long,'缚虎囚龙'],
#[952, 345, 1263, 678,'与戚少商商议.bmp',Shang_Yi,'与戚少商商议'],

#[952, 345, 1263, 678,'跟随戚少商继续深入大牢.bmp',ShenRuDaLao,'跟随戚少商继续深入大牢'],
[952, 345, 1263, 678,'升台机关.bmp',shengtai,'升台机关'],
[952, 345, 1263, 678,'止血.bmp',Z_X,'止血'],
[952, 345, 1263, 678,'第一处帐篷.bmp|第二处帐篷.bmp|第三处帐篷.bmp', Shao,'第一处帐篷'],
[952, 345, 1263, 678,'击退辽兵.bmp|辽军大将.bmp|进攻.bmp',JinGong,'击退辽兵'],
[952, 345, 1263, 678,'围堵聂琦.bmp',WEI_Du,'围堵聂琦'],
[952, 345, 1263, 678,'偷袭.bmp',Tou_Xi,'偷袭'],
[952, 345, 1263, 678,'落座.bmp',Luozhuo,'落座'],
[952, 345, 1263, 678,'烹鲜醉客.bmp',Peng_Xian,'烹鲜醉客'],
[490,109,865,334,'入木三分.bmp',Ru_Mu,'入木三分'],
[952, 345, 1263, 678,'堂前风.bmp',Tang_Qian,'堂前风'],
[952, 345, 1263, 678,'推开房门.bmp',Tuikai,'推开房门'],
[952, 345, 1263, 678,'关闭.bmp',GuangBi,'关闭'],
[952, 345, 1263, 678,'关闭书房.bmp',Guang,'关闭书房'],
[952, 345, 1263, 678,'离开书房.bmp',Guang1,'离开书房'],
[952, 345, 1263, 678,'痛打陈三刀.bmp',Tong_Da,'痛打陈三刀'],
[952, 345, 1263, 678,'坐过去.bmp|空位.bmp',ZUOguoqu,'坐过去'],
[952, 345, 1263, 678,'击晕船工.bmp|击晕船工1.bmp',Chuan_Gong,'击晕船工'],
[952, 345, 1263, 678,'初云装.bmp',Chu_Yun,'初云装'],
    [952, 345, 1263, 678,'水井.bmp',ShuiJin,'水井']
]

Zhao_Tu_JiHe_ZW =[
[471,220,798,430,'提交.bmp|提交1.bmp|提交物品.bmp',Ti_Jiao1,'提交'],
[25,34,1259,551, '莲塘.bmp|寒酸.bmp|晏几道.bmp|我不太记得了.bmp|我能挺住.bmp|'
                   '明公胜.bmp|孤山胜.bmp|孤山胜.bmp|二千两.bmp|苏1.bmp|大苏.bmp', WangQ, '莲塘'],

[479,242,786,433,'提交.bmp|提交1.bmp|提交2.bmp|提交3.bmp|递过茶业.bmp|递过笔墨.bmp|',Ti_Jiao1,'提交'],
[800, 449, 1261, 693,'前往故地.bmp|送我上塔顶.bmp|带我上去.bmp|'
                     '兔毫.bmp|拿出白纸扇.bmp|放下旧扇.bmp|包袱还给她.bmp|'
                     '递过扇子.bmp|递交字纸.bmp|递交给婆婆.bmp|听曲.bmp|落花记前踪.bmp|茶.bmp|'
                     '向阳.bmp|熙春.bmp|舞隐.bmp|眉山人.bmp|眉.bmp|山.bmp|苏.bmp|东.bmp|坡.bmp|'
                     '递过茶业.bmp|递过笔墨.bmp|集会.bmp',Hu_Dongl,'前往故地'],

[230,76,880,453, '买酒.bmp', Mai_Jiu, '买酒'],
    [951,48,1242,232,'看图.bmp',KanTu,'看图'],
                  ]



Zhao_Tu_JiHe_ZY = [
[952,345,1263,678, '位子.bmp',WEI_Zhi,'位子'],
[952,345,1263,678, '位子1.bmp',WEI_Zhi1,'位子'],


[952,345,1263,678, '绿琦.bmp',F,'绿琦'],


[952, 345, 1263, 678,'击败.bmp|打败.bmp|迎战.bmp|击败1.bmp|战斗.bmp|击败1.bmp|'
                     '教训2.bmp|战胜4.bmp|战胜5.bmp|阻止.bmp|打跑.bmp|',A,'击败'],
[952, 345, 1263, 678,'修好瑶筝.bmp',Xiu_Yao_Zhen,'修好瑶筝'],
[952, 345, 1263, 678,'弹琴.bmp',WEI_Zhi2,'弹琴'],
[952, 345, 1263, 678,'追上游船.bmp',YouChuan,'追上游船'],
[952, 345, 1263, 678,'和曲和星对峙.bmp',Dui_Zhi,'和曲和星对峙'],
[952, 345, 1263, 678,'追上檀沁.bmp',ZhuiTan,'追上檀沁'],
[952, 345, 1263, 678,'红烧鱼.bmp',HongShao,'红烧鱼'],
[952, 345, 1263, 678,'躲避和尚.bmp|躲避和尚1.bmp',Duo_Bi,'躲避和尚'],
[952, 345, 1263, 678,'草帽木屐.bmp',Mu_Ji,'草帽木屐'],
[952, 345, 1263, 678,'似有感触.bmp',Gan_Chu,'似有感触'],




]
ziku=[['雪中送炭.bmp',XueZhong],
['火眼金睛.bmp',Duan ],
      ['资源援助.bmp', Yuan_Zhu],
      ['秋风落叶.bmp', Qiu_Feng],
      ['断其喉舌.bmp', Duan],
      ['打草熏蛇.bmp',XunShe],
      ['千杯不醉.bmp', Duan],
['金蝉脱壳.bmp', JinChan],
['莫欺年少.bmp', MoQi],

      ['结束.bmp',]

      ]
enchou=[['瓦上君子.bmp',Wanc],
        ['先发制人.bmp',XianFa],
        ['一探虚实.bmp',Wanc],
['驱虎吞狼.bmp',Wanc],
['趁火打劫.bmp',Da_Jie],
['断敌一指.bmp',Da_Jie],
['以眼还眼.bmp',Da_Jie],
['牛刀杀鸡.bmp',Wanc],

        ['结束.bmp',]
]

def run(hwnd,x,y):
    dm.movewindow(hwnd, x, y)
    sleep(1)
    l = dm.BindWindowEx(hwnd, 'dx2', 'dx2', 'dx', 'dx.public.disable.window.size', 0)
    print(hwnd,'绑定返回码',l)
    sleep(3)
    while True:
        shui = random.randint(1, 10)
        s = dm.findstr(1023, 375, 1284, 533, '落枫|清明|神猴令', '208.56.60-1.5.30', 0.7, '', '')
        #print('s', s)
        if s != -1:
            print('经验不够',now())
            dm.UnBindWindow()
            break
        ##找任务框  找色
        else:
            z = Zhao_Tu(319, 156, 911, 496, '点击离开副本.bmp')
            if z[0] != -1:
                print('点击离开副本-取消')
                dm.movetoex(z[1] + 180, z[2] + 50, 10, 10)
                sleep(0.5)
                dm.leftclick()
            Ren_WU_Kuan = dm.FindMultiColor(965, 327, 1279, 590, '6193f1-000000',
                                            '3|0|6192f7-000000,3|5|6193fa-000000', 0.95, 0)

            if Ren_WU_Kuan[0] == 1:
                print('其他任务',Ren_WU_Kuan)
                dm.movetoex(Ren_WU_Kuan[1]+240,Ren_WU_Kuan[2], 10, 5)
                sleep(0.5)
                dm.leftclick()
            '''
            Key_Sheng_Ji = dm.FindColor(1284, 742, 1285, 743, 'a5ffa4-000000', 1.0, 0)

            # print(Key_Sheng_Ji)
            if Key_Sheng_Ji[0] != 0:
                print('可以升级')
                dm.keypress(80)
                sleep(1)
                dm.movetoex(502, 626, 20, 10)
                sleep(1)
                dm.leftclick()
                sleep(1)
                Xiu_Wei = Zhao_Tu(420, 185, 842, 492, '修为不足.bmp|')
                dm.keypress(80)
                if Xiu_Wei[0] != -1:
                    print('修为不足')
                    dm.movetoex(602, 364, 40, 20) #确定
                    sleep(1)
                    dm.leftclick()
                    sleep(1)
                    dm.keypress(75)
                    sleep(1)
                    Z = Zhao_Tu(315, 590, 1067, 721, '购买秘籍.bmp')
                    dm.movetoex(Z[1] - 95, Z[2]+5 , 5, 5)
                    sleep(1)
                    dm.leftclick()
                    sleep(1)
                    z = Zhao_Tu(319, 156, 911, 496, '点击离开副本.bmp')
                    if z[0] != -1:
                        dm.movetoex(z[1] + 40, z[2] + 50, 10, 10)
                        sleep(0.5)
                        dm.leftclick()
                    dm.keypress(75)
                    while True:
                        zz = Zhao_Tu(937, 363, 1265, 725, '升级.bmp')
                        if zz[0] != -1:
                            dm.movetoex(zz[1]+50, zz[2] + 45, 30, 10)
                            sleep(1)
                            dm.leftclick()
                            #dm.keypress(75)
                            sleep(2)
                            break
                        else:
                            sleep(5)

                    Shen_Ji_JiNeng()
            '''
            sleep(0.2)
            XiTong = Zhao_Tu(134, 56, 1109, 660, '系统设置.bmp|技能界面.bmp|活动界面.bmp|已知晓2.bmp|')
            if XiTong[0] != -1:
                dm.keypress(27)  ##所有 ESC 的界面清理

            sleep(0.2)
            Zhuang_Bei = Zhao_Tu(2, 4, 1284, 744, '原地疗伤.bmp|原地疗伤1.bmp|原地疗伤2.bmp|原地疗伤3.bmp|原地疗伤4.bmp|'
                                                  '装备.bmp|装备1.bmp|装备2.bmp|使用.bmp|确定.bmp|已知晓1.bmp|确定4.bmp|确定5.bmp')  ##所有需要鼠标点击的右下角装备处理
            # print(Zhuang_Bei)
            if Zhuang_Bei[0] != -1:
                dm.movetoex(Zhuang_Bei[1], Zhuang_Bei[2], 20, 15)
                sleep(0.5)
                dm.leftclick()

                ly = Zhao_Tu(173, 149, 1149, 655, '确定4.bmp|确定5.bmp')
                print('确定', now())
                if ly[0] != -1:
                    dm.keypresschar('enter')

            sleep(0.2)
            Ren_WU_Kuan = dm.FindMultiColor(965, 327, 1279, 590, 'fbf461-000000',
                                            '2|0|fcf462-000000,2|4|fdf461-000000', 0.95, 0)
            # print('任务框',Ren_WU_Kuan)
            if Ren_WU_Kuan[0] == 1:  # 有任务框
                Ctf()
                print('主线中。。',now())
                sleep(1)
                for v in Zhao_Tu_JiHe_Y:  ##判断异常  找字  =改成找图
                    l = Zhao_Tu(v[0], v[1], v[2], v[3], v[4])
                    sleep(0.01)
                    if l[0] != -1:
                        print(l)
                        print('已见{}'.format(v[6]),now())
                        while True:
                            v[5]()
                            sleep(1)
                            l = Zhao_Tu(v[0], v[1], v[2], v[3], v[4])
                            if l[0] == -1:  # 异常处理完毕
                                    # del Jie_Guo_Y[0]
                                break
                        break
                sleep(shui/3)




            else:
                yichang=[]
                for v in Zhao_Tu_JiHe_W:  ##判断对话状态， 进房间，选项，转剧情 X里封装的是对话界面产生的所有异常
                    l = Zhao_Tu(v[0], v[1], v[2], v[3], v[4])
                    sleep(0.01)
                    if l[0] != -1:
                        print(l)
                        yichang.append(v)
                        print('已见{}'.format(v[6]),now())
                        while True:
                            v[5]()
                            l = Zhao_Tu(v[0], v[1], v[2], v[3], v[4])
                            if l[0] == -1:

                                break
                        break
                #sleep(shui / 7)
               # Li_Kai = dm.FindPic(1062, 654, 1280, 742, '离开.bmp|离开1.bmp|离开2.bmp|离开3.bmp|离开6.bmp|离开5.bmp',
                #                    '200.5.60-180.5.20', 0.7, 3)
                # print('离开', Li_Kai)
                if len(yichang)==0:
                    Li_Kai =Zhao_Tu(885, 663, 1016, 736, '对话1.bmp')
                    if Li_Kai[0] == -1:
                        while True:
                            print('剧情中...',now())
                            sleep(Sleep())
                            dm.keypresschar('esc')
                            sleep(1)
                            ll = Zhao_Tu(363, 260, 854, 541, '确定.bmp|确定3.bmp|')
                            if ll[0] != -1:
                                dm.movetoex(494, 416, 20, 20)
                                sleep(1)
                                dm.leftclick()
                            Ren_WU_Kuan = dm.FindMultiColor(965, 327, 1279, 590, 'fbf461-000000',
                                                            '2|0|fcf462-000000,2|4|fdf461-000000', 0.95, 0)
                            if Ren_WU_Kuan[0] == 1:
                                break


                    else:
                        while True:
                            s=random.randint(1,5)
                            print("对话中....   \n",now())
                            dm.keypresschar('f')
                            sleep(s/5)

                            z=Zhao_Tu(479,242,786,433,'提交.bmp|提交1.bmp|提交2.bmp')
                            if z[0]!=-1:
                                sleep(0.5)
                                dm.movetoex(z[1],z[2],5,5)
                                sleep(0.8)
                                dm.leftclick()
                            Li_Kai = Zhao_Tu(885, 663, 1016, 736, '对话1.bmp')
                            if Li_Kai[0]==-1:
                                break
                else:
                    del yichang[0]

def zrun1(hwnd,x,y):
        dm.movewindow(hwnd, x, y)
        sleep(1)
        l = dm.BindWindowEx(hwnd, 'dx2', 'dx2', 'dx', 'dx.public.disable.window.size', 0)
        print(hwnd, '绑定返回码', l)
        sleep(3)
        L=['当时明月在.bmp','一生一世一双人.bmp',

           '雪泥上.bmp','雪泥下.bmp']
        for i in L:
            Ren_WU_Kuan = dm.FindMultiColor(1000,326,1191,494, '6193f1-000000',
                                            '3|0|6192f7-000000,3|5|6193fa-000000', 0.95, 0)
            Z = Zhao_Tu(749,16,992,95, '福利.bmp')
            if Ren_WU_Kuan[0] ==0 and Z[0]!=-1:  # 没有有任务框
                print('调接任务函数')
                Jie_Ren_Wu(i)

            while True:
                shui =random.randint(1,10)
                #z = dm.findstr(1002, 337, 1283, 511, '当时明月在|一生一世一双人', '228.34.65-30.30.40', 0.7, '', '')
                Ren_WU_Kuan = dm.FindMultiColor(1000,326,1191,494, '6193f1-000000',
                                                '3|0|6192f7-000000,3|5|6193fa-000000', 0.95, 0)
                print(Ren_WU_Kuan,now())
                #print(z)
                Z=Zhao_Tu(749,16,992,95,'福利.bmp')
                if Ren_WU_Kuan[0] == 0 and Z[0]!=-1:  #正常界面没任务框结束
                    dm.UnBindWindow()
                    print('任务结束',now())
                    break

                ##找任务框  找色
                else:
                    z = Zhao_Tu(319, 156, 911, 496, '点击离开副本.bmp')
                    if z[0] != -1:
                        print('点击离开副本--取消')
                        dm.movetoex(z[1] + 180, z[2] + 50, 10, 10)
                        sleep(0.5)
                        dm.leftclick()
                        '''
                    Key_Sheng_Ji = dm.FindColor(1284, 742, 1285, 743, 'a5ffa4-000000', 1.0, 0)

                    # print(Key_Sheng_Ji)
                    if Key_Sheng_Ji[0] != 0:
                        print('可以升级')
                        dm.keypress(80)
                        sleep(1)
                        dm.movetoex(502, 626, 20, 10)
                        sleep(1)
                        dm.leftclick()
                        sleep(1)
                        Xiu_Wei = Zhao_Tu(420, 185, 842, 492, '修为不足.bmp|')
                        dm.keypress(80)
                        if Xiu_Wei[0] != -1:
                            print('修为不足')
                            dm.movetoex(602, 364, 40, 20)  # 确定
                            sleep(1)
                            dm.leftclick()
                            sleep(1)
                            dm.keypress(75)
                            sleep(1)
                            Z = Zhao_Tu(315, 590, 1067, 721, '购买秘籍.bmp')
                            dm.movetoex(Z[1] - 95, Z[2] + 5, 5, 5)
                            sleep(1)
                            dm.leftclick()
                            sleep(1)
                            z = Zhao_Tu(319, 156, 911, 496, '点击离开副本.bmp')
                            if z[0] != -1:
                                dm.movetoex(z[1] + 40, z[2] + 50, 10, 10)
                                sleep(0.5)
                                dm.leftclick()
                            dm.keypress(75)
                            while True:
                                zz = Zhao_Tu(937, 363, 1265, 725, '升级.bmp')
                                if zz[0] != -1:
                                    dm.movetoex(zz[1] + 50, zz[2] + 45, 30, 10)
                                    sleep(1)
                                    dm.leftclick()
                                    # dm.keypress(75)
                                    sleep(2)
                                        break
                                else:
                                    sleep(5)

                            Shen_Ji_JiNeng()
                    '''
                    XiTong = Zhao_Tu(134, 56, 1109, 660, '系统设置.bmp|技能界面.bmp|活动界面.bmp|已知晓2.bmp|长风.bmp|长风1.bmp|')
                    if XiTong[0] != -1:
                        print('清理界面')
                        dm.keypress(27)##所有 ESC 的界面清理


                    Zhuang_Bei = Zhao_Tu(2, 4, 1284, 744, '原地疗伤.bmp|原地疗伤1.bmp|原地疗伤2.bmp|原地疗伤3.bmp|原地疗伤4.bmp|'
                                                          '装备.bmp|装备1.bmp|装备2.bmp|使用.bmp|确定.bmp|已知晓1.bmp|确定1.bmp')  ##所有需要鼠标点击的右下角装备处理
                    print(Zhuang_Bei)
                    if Zhuang_Bei[0] != -1:
                        print('清理界面1')
                        dm.movetoex(Zhuang_Bei[1], Zhuang_Bei[2], 20, 15)
                        sleep(Sleep())
                        dm.leftclick()


                    Ren_WU_Kuan = dm.FindMultiColor(1000,326,1191,494, '6193f1-000000',
                                                    '3|0|6192f7-000000,3|5|6193fa-000000', 0.95, 0)
                    if Ren_WU_Kuan[0]==1: #有任务框
                        Ctf()
                        print('已见任务框')
                        print('主线中。。',now())
                        sleep(0.3)

                        print('主线找异常y=0。。',now())
                        for v in Zhao_Tu_JiHe_ZY:  ##判断异常  找字  =改成找图
                            l = Zhao_Tu(v[0], v[1], v[2], v[3], v[4])
                            sleep(0.1)
                            if l[0] != -1:
                                print(l)
                                print('已见{}'.format(v[6]),now())
                                while True:
                                    v[5]()
                                    sleep(1)
                                    l = Zhao_Tu(v[0], v[1], v[2], v[3], v[4])
                                    if l[0] == -1:  # 异常处理完毕
                                        # del Jie_Guo_Y[0]
                                        break
                                break
                        sleep(shui / 3)
                    else:
                        print('未见任务框')
                        yichang=[]
                        for v in Zhao_Tu_JiHe_ZW:  ##判断对话状态， 进房间，选项，转剧情 X里封装的是对话界面产生的所有异常

                            l = Zhao_Tu(v[0], v[1], v[2], v[3], v[4])
                            sleep(0.01)
                            if l[0] != -1:
                                yichang.append(v)
                                print(l)
                                print('已见{}'.format(v[6]),now())
                                while True:
                                    v[5]()
                                    l = Zhao_Tu(v[0], v[1], v[2], v[3], v[4])
                                    if l[0] == -1:
                                        break
                                break

                        # sleep(shui / 7)

                        # Li_Kai = dm.FindPic(1062, 654, 1280, 742, '离开.bmp|离开1.bmp|离开2.bmp|离开3.bmp|离开6.bmp|离开5.bmp',

                        #                    '200.5.60-180.5.20', 0.7, 3)

                        # print('离开', Li_Kai)
                        if len(yichang)==0:
                            Li_Kai = Zhao_Tu(885, 663, 1016, 736, '对话1.bmp')
                            if Li_Kai[0] == -1:
                                while True:
                                    print('剧情中...',now())
                                    sleep(Sleep())
                                    dm.keypresschar('esc')
                                    sleep(1)
                                    ll = Zhao_Tu(363, 260, 854, 541, '确定.bmp|确定3.bmp|')
                                    if ll[0] != -1:
                                        dm.movetoex(494, 416, 20, 20)
                                        sleep(1)
                                        dm.leftclick()
                                    Ren_WU_Kuan = dm.FindMultiColor(1000,326,1191,494, '6193f1-000000',
                                                                    '3|0|6192f7-000000,3|5|6193fa-000000', 0.95, 0)
                                    if Ren_WU_Kuan[0] == 1:
                                        break



                            else:
                                while True:
                                    s = random.randint(1, 5)
                                    print("对话中....   \n",now())
                                    dm.keypresschar('f')
                                    sleep(s / 5)
                                    z = Zhao_Tu(479, 242, 786, 433, '提交.bmp|提交1.bmp|提交2.bmp|')
                                    if z[0]!=-1:
                                        sleep(0.5)
                                        dm.movetoex(z[1], z[2], 5, 5)
                                        sleep(0.8)
                                        dm.leftclick()
                                    Li_Kai = Zhao_Tu(885, 663, 1016, 736, '对话1.bmp')
                                    if Li_Kai[0] == -1:
                                        break
                        else:
                            del yichang[0]

def Frun1(hwnd):
    # self.sv.set('当前副本中')
    print('当前副本中')
    FubenJiHe = [['落枫山庄', Fu_Ben],
                 ['水啸钱塘|', Fu_Ben],
                 ['云起台', Fu_Ben],
                 ['清明上河', Fu_Ben],
                 ['冰火湖心', Fu_Ben],
                 ['怒砸黑店', Fu_Ben],

                 ['枫林追迹', Fu_Ben],
                 ['洞天福地', Fu_Ben],
                 ['勇闯辽营|', Fu_Ben],
                 ['神州奇侠', shenzhou],
                 ['虎口夺食', Hu_Kou],
                 ['棋阵迷踪', Qi_Zhen],
                 ]
    c = 0
    while True:
        '''
        while True:
            print('组队中')
            manyuan5 = Zhao_Tu(18, 147, 186, 454, '铁衣.bmp|神像.bmp|龙吟.bmp|素问.bmp|九灵1.bmp|碎梦1.bmp')
            if manyuan5[0] != -1:
                dm.keypresschar('g')
                break
            else:
                tongyi = Zhao_Tu(160, 167, 1156, 475, '同意申请.bmp')
                zudui = Zhao_Tu(480, 342, 756, 544, '组队图标.bmp')
                if tongyi[0] != -1:
                    dm.moveto(tongyi[1], tongyi[2])
                    sleep(1)
                    dm.leftclick()
                    sleep(0.5)
                    dm.keypress(84)
                    sleep(0.5)
                elif zudui[0] != -1:
                    dm.moveto(zudui[1], zudui[2])
                    dm.leftclick()
                    sleep(1)
                else:
                    sleep(3)
        '''

        while True:
            # for fi in l:

            z = dm.findstr(1061, 35, 1241, 100, '落枫山庄|水啸钱塘|云起台|清明上河|'
                                                '冰火湖心|怒砸黑店|枫林追迹|洞天福地|'
                                                '勇闯辽营|神州奇侠|虎口夺食|棋阵迷踪', '52.42.73-2.5.30', 0.65, '', '')
            print(z)
            if z == -1:
                print('等待进副本',now())
                sleep(2)
            else:
                l = ['任务详情.bmp', '买药.bmp', '系统设置.bmp']  ##界面清理
                for ii in l:
                    print('当前副本。{}'.format(FubenJiHe[z][0]),now())
                    sleep(1)
                    r = Zhao_Tu(28, 19, 1299, 733, ii)
                    if r[0] != -1:
                        dm.keypresschar('esc')
                FubenJiHe[z][1]()
                c += 1
                break
def  Zhang_Jian(hwnd):
    print('当前--仗剑江湖')
    while True:
        xx=random.randint(1,10)
        Z = dm.FindMultiColor(1017, 363, 1129, 454, '3db37a-000000',
                              '3|0|40b777-000000,3|5|38b978-000000', 0.95, 0)
        print('任务框',Z)
        if Z[0]==0:
            z = Zhao_Tu(571, 311, 827, 540, '敖青云1.bmp')
            if z[0] != -1:
                print('接任务')
                dm.keypresschar('F')

            else:
                while True:
                    print('找任务')
                    z=Zhao_Tu(163,61,1111,670,'帮贡.bmp|帮贡1.bmp|')
                    if z[0]==-1:
                        dm.keypresschar('j')
                        sleep(xx/5)
                        z=Zhao_Tu(441,313,863,507,'确定1.bmp')
                        if z[0]!=-1:
                            dm.movetoex(z[1],z[2],5,5)
                            sleep(0.5)
                            dm.leftclick()
                        z1 = Zhao_Tu(518,122,803,213, '活动周历.bmp')
                        if z1[0] != -1:
                            dm.keypresschar('esc')
                        sleep(xx/5)
                    else:
                        dm.movetoex(z[1], z[2], 10, 10)
                        sleep(xx / 5)
                        dm.leftclick()
                        sleep(xx / 5)
                        zz= Zhao_Tu(163, 61, 1111, 670, '仗剑江湖.bmp|仗剑江湖1.bmp|')
                        sleep(0.5)
                        dm.movetoex(zz[1]+190,zz[2]+20,10,5)
                        sleep(0.5)
                        dm.leftclick()
                        sleep(0.5)
                        dm.keypresschar('j')
                        print('去接任务')
                        break
            while True:
                z=Zhao_Tu(435,314,839,565,'再见.bmp')
                zz = Zhao_Tu(435,314,839,565, '仗剑江湖3.bmp|')
                if zz[0]==-1 and z[0]!=-1:
                    print('任务完成')
                    return None
                else:
                    if zz[0]!=-1:

                        dm.movetoex(zz[1] , zz[2],50,5)
                        sleep(0.1)
                        dm.leftclick()
                        sleep(0.8)
                        zz1 = Zhao_Tu(1036,511,1261,685, '接受.bmp|')
                        sleep(0.5)
                        dm.movetoex(zz1[1], zz1[2], 15, 5)
                        sleep(0.1)
                        dm.leftclick()
                        sleep(0.5)
                        print('接到任务')
                        break
                    else:
                        sleep(3)



        else:
            for i in ziku:
               # Z1 = dm.findstr(929,319,1283,578, i[0], '147.59.100-5.6.35', 0.8, '', '')
                Z1= Zhao_Tu(88,154,426,246, i[0])
                sleep(0.5)

                if Z1[0]!=-1:
                    print('当前任务-- {}'.format(i[0]))
                    i[1]()
                    sleep(xx/10)
                    print('当前任务{}结束'.format(i[0]))
                    break
                elif i[0]=='结束.bmp':
                    print('任务结束')
                    return None
def  En_Chou(hwnd):
    print('当前--快意恩仇')
    while True:
        xx=random.randint(1,5)/3
        Z = dm.FindMultiColor(1017, 363, 1129, 454, '3db37a-000000',
                              '3|0|40b777-000000,3|5|38b978-000000', 0.95, 0)
        print('任务框',Z)
        if Z[0]==0:
            z = Zhao_Tu(571, 311, 827, 540, '敖青云.bmp|光云长.bmp|敖青云1.bmp')
            if z[0]!=-1:
                dm.keypresschar('F')
            else:
                while True:
                    print('找任务')

                    z=Zhao_Tu(715,526,1021,704,'提问.bmp')
                    if z[0]!=-1:
                        dm.movetoex(z[1]-300,z[2],20,10)
                        sleep(0.1)
                        dm.leftclick()
                        sleep(xx)
                        dm.SendString(hwnd,'快意恩仇')
                        sleep(0.1)
                        dm.keypresschar('enter')
                        sleep(xx)
                        z=dm.findstre(335,207,1002,601,'敖青云','160.68.73-10.10.10',0.95).split('|')
                        sleep(0.5)
                        dm.movetoex(int(z[1])+10,int(z[2])+5,5,5)
                        sleep(0.1)
                        dm.leftclick()
                        sleep(0.5)
                        dm.keypresschar('alt')
                        dm.keypresschar('j')
                        print('去接任务')
                        sleep(xx)
                        break
                    else:
                        dm.keypresschar('alt')
                        dm.keypresschar('j')
                        sleep(2)
            while True:
                z=Zhao_Tu(435,314,839,565,'我要进行修炼.bmp')
                zz = Zhao_Tu(435,314,839,565, '快意恩仇.bmp|')
                if zz[0]==-1 and z[0]!=-1:
                    print('任务完成')
                    #sys.exit()
                    return None
                else:
                    if zz[0]!=-1:
                        dm.movetoex(zz[1] , zz[2],50,5)
                        sleep(0.1)
                        dm.leftclick()
                        sleep(0.75)
                        zz1 = Zhao_Tu(1036,511,1261,685, '接受.bmp|')
                        #sleep(0.5)
                        dm.movetoex(zz1[1], zz1[2], 15, 5)
                        sleep(0.1)
                        dm.leftclick()
                        sleep(0.5)
                        print('接到任务')
                        break
                    else:
                        sleep(3)



        else:
            for i in enchou:
                #Z1 = dm.findstr(1022, 367, 1238, 425, i[0], '147.59.100-5.6.35', 0.8, '', '')
                Z1 = Zhao_Tu(88, 154, 426, 246, i[0])
                print(Z1)
                sleep(0.5)
                if Z1[0]!=-1:
                    print('当前任务{}'.format(i[0]))
                    i[1]()
                    sleep(xx)
                    break
                elif i[0]=='结束':
                    print('任务结束')
                    return None




s=random.randint(30,40)
##押镖，连云寨
def  Ya_Biao(hwnd):
    while True:
        Ren_WU_Kuan = dm.FindMultiColor(965, 327, 1279, 590, '3db27a-000000',
                                        '3|0|41bb79-000000,3|6|37b075-000000', 0.95, 0)
        # Zz = Zhao_Tu(965, 327, 1279, 590, '围攻.bmp|围攻1.bmp')
        print('Ren_WU_Kuan',Ren_WU_Kuan)
        if Ren_WU_Kuan[0] == 0:
            while True:
                print('找任务')

                z = Zhao_Tu(715, 526, 1021, 704, '提问.bmp')
                if z[0] != -1:
                    dm.movetoex(z[1] - 300, z[2], 20, 10)
                    sleep(0.1)
                    dm.leftclick()
                    sleep(1)
                    dm.SendString(hwnd, '连云寨押镖')
                    sleep(0.1)
                    dm.keypresschar('enter')
                    sleep(1)
                    z = dm.findstre(335, 207, 1002, 601, '高俊领', '160.68.73-10.10.10', 0.95).split('|')
                    sleep(0.5)
                    dm.movetoex(int(z[1]) + 10, int(z[2]) + 5, 5, 5)
                    sleep(0.1)
                    dm.leftclick()
                    sleep(0.5)
                    dm.keypresschar('alt')
                    dm.keypresschar('j')
                    print('去接任务')
                    sleep(1)
                    break
                else:
                    dm.keypresschar('alt')
                    dm.keypresschar('j')
                    sleep(2)
            C=100
            while True:
                Li_Kai = dm.FindPic(1168, 678, 1264, 727, '离开.bmp|离开1.bmp|离开2.bmp|', '200.5.60-180.5.20', 0.7, 3)
                # Zz = Zhao_Tu(965, 327, 1279, 590, '围攻.bmp|围攻1.bmp')
                # print(Zz)
                if Li_Kai[0] != -1:
                    dm.keypresschar('F')
                    zz1 = Zhao_Tu(1036, 511, 1261, 685, '接受.bmp|')
                    # Zz = Zhao_Tu(965, 327, 1279, 590, '围攻.bmp|围攻1.bmp')
                    # print(Zz)
                    z = dm.findstr(268, 444, 924, 648, '最大的福气', '60.0.88-60.5.20', 0.8, '', '')
                    if zz1[0] != -1:
                        zz1 = Zhao_Tu(1036, 511, 1261, 685, '接受.bmp|')
                        sleep(0.5)
                        dm.movetoex(zz1[1], zz1[2], 15, 5)
                        sleep(0.1)
                        dm.leftclick()
                        sleep(1)
                        print('接到任务')
                        Ren_WU_Kuan = dm.FindMultiColor(965, 327, 1279, 590, '3db27a-000000',
                                                        '3|0|41bb79-000000,3|6|37b075-000000', 0.95, 0)
                        # Zz = Zhao_Tu(965, 327, 1279, 590, '围攻.bmp|围攻1.bmp')
                        print('Ren_WU_Kuan', Ren_WU_Kuan)
                        if Ren_WU_Kuan[0] == 0:
                            print('应该是活跃度不够了')
                            return None
                        else:
                            print('接到任务开始跑咯...')
                            break
                    elif z != -1:
                        print('任务已完成')
                        return None
                else:
                    print('正在跑路...休息{}秒'.format(C))
                    sleep(1)
                    C-=1

        else:

                    while True:
                    #Z=Zhao_Tu(965, 327, 1279, 590,'静观其变.bmp')
                        Ren_WU_Kuan = dm.FindMultiColor(965, 327, 1279, 590, '3db27a-000000',
                                                        '3|0|41bb79-000000,3|6|37b075-000000', 0.95, 0)
                        #Zz = Zhao_Tu(965, 327, 1279, 590, '围攻.bmp|围攻1.bmp')
                        #print(Zz)
                        if Ren_WU_Kuan[0]!=0:
                            z = Zhao_Tu(428, 225, 886, 521, '选择奖励.bmp')
                            print('选择奖励.bmp',z)
                            z1 = Zhao_Tu(428, 225, 886, 521, '铜钱奖励.bmp')
                            print('铜钱奖励.bmp',z1)
                            if z[0]==-1:
                                    A()
                                    Ctf()
                                    sleep(s/6)

                            else:
                                dm.movetoex(z1[1],z1[2],30,5)
                                sleep(0.1)
                                dm.leftclick()
                                sleep(0.1)
                                dm.keypresschar('enter')
                                sleep(1)
                                z = Zhao_Tu(428, 225, 886, 521,'选择奖励.bmp')
                                if z[0] != -1:
                                    z = Zhao_Tu(428, 225, 886, 521, '全额交子.bmp')
                                    dm.movetoex(z[1], z[2], 30, 5)
                                    sleep(0.1)
                                    dm.leftclick()
                                    sleep(0.1)
                                    dm.keypresschar('enter')
                                    sleep(1)
                                break
                        else:


                                #print('对话中')
                                while True:
                                    dm.keypresschar('f')
                                    sleep(0.5)
                                    z = dm.findstr(765, 568, 1146, 740, '自动播放中', '30.0.85-30.2.25', 0.8, '', '')
                                    if z == -1:
                                        z=Zhao_Tu(976,599,1169,695,'选择奖励1.bmp')
                                        if z[0]!=-1:
                                            print('选择奖励1.bmp',z)
                                            dm.movetoex(z[1],z[2],100,5)
                                            sleep(0.3)
                                            dm.leftclick()
                                            sleep(0.5)
                                        else:
                                            print('esc')
                                            dm.keypresschar('esc')
                                    Ren_WU_Kuan = dm.FindMultiColor(965, 327, 1279, 590, '3db27a-000000',
                                                                    '3|0|41bb79-000000,3|6|37b075-000000', 0.95, 0)

                                    if Ren_WU_Kuan[0] != 0:
                                        #Ctf()
                                        print('见任务框')
                                        sleep(3)
                                        break
def Tui(hwnd):

    l=input('按w退出')
    if l=='w':
        print('退出')
        dm.UnBindWindow()
        sys.exit()
    else:
        sleep(5)



if __name__ == '__main__':
    hwnd = dm.EnumWindowByProcess("GacRunnerNG.exe", "逆水寒", "", 1).split(',')
    l = dm.BindWindowEx(hwnd[0], 'dx2', 'dx2', 'dx', 'dx.public.disable.window.size|dx.public.hide.dll'
                                                     '', 0)
    sleep(3)
    for i in hwnd :
        t1 = Process(target=zrun1, args=(i, 0, 0,))
    #t2 = Process(target=zrun1, args=(hwnd[1], 1000, 0,))
        t1.start()
        print(i,'开始,返回码',l)
        sleep(1)
    #t2.start()
        print('#1:主线 2：支线 3：副本 4：连云寨押镖 5：仗剑 6：恩仇  7：跟随打怪')

        zz11={'1':run,'2':zrun1,'3':Frun1,'4':Ya_Biao,'5':Zhang_Jian,'6':En_Chou,'7':Fu}
        zz=input('工作模式：' )
        print(zz)
        hwnd = dm.EnumWindowByProcess("GacRunnerNG.exe", "逆水寒", "", 1).split(',')
        print(len(hwnd))
        sleep(1)

        #if len(hwnd)!=1:
        dm.MoveWindow(hwnd[0], 1, 2)
        for i in zz:
            for i1,i2 in zz11.items():
                if i==i1:
                    i2(hwnd[0])



